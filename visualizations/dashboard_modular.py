"""
Dashboard Interactivo Modular para Análisis de Series Temporales

Este script crea una aplicación web interactiva usando Dash para
visualizar y explorar las series temporales de manera dinámica.
Versión modular y mantenible.
"""

import dash
import dash_bootstrap_components as dbc

# Importar componentes
from .components import Header, Controls, Metrics, Charts
from .callbacks import setup_chart_callbacks, setup_export_callbacks
from .utils import DataLoader

class SeriesTemporalesDashboard:
    """Dashboard modular para análisis de series temporales"""
    
    def __init__(self, archivo_excel='data/raw/Datos_Series_Leo.xlsx'):
        self.app = dash.Dash(
            __name__, 
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            title="Análisis de Series Temporales"
        )
        
        # Inicializar cargador de datos
        self.data_loader = DataLoader(archivo_excel)
        self.cargar_datos()
        self.setup_layout()
        self.setup_callbacks()
    
    def cargar_datos(self):
        """Carga los datos usando el DataLoader"""
        self.data_loaded = self.data_loader.cargar_datos()
        if self.data_loaded:
            self.datos = self.data_loader.get_datos()
            self.metadatos = self.data_loader.get_metadatos()
    
    def setup_layout(self):
        """Configura el layout de la aplicación"""
        if not self.data_loaded:
            # Layout para cuando no hay datos
            self.app.layout = Header.create_error_layout()
            return
        
        # Layout completo con datos
        self.app.layout = dbc.Container([
            Header.create(),
            Controls.create(self.datos),
            Metrics.create(self.metadatos, self.datos),
            Charts.create()
        ], fluid=True)
    
    def setup_callbacks(self):
        """Configura los callbacks para interactividad"""
        if not self.data_loaded:
            return
        
        # Configurar callbacks de gráficos
        setup_chart_callbacks(self.app, self.datos)
        
        # Configurar callbacks de exportación
        setup_export_callbacks(self.app, self.datos, self.metadatos)
    
    def run(self, debug=True, host='127.0.0.1', port=8050):
        """Ejecuta la aplicación"""
        print(f"🚀 Iniciando dashboard modular en http://{host}:{port}")
        self.app.run(debug=debug, host=host, port=port)

def main():
    """Función principal"""
    dashboard = SeriesTemporalesDashboard()
    dashboard.run()

if __name__ == '__main__':
    main() 