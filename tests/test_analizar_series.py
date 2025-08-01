"""
Tests para el módulo analizar_series.py
"""

import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
from pathlib import Path
import tempfile
import os
from src.analizar_series import construir_modelo


class TestConstruirModelo:
    """Tests para la función construir_modelo"""
    
    def test_construir_modelo_basico(self, temp_excel_file):
        """Test básico de construcción de modelo"""
        # Act
        metadatos, datos = construir_modelo(temp_excel_file)
        
        # Assert
        assert isinstance(metadatos, pd.DataFrame)
        assert isinstance(datos, pd.DataFrame)
        assert len(metadatos) > 0
        assert len(datos) > 0
    
    def test_construir_modelo_estructura_metadatos(self, temp_excel_file):
        """Test que verifica la estructura de metadatos"""
        # Act
        metadatos, _ = construir_modelo(temp_excel_file)
        
        # Assert
        expected_columns = ['id_serie', 'hoja', 'tipo', 'categoria', 'unidad', 'fecha_inicio', 'fecha_fin']
        for col in expected_columns:
            assert col in metadatos.columns
    
    def test_construir_modelo_estructura_datos(self, temp_excel_file):
        """Test que verifica la estructura de datos"""
        # Act
        _, datos = construir_modelo(temp_excel_file)
        
        # Assert
        expected_columns = ['id_serie', 'fecha', 'valor']
        for col in expected_columns:
            assert col in datos.columns
    
    def test_construir_modelo_filtrado_metadatos(self, temp_excel_file):
        """Test que verifica el filtrado de metadatos"""
        # Act
        metadatos, _ = construir_modelo(temp_excel_file)
        
        # Assert
        # Verificar que no hay valores NaN en tipo y categoria
        assert metadatos['tipo'].notna().all()
        assert metadatos['categoria'].notna().all()
    
    def test_construir_modelo_filtrado_datos(self, temp_excel_file):
        """Test que verifica el filtrado de datos"""
        # Act
        _, datos = construir_modelo(temp_excel_file)
        
        # Assert
        # Verificar que no hay valores NaN en fecha
        assert datos['fecha'].notna().all()
    
    def test_construir_modelo_correspondencia_ids(self, temp_excel_file):
        """Test que verifica la correspondencia entre metadatos y datos"""
        # Act
        metadatos, datos = construir_modelo(temp_excel_file)
        
        # Assert
        # Los IDs en datos deben estar en metadatos
        ids_datos = datos['id_serie'].unique()
        ids_metadatos = metadatos['id_serie'].unique()
        
        for id_serie in ids_datos:
            assert id_serie in ids_metadatos
    
    @patch('pandas.ExcelFile')
    def test_construir_modelo_con_hojas_multiples(self, mock_excel_file):
        """Test con múltiples hojas de Excel"""
        # Arrange
        mock_excel = MagicMock()
        mock_excel.sheet_names = ['Hoja1', 'Hoja2']
        
        # Mock para Hoja1
        df1 = pd.DataFrame({
            0: ['2023-01-01', 'Población', 'Demografía', 'Millones', '2023-12-31', ''] + list(range(10)),
            1: ['2023-01-01', 'PIB', 'Economía', 'Millones USD', '2023-12-31', ''] + list(range(10, 20))
        })
        
        # Mock para Hoja2
        df2 = pd.DataFrame({
            0: ['2023-01-01', 'Inflación', 'Economía', 'Porcentaje', '2023-12-31', ''] + list(range(20, 30)),
            1: ['2023-01-01', 'Desempleo', 'Laboral', 'Porcentaje', '2023-12-31', ''] + list(range(30, 40))
        })
        
        mock_excel.parse.side_effect = [df1, df2]
        mock_excel_file.return_value = mock_excel
        
        # Act
        metadatos, datos = construir_modelo('fake_file.xlsx')
        
        # Assert
        assert len(metadatos) >= 4  # Al menos 4 series (2 por hoja)
        assert len(datos) > 0
    
    def test_construir_modelo_archivo_inexistente(self):
        """Test con archivo que no existe"""
        # Act & Assert
        with pytest.raises(FileNotFoundError):
            construir_modelo('archivo_inexistente.xlsx')
    
    @patch('pandas.ExcelFile')
    def test_construir_modelo_con_datos_vacios(self, mock_excel_file):
        """Test con hojas de Excel vacías"""
        # Arrange
        mock_excel = MagicMock()
        mock_excel.sheet_names = ['Hoja1']
        
        # DataFrame vacío
        df_vacio = pd.DataFrame()
        mock_excel.parse.return_value = df_vacio
        mock_excel_file.return_value = mock_excel
        
        # Act
        metadatos, datos = construir_modelo('fake_file.xlsx')
        
        # Assert
        assert len(metadatos) == 0
        assert len(datos) == 0
    
    @patch('pandas.ExcelFile')
    def test_construir_modelo_con_metadatos_invalidos(self, mock_excel_file):
        """Test con metadatos inválidos (NaN en tipo/categoria)"""
        # Arrange
        mock_excel = MagicMock()
        mock_excel.sheet_names = ['Hoja1']
        
        # DataFrame con metadatos inválidos
        df_invalido = pd.DataFrame({
            0: ['2023-01-01', np.nan, 'Demografía', 'Millones', '2023-12-31', ''] + list(range(10)),
            1: ['2023-01-01', 'PIB', np.nan, 'Millones USD', '2023-12-31', ''] + list(range(10, 20))
        })
        
        mock_excel.parse.return_value = df_invalido
        mock_excel_file.return_value = mock_excel
        
        # Act
        metadatos, datos = construir_modelo('fake_file.xlsx')
        
        # Assert
        # Debe filtrar las filas con NaN en tipo o categoria
        assert len(metadatos) == 0
    
    def test_construir_modelo_tipos_datos(self, temp_excel_file):
        """Test que verifica los tipos de datos correctos"""
        # Act
        metadatos, datos = construir_modelo(temp_excel_file)
        
        # Assert
        # Verificar tipos en metadatos
        assert pd.api.types.is_datetime64_any_dtype(metadatos['fecha_inicio'])
        assert pd.api.types.is_datetime64_any_dtype(metadatos['fecha_fin'])
        assert pd.api.types.is_string_dtype(metadatos['tipo'])
        assert pd.api.types.is_string_dtype(metadatos['categoria'])
        
        # Verificar tipos en datos
        assert pd.api.types.is_datetime64_any_dtype(datos['fecha'])
        assert pd.api.types.is_numeric_dtype(datos['valor'])
        assert pd.api.types.is_string_dtype(datos['id_serie'])
    
    def test_construir_modelo_reset_index(self, temp_excel_file):
        # Act
        metadatos, datos = construir_modelo(temp_excel_file)
        
        # Assert
        # Verificar que los índices empiezan en 0
        assert metadatos.index.tolist() == list(range(len(metadatos)))
        assert datos.index.tolist() == list(range(len(datos)))


