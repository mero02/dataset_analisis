"""
Componente de Métricas del Dashboard
"""

import dash_bootstrap_components as dbc
from dash import html

class Metrics:
    """Componente de métricas del dashboard"""
    
    @staticmethod
    def create(metadatos, datos):
        """Crea las métricas principales del dashboard"""
        return dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4(f"{len(metadatos):,}", className="card-title text-primary"),
                            html.P("Series Totales", className="card-text")
                        ])
                    ])
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4(f"{len(datos):,}", className="card-title text-success"),
                            html.P("Registros Totales", className="card-text")
                        ])
                    ])
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4(f"{datos['tipo'].nunique()}", className="card-title text-info"),
                            html.P("Tipos Únicos", className="card-text")
                        ])
                    ])
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4(f"{datos['categoria'].nunique()}", className="card-title text-warning"),
                            html.P("Categorías Únicas", className="card-text")
                        ])
                    ])
                ], width=3)
            ], className="mb-4")
        ]) 