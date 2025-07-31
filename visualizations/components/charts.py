"""
Componente de Gráficos del Dashboard
"""

import dash_bootstrap_components as dbc
from dash import dcc

class Charts:
    """Componente de gráficos del dashboard"""
    
    @staticmethod
    def create():
        """Crea los contenedores de gráficos"""
        return dbc.Container([
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='grafico-series-temporales')
                ], width=12)
            ], className="mb-4"),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='grafico-distribucion-tipos')
                ], width=6),
                dbc.Col([
                    dcc.Graph(id='grafico-distribucion-categorias')
                ], width=6)
            ], className="mb-4"),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='grafico-boxplot')
                ], width=6),
                dbc.Col([
                    dcc.Graph(id='grafico-correlacion')
                ], width=6)
            ])
        ]) 