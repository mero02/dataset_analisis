"""
Paquete para análisis de series temporales.

Este paquete contiene módulos para:
- Cargar y procesar datos desde Excel
- Limpiar y transformar datos
- Generar análisis por categorías y tipos
"""

from .analizar_series import construir_modelo
from .utils import limpiar_dataframe

__version__ = "1.0.0"
__author__ = "Análisis de Datos" 