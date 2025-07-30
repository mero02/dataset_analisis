"""
Configuración Global del Proyecto de Análisis de Series Temporales

Este archivo centraliza todas las configuraciones y constantes
utilizadas en el proyecto.
"""

import os
from pathlib import Path

# Configuración de rutas
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
SRC_DIR = PROJECT_ROOT / 'src'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'
VISUALIZATIONS_DIR = PROJECT_ROOT / 'visualizations'

# Archivos principales
EXCEL_FILE = RAW_DATA_DIR / 'Datos_Series_Leo.xlsx'
NOTEBOOK_FILE = NOTEBOOKS_DIR / 'analisis_exploratorio.ipynb'

# Configuración del dashboard
DASHBOARD_CONFIG = {
    'host': '127.0.0.1',
    'port': 8050,
    'debug': False,
    'title': 'Análisis de Series Temporales'
}

# Configuración de visualización
PLOT_CONFIG = {
    'theme': 'plotly_white',
    'color_palette': 'viridis',
    'figure_size': (12, 8),
    'dpi': 100
}

# Configuración de datos
DATA_CONFIG = {
    'date_format': '%Y-%m-%d',
    'decimal_places': 2,
    'missing_value_threshold': 0.1  # 10% de valores faltantes máximo
}

# Configuración de exportación
EXPORT_CONFIG = {
    'csv_encoding': 'utf-8',
    'excel_engine': 'openpyxl',
    'image_format': 'png',
    'image_dpi': 300
}

# Mensajes del sistema
MESSAGES = {
    'loading': '🔄 Cargando datos...',
    'success': '✅ Proceso completado exitosamente',
    'error': '❌ Error durante la ejecución',
    'file_not_found': '📁 Archivo no encontrado',
    'dependencies_ok': '✅ Dependencias verificadas',
    'structure_ok': '✅ Estructura de directorios verificada'
}

# Validación de estructura de Excel
EXCEL_STRUCTURE = {
    'metadata_rows': {
        'fecha_inicio': 1,
        'tipo': 2,
        'categoria': 3,
        'unidad': 4,
        'fecha_fin': 5
    },
    'data_start_row': 6,
    'required_columns': ['fecha', 'valor']
}

def crear_directorios():
    """Crea los directorios necesarios si no existen"""
    directorios = [
        DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR,
        NOTEBOOKS_DIR, VISUALIZATIONS_DIR
    ]
    
    for directorio in directorios:
        directorio.mkdir(parents=True, exist_ok=True)

def verificar_archivo_excel():
    """Verifica si el archivo Excel existe"""
    return EXCEL_FILE.exists()

def get_rutas_salida():
    """Retorna las rutas de archivos de salida"""
    return {
        'resumen_tipos': PROCESSED_DATA_DIR / 'resumen_por_tipo.csv',
        'resumen_categorias': PROCESSED_DATA_DIR / 'resumen_por_categoria.csv',
        'datos_procesados': PROCESSED_DATA_DIR / 'datos_completos_procesados.csv',
        'evolucion_mensual': PROCESSED_DATA_DIR / 'evolucion_mensual.csv'
    } 