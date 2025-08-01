"""
Tests para el módulo utils.py
"""

import pytest
import pandas as pd
import numpy as np
from src.utils import limpiar_dataframe


class TestLimpiarDataframe:
    """Clase de tests para la función limpiar_dataframe"""
    
    def test_limpiar_dataframe_basico(self, sample_dataframe):
        """Test básico de limpieza de DataFrame"""
        # Arrange
        df_original = sample_dataframe.copy()
        filas_originales = len(df_original)
        
        # Act
        df_limpio = limpiar_dataframe(df_original)
        
        # Assert
        assert isinstance(df_limpio, pd.DataFrame)
        assert len(df_limpio) <= filas_originales
        assert 'id_serie' in df_limpio.columns
        assert 'fecha' in df_limpio.columns
        assert 'valor' in df_limpio.columns
    
    def test_limpiar_dataframe_con_valores_faltantes(self, sample_dataframe_with_missing):
        """Test con valores faltantes en columnas clave"""
        # Arrange
        df_con_faltantes = sample_dataframe_with_missing.copy()
        filas_con_faltantes = len(df_con_faltantes)
        
        # Act
        df_limpio = limpiar_dataframe(df_con_faltantes)
        
        # Assert
        assert len(df_limpio) < filas_con_faltantes  # Debe eliminar filas con NaN
        assert df_limpio['id_serie'].notna().all()
        assert df_limpio['fecha'].notna().all()
        assert df_limpio['valor'].notna().all()
    
    def test_limpiar_dataframe_solo_columnas_presentes(self):
        """Test cuando no están todas las columnas esperadas"""
        # Arrange
        df_incompleto = pd.DataFrame({
            'id_serie': ['serie1', 'serie2', 'serie3'],
            'valor': [1.0, 2.0, np.nan],
            'otra_columna': ['A', 'B', 'C']
        })
        
        # Act
        df_limpio = limpiar_dataframe(df_incompleto)
        
        # Assert
        assert isinstance(df_limpio, pd.DataFrame)
        assert 'id_serie' in df_limpio.columns
        assert 'valor' in df_limpio.columns
        assert 'otra_columna' in df_limpio.columns
        assert len(df_limpio) < len(df_incompleto)  # Debe eliminar fila con NaN en valor
    
    def test_limpiar_dataframe_dataframe_vacio(self):
        """Test con DataFrame vacío"""
        # Arrange
        df_vacio = pd.DataFrame()
        
        # Act
        df_limpio = limpiar_dataframe(df_vacio)
        
        # Assert
        assert isinstance(df_limpio, pd.DataFrame)
        assert len(df_limpio) == 0
    
    def test_limpiar_dataframe_sin_columnas_clave(self):
        """Test con DataFrame que no tiene columnas clave"""
        # Arrange
        df_sin_claves = pd.DataFrame({
            'columna1': [1, 2, 3],
            'columna2': ['A', 'B', 'C']
        })
        
        # Act
        df_limpio = limpiar_dataframe(df_sin_claves)
        
        # Assert
        assert isinstance(df_limpio, pd.DataFrame)
        assert len(df_limpio) == len(df_sin_claves)  # No debe cambiar nada
        assert list(df_limpio.columns) == list(df_sin_claves.columns)
    
    def test_limpiar_dataframe_preserva_datos_validos(self, sample_dataframe):
        """Test que verifica que se preservan los datos válidos"""
        # Arrange
        df_original = sample_dataframe.copy()
        
        # Act
        df_limpio = limpiar_dataframe(df_original)
        
        # Assert
        # Verificar que los datos válidos se mantienen
        filas_validas = df_original.dropna(subset=['id_serie', 'fecha', 'valor'])
        assert len(df_limpio) == len(filas_validas)
        
        # Verificar que los valores se mantienen iguales (ignorando el índice)
        for col in ['id_serie', 'fecha', 'valor']:
            if col in df_limpio.columns:
                # Resetear índices para comparar solo los valores
                assert df_limpio[col].reset_index(drop=True).equals(
                    filas_validas[col].reset_index(drop=True)
                )
    
    def test_limpiar_dataframe_reset_index(self, sample_dataframe_with_missing):
        """Test que verifica que el índice se resetea correctamente"""
        # Arrange
        df_con_faltantes = sample_dataframe_with_missing.copy()
        
        # Act
        df_limpio = limpiar_dataframe(df_con_faltantes)
        
        # Assert
        # Verificar que el índice empieza en 0 y es continuo
        assert df_limpio.index.tolist() == list(range(len(df_limpio)))
    
    def test_limpiar_dataframe_no_modifica_original(self, sample_dataframe):
        """Test que verifica que no se modifica el DataFrame original"""
        # Arrange
        df_original = sample_dataframe.copy()
        df_original_copy = df_original.copy()
        
        # Act
        df_limpio = limpiar_dataframe(df_original)
        
        # Assert
        # El DataFrame original no debe cambiar
        pd.testing.assert_frame_equal(df_original, df_original_copy)
        # El resultado debe ser diferente (limpio)
        assert not df_limpio.equals(df_original)
    
    def test_limpiar_dataframe_con_diferentes_tipos_datos(self):
        """Test con diferentes tipos de datos en las columnas"""
        # Arrange
        df_mixto = pd.DataFrame({
            'id_serie': ['serie1', 'serie2', None, 'serie4'],
            'fecha': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', None]),
            'valor': [1.0, 'texto', 3.0, 4.0],  # Mezcla de tipos
            'tipo': ['A', 'B', 'A', 'B']
        })
        
        # Act
        df_limpio = limpiar_dataframe(df_mixto)
        
        # Assert
        assert isinstance(df_limpio, pd.DataFrame)
        # Debe eliminar filas con None en columnas clave
        assert df_limpio['id_serie'].notna().all()
        assert df_limpio['fecha'].notna().all() 