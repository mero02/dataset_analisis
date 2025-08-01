"""
Tests para el módulo config.py
"""

import pytest
import pandas as pd
from pathlib import Path
import tempfile
import os
from src import config


class TestConfigConstants:
    """Tests para las constantes de configuración"""
    
    def test_project_root_path(self):
        """Test que verifica que PROJECT_ROOT es un Path válido"""
        assert isinstance(config.PROJECT_ROOT, Path)
        assert config.PROJECT_ROOT.exists()
    
    def test_data_directories_exist(self):
        """Test que verifica que los directorios de datos están definidos"""
        assert isinstance(config.DATA_DIR, Path)
        assert isinstance(config.RAW_DATA_DIR, Path)
        assert isinstance(config.PROCESSED_DATA_DIR, Path)
    
    def test_excel_file_path(self):
        """Test que verifica la ruta del archivo Excel"""
        assert isinstance(config.EXCEL_FILE, Path)
        assert config.EXCEL_FILE.suffix == '.xlsx'
    
    def test_dashboard_config_structure(self):
        """Test que verifica la estructura de DASHBOARD_CONFIG"""
        required_keys = ['host', 'port', 'debug', 'title']
        for key in required_keys:
            assert key in config.DASHBOARD_CONFIG
        
        assert isinstance(config.DASHBOARD_CONFIG['host'], str)
        assert isinstance(config.DASHBOARD_CONFIG['port'], int)
        assert isinstance(config.DASHBOARD_CONFIG['debug'], bool)
        assert isinstance(config.DASHBOARD_CONFIG['title'], str)
    
    def test_plot_config_structure(self):
        """Test que verifica la estructura de PLOT_CONFIG"""
        required_keys = ['theme', 'color_palette', 'figure_size', 'dpi']
        for key in required_keys:
            assert key in config.PLOT_CONFIG
        
        assert isinstance(config.PLOT_CONFIG['theme'], str)
        assert isinstance(config.PLOT_CONFIG['color_palette'], str)
        assert isinstance(config.PLOT_CONFIG['figure_size'], tuple)
        assert len(config.PLOT_CONFIG['figure_size']) == 2
        assert isinstance(config.PLOT_CONFIG['dpi'], int)
    
    def test_data_config_structure(self):
        """Test que verifica la estructura de DATA_CONFIG"""
        required_keys = ['date_format', 'decimal_places', 'missing_value_threshold']
        for key in required_keys:
            assert key in config.DATA_CONFIG
        
        assert isinstance(config.DATA_CONFIG['date_format'], str)
        assert isinstance(config.DATA_CONFIG['decimal_places'], int)
        assert isinstance(config.DATA_CONFIG['missing_value_threshold'], float)
        assert 0 <= config.DATA_CONFIG['missing_value_threshold'] <= 1
    
    def test_export_config_structure(self):
        """Test que verifica la estructura de EXPORT_CONFIG"""
        required_keys = ['csv_encoding', 'excel_engine', 'image_format', 'image_dpi']
        for key in required_keys:
            assert key in config.EXPORT_CONFIG
        
        assert isinstance(config.EXPORT_CONFIG['csv_encoding'], str)
        assert isinstance(config.EXPORT_CONFIG['excel_engine'], str)
        assert isinstance(config.EXPORT_CONFIG['image_format'], str)
        assert isinstance(config.EXPORT_CONFIG['image_dpi'], int)
    
    def test_messages_structure(self):
        """Test que verifica la estructura de MESSAGES"""
        required_keys = ['loading', 'success', 'error', 'file_not_found', 
                        'dependencies_ok', 'structure_ok']
        for key in required_keys:
            assert key in config.MESSAGES
            assert isinstance(config.MESSAGES[key], str)
    
    def test_excel_structure_config(self):
        """Test que verifica la estructura de EXCEL_STRUCTURE"""
        assert 'metadata_rows' in config.EXCEL_STRUCTURE
        assert 'data_start_row' in config.EXCEL_STRUCTURE
        assert 'required_columns' in config.EXCEL_STRUCTURE
        
        # Verificar metadata_rows
        metadata_keys = ['fecha_inicio', 'tipo', 'categoria', 'unidad', 'fecha_fin']
        for key in metadata_keys:
            assert key in config.EXCEL_STRUCTURE['metadata_rows']
            assert isinstance(config.EXCEL_STRUCTURE['metadata_rows'][key], int)
        
        # Verificar data_start_row
        assert isinstance(config.EXCEL_STRUCTURE['data_start_row'], int)
        assert config.EXCEL_STRUCTURE['data_start_row'] > 0
        
        # Verificar required_columns
        assert isinstance(config.EXCEL_STRUCTURE['required_columns'], list)
        assert len(config.EXCEL_STRUCTURE['required_columns']) > 0