class TestConstruirModeloEdgeCases:
    """Tests para casos edge de construir_modelo"""
    
    @patch('pandas.ExcelFile')
    def test_construir_modelo_con_fechas_invalidas(self, mock_excel_file):
        """Test con fechas inválidas en los datos"""
        # Arrange
        mock_excel = MagicMock()
        mock_excel.sheet_names = ['Hoja1']
        
        # DataFrame con fechas inválidas
        df_fechas_invalidas = pd.DataFrame({
            0: ['2023-01-01', 'Población', 'Demografía', 'Millones', '2023-12-31', ''] + 
               ['fecha_invalida', '2023-01-02', '2023-01-03'],
            1: ['2023-01-01', 'PIB', 'Economía', 'Millones USD', '2023-12-31', ''] + 
               [100, 200, 300]
        })
        
        mock_excel.parse.return_value = df_fechas_invalidas
        mock_excel_file.return_value = mock_excel
        
        # Act
        metadatos, datos = construir_modelo('fake_file.xlsx')
        
        # Assert
        # Debe filtrar las fechas inválidas
        assert len(datos) < 3  # Debe ser menor que el total de filas
    
    @patch('pandas.ExcelFile')
    def test_construir_modelo_con_valores_no_numericos(self, mock_excel_file):
        """Test con valores no numéricos en la columna de valores"""
        # Arrange
        mock_excel = MagicMock()
        mock_excel.sheet_names = ['Hoja1']
        
        # DataFrame con valores no numéricos
        df_valores_invalidos = pd.DataFrame({
            0: ['2023-01-01', 'Población', 'Demografía', 'Millones', '2023-12-31', ''] + 
               ['2023-01-01', '2023-01-02', '2023-01-03'],
            1: ['2023-01-01', 'PIB', 'Economía', 'Millones USD', '2023-12-31', ''] + 
               ['texto', 'otro_texto', 300]
        })
        
        mock_excel.parse.return_value = df_valores_invalidos
        mock_excel_file.return_value = mock_excel
        
        # Act
        metadatos, datos = construir_modelo('fake_file.xlsx')
        
        # Assert
        # Debe filtrar los valores no numéricos
        assert len(datos) < 3  # Debe ser menor que el total de filas


class TestConstruirModeloIntegration:
    """Tests de integración para construir_modelo"""
    
    def test_construir_modelo_end_to_end(self, temp_excel_file):
        """Test de integración completo"""
        # Act
        metadatos, datos = construir_modelo(temp_excel_file)
        
        # Assert
        # Verificar que el proceso completo funciona
        assert isinstance(metadatos, pd.DataFrame)
        assert isinstance(datos, pd.DataFrame)
        
        # Verificar que hay correspondencia entre metadatos y datos
        if len(metadatos) > 0 and len(datos) > 0:
            ids_metadatos = set(metadatos['id_serie'])
            ids_datos = set(datos['id_serie'])
            assert ids_datos.issubset(ids_metadatos)
    
    def test_construir_modelo_consistencia_datos(self, temp_excel_file):
        """Test que verifica la consistencia de los datos generados"""
        # Act
        metadatos, datos = construir_modelo(temp_excel_file)
        
        # Assert
        if len(datos) > 0:
            # Verificar que las fechas están en el rango esperado
            for _, row in metadatos.iterrows():
                serie_datos = datos[datos['id_serie'] == row['id_serie']]
                if len(serie_datos) > 0:
                    assert serie_datos['fecha'].min() >= row['fecha_inicio']
                    assert serie_datos['fecha'].max() <= row['fecha_fin'] 