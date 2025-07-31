"""
Componente Header del Dashboard
"""

import dash_bootstrap_components as dbc
from dash import html

class Header:
    """Componente de encabezado del dashboard"""
    
    @staticmethod
    def create():
        """Crea el componente header"""
        return dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1("📊 Análisis de Series Temporales", 
                           className="text-center text-primary mb-4"),
                    html.Hr(),
                ], width=12)
            ])
        ])
    
    @staticmethod
    def create_error_layout():
        """Crea layout de error cuando no hay datos"""
        return dbc.Container([
            Header.create(),
            dbc.Alert([
                html.H4("⚠️ No se pudieron cargar los datos", className="alert-heading"),
                html.P("Por favor, asegúrate de que el archivo 'Datos_Series_Leo.xlsx' "
                      "esté en la carpeta 'data/raw/'"),
            ], color="warning", className="mt-4")
        ], fluid=True) 