class TestConfigFunctions:
    """Tests para las funciones de configuración"""
    
    def test_crear_directorios(self, tmp_path):
        """Test para la función crear_directorios"""
        # Arrange - Crear un directorio temporal para testing
        test_dir = tmp_path / "test_project"
        test_dir.mkdir()
        
        # Simular la estructura del proyecto
        data_dir = test_dir / "data"
        raw_dir = data_dir / "raw"
        processed_dir = data_dir / "processed"
        notebooks_dir = test_dir / "notebooks"
        visualizations_dir = test_dir / "visualizations"
        
        # Act - Llamar la función (necesitaríamos mockear las rutas)
        # Por ahora verificamos que la función existe y es callable
        assert callable(config.crear_directorios)
    
    def test_verificar_archivo_excel(self):
        """Test para la función verificar_archivo_excel"""
        # Act
        resultado = config.verificar_archivo_excel()
        
        # Assert
        assert isinstance(resultado, bool)
    
    def test_get_rutas_salida(self):
        """Test para la función get_rutas_salida"""
        # Act
        rutas = config.get_rutas_salida()
        
        # Assert
        assert isinstance(rutas, dict)
        expected_keys = ['resumen_tipos', 'resumen_categorias', 
                        'datos_procesados', 'evolucion_mensual']
        
        for key in expected_keys:
            assert key in rutas
            assert isinstance(rutas[key], Path)
            # Verificar que las rutas apuntan a archivos CSV
            assert rutas[key].suffix == '.csv'


class TestConfigIntegration:
    """Tests de integración para config"""
    
    def test_config_consistency(self):
        """Test que verifica la consistencia entre configuraciones"""
        # Verificar que el puerto del dashboard es un número válido
        assert 1024 <= config.DASHBOARD_CONFIG['port'] <= 65535
        
        # Verificar que el DPI de las imágenes es razonable
        assert 72 <= config.PLOT_CONFIG['dpi'] <= 600
        
        # Verificar que el threshold de valores faltantes es válido
        assert 0 <= config.DATA_CONFIG['missing_value_threshold'] <= 1
    
    def test_path_relationships(self):
        """Test que verifica las relaciones entre rutas"""
        # Verificar que RAW_DATA_DIR está dentro de DATA_DIR
        assert config.RAW_DATA_DIR.parent == config.DATA_DIR
        
        # Verificar que PROCESSED_DATA_DIR está dentro de DATA_DIR
        assert config.PROCESSED_DATA_DIR.parent == config.DATA_DIR
        
        # Verificar que EXCEL_FILE está en RAW_DATA_DIR
        assert config.EXCEL_FILE.parent == config.RAW_DATA_DIR
    
    def test_config_imports(self):
        """Test que verifica que todas las configuraciones se pueden importar"""
        # Verificar que todas las constantes están definidas
        assert hasattr(config, 'PROJECT_ROOT')
        assert hasattr(config, 'DATA_DIR')
        assert hasattr(config, 'DASHBOARD_CONFIG')
        assert hasattr(config, 'PLOT_CONFIG')
        assert hasattr(config, 'DATA_CONFIG')
        assert hasattr(config, 'EXPORT_CONFIG')
        assert hasattr(config, 'MESSAGES')
        assert hasattr(config, 'EXCEL_STRUCTURE') 