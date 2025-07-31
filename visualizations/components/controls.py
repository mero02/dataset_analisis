"""
Componente de Controles del Dashboard
"""

import dash_bootstrap_components as dbc
from dash import html, dcc

class Controls:
    """Componente de controles del dashboard"""
    
    @staticmethod
    def create(datos):
        """Crea los controles del dashboard"""
        return dbc.Container([
            # Controles de selección
            dbc.Row([
                dbc.Col([
                    html.Label("Seleccionar Tipo:", className="fw-bold"),
                    dcc.Dropdown(
                        id='dropdown-tipo',
                        options=[{'label': t, 'value': t} for t in datos['tipo'].unique()],
                        value=datos['tipo'].unique()[0],
                        clearable=False
                    )
                ], width=3),
                dbc.Col([
                    html.Label("Seleccionar Categoría:", className="fw-bold"),
                    dcc.Dropdown(
                        id='dropdown-categoria',
                        options=[{'label': c, 'value': c} for c in datos['categoria'].unique()],
                        value=datos['categoria'].unique()[0],
                        clearable=False
                    )
                ], width=3),
                dbc.Col([
                    html.Label("Rango de Fechas:", className="fw-bold"),
                    dcc.DatePickerRange(
                        id='date-picker-range',
                        start_date=datos['fecha'].min(),
                        end_date=datos['fecha'].max(),
                        display_format='DD/MM/YYYY'
                    )
                ], width=3),
                dbc.Col([
                    html.Label("Exportar Reporte:", className="fw-bold"),
                    dbc.ButtonGroup([
                        dbc.Button("📄 PDF", id="btn-pdf", color="danger", size="sm"),
                        dbc.Button("📝 Word", id="btn-word", color="primary", size="sm"),
                        dbc.Button("🌐 HTML", id="btn-html", color="success", size="sm"),
                        dbc.Button("📊 Todos", id="btn-todos", color="warning", size="sm")
                    ], vertical=False)
                ], width=3)
            ], className="mb-4"),
            
            # Alertas de exportación
            dbc.Row([
                dbc.Col([
                    dbc.Alert(id="alert-exportacion", is_open=False, duration=4000)
                ], width=12)
            ], className="mb-3")
        ]) 