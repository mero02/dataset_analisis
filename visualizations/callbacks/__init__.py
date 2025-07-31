"""
Callbacks del Dashboard de Series Temporales
"""

from .chart_callbacks import setup_chart_callbacks
from .export_callbacks import setup_export_callbacks

__all__ = ['setup_chart_callbacks', 'setup_export_callbacks'] 