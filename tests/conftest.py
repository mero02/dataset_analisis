"""
Configuración de pytest y fixtures comunes para todos los tests
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import os

# Agregar el directorio src al path para importar módulos
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

@pytest.fixture
def sample_dataframe():
    """Fixture que proporciona un DataFrame de ejemplo para testing"""
    return pd.DataFrame({
        'id_serie': ['serie1', 'serie2', 'serie3', 'serie4', 'serie5'],
        'fecha': pd.date_range('2023-01-01', periods=5),
        'valor': [1.0, 2.0, np.nan, 4.0, 5.0],
        'tipo': ['A', 'B', 'A', 'B', 'A'],
        'categoria': ['X', 'Y', 'X', 'Y', 'X']
    })

@pytest.fixture
def sample_dataframe_with_missing():
    """Fixture con DataFrame que tiene valores faltantes"""
    return pd.DataFrame({
        'id_serie': ['serie1', 'serie2', None, 'serie4', 'serie5'],
        'fecha': [pd.Timestamp('2023-01-01'), pd.Timestamp('2023-01-02'), 
                 None, pd.Timestamp('2023-01-04'), pd.Timestamp('2023-01-05')],
        'valor': [1.0, 2.0, 3.0, None, 5.0],
        'tipo': ['A', 'B', 'A', 'B', 'A'],
        'categoria': ['X', 'Y', 'X', 'Y', 'X']
    })

@pytest.fixture
def sample_metadatos():
    """Fixture con metadatos de ejemplo"""
    return pd.DataFrame({
        'id_serie': ['serie1', 'serie2', 'serie3'],
        'hoja': ['Hoja1', 'Hoja1', 'Hoja2'],
        'tipo': ['Población', 'PIB', 'Inflación'],
        'categoria': ['Demografía', 'Economía', 'Economía'],
        'unidad': ['Millones', 'Millones USD', 'Porcentaje'],
        'fecha_inicio': pd.to_datetime(['2020-01-01', '2020-01-01', '2020-01-01']),
        'fecha_fin': pd.to_datetime(['2023-12-31', '2023-12-31', '2023-12-31'])
    })

@pytest.fixture
def temp_excel_file():
    """Fixture que crea un archivo Excel temporal para testing"""
    with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
        # Crear un DataFrame de ejemplo
        df = pd.DataFrame({
            'Fecha': pd.date_range('2023-01-01', periods=10),
            'Col1': range(10),
            'Col2': range(10, 20)
        })
        
        # Agregar metadatos en las primeras filas
        metadata_df = pd.DataFrame({
            'Col1': ['2023-01-01', 'Población', 'Demografía', 'Millones', '2023-12-31', ''],
            'Col2': ['2023-01-01', 'PIB', 'Economía', 'Millones USD', '2023-12-31', '']
        }, index=['fecha_inicio', 'tipo', 'categoria', 'unidad', 'fecha_fin', ''])
        
        # Combinar metadatos y datos
        combined_df = pd.concat([metadata_df, df])
        
        # Guardar como Excel
        combined_df.to_excel(tmp.name, index=False, header=False)
        yield tmp.name
        # Limpiar después del test (con manejo de errores)
        try:
            os.unlink(tmp.name)
        except (PermissionError, OSError):
            # En Windows, a veces el archivo está en uso
            pass

@pytest.fixture
def mock_config():
    """Fixture con configuración mock para testing"""
    return {
        'host': '127.0.0.1',
        'port': 8050,
        'debug': True,
        'title': 'Test Dashboard'
    } 