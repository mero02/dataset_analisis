"""
Módulo de Reportes para Análisis de Series Temporales

Este módulo proporciona funcionalidades para generar reportes automáticos
en formatos PDF y Word con gráficos, estadísticas y análisis.
"""

from .generador_reportes import GeneradorReportes
from .utils_reportes import exportar_grafico_plotly, generar_estadisticas

__all__ = [
    'GeneradorReportes',
    'exportar_grafico_plotly', 
    'generar_estadisticas'
] 