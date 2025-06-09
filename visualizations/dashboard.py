"""
Dashboard Interactivo para Análisis de Series Temporales

Este script crea una aplicación web interactiva usando Dash para
visualizar y explorar las series temporales de manera dinámica.
"""

import sys
import os
sys.path.append('../src')

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

# Cargar módulos del proyecto
from src.analizar_series import construir_modelo
from src.utils import limpiar_dataframe

# Configuración global
ARCHIVO_EXCEL = 'data/raw/Datos_Series_Leo.xlsx'

# Clase para el dashboard
class SeriesTemporalesDashboard:
    def __init__(self):
        self.app = dash.Dash(
            __name__, 
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            title="Análisis de Series Temporales"
        )
        self.cargar_datos()
        self.setup_layout()
        self.setup_callbacks()
    
    def cargar_datos(self):
        """Carga y procesa los datos"""
        try:
            # Verificar si el archivo existe
            if os.path.exists(ARCHIVO_EXCEL):
                print("🔄 Cargando datos...")
                self.metadatos, self.datos = construir_modelo(ARCHIVO_EXCEL)
                
                # Limpiar datos
                self.datos = limpiar_dataframe(self.datos)
                self.metadatos = self.metadatos.dropna(subset=['tipo', 'categoria'])
                
                # Filtrar series válidas
                series_validas = self.metadatos['id_serie'].unique()
                self.datos = self.datos[self.datos['id_serie'].isin(series_validas)]
                
                # Agregar información de tipo y categoría a los datos
                self.datos['tipo'] = self.datos['id_serie'].map(
                    self.metadatos.set_index('id_serie')['tipo']
                )
                self.datos['categoria'] = self.datos['id_serie'].map(
                    self.metadatos.set_index('id_serie')['categoria']
                )
                
                self.data_loaded = True
                print("✅ Datos cargados correctamente")
            else:
                print(f"❌ No se encontró el archivo: {ARCHIVO_EXCEL}")
                self.data_loaded = False
        except Exception as e:
            print(f"❌ Error al cargar datos: {e}")
            self.data_loaded = False
    #layout 
    def setup_layout(self):
        """Configura el layout de la aplicación"""
        
        # Header
        header = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1("📊 Análisis de Series Temporales", 
                           className="text-center text-primary mb-4"),
                    html.Hr(),
                ], width=12)
            ])
        ])
        
        if not self.data_loaded:
            # Layout para cuando no hay datos
            self.app.layout = dbc.Container([
                header,
                dbc.Alert([
                    html.H4("⚠️ No se pudieron cargar los datos", className="alert-heading"),
                    html.P(f"Por favor, asegúrate de que el archivo 'Datos_Series_Leo.xlsx' "
                          f"esté en la carpeta 'data/raw/'"),
                ], color="warning", className="mt-4")
            ], fluid=True)
            return
        
        # Controles 
        controles = dbc.Container([
            # Controles de selección
            dbc.Row([
                dbc.Col([
                    html.Label("Seleccionar Tipo:", className="fw-bold"),
                    dcc.Dropdown(
                        id='dropdown-tipo',
                        options=[{'label': t, 'value': t} for t in self.datos['tipo'].unique()],
                        value=self.datos['tipo'].unique()[0],
                        clearable=False
                    )
                ], width=4),
                dbc.Col([
                    html.Label("Seleccionar Categoría:", className="fw-bold"),
                    dcc.Dropdown(
                        id='dropdown-categoria',
                        options=[{'label': c, 'value': c} for c in self.datos['categoria'].unique()],
                        value=self.datos['categoria'].unique()[0],
                        clearable=False
                    )
                ], width=4),
                dbc.Col([
                    html.Label("Rango de Fechas:", className="fw-bold"),
                    dcc.DatePickerRange(
                        id='date-picker-range',
                        start_date=self.datos['fecha'].min(),
                        end_date=self.datos['fecha'].max(),
                        display_format='DD/MM/YYYY'
                    )
                ], width=4)
            ], className="mb-4")
        ])
        
        # Métricas principales
        metricas = dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4(f"{len(self.metadatos):,}", className="card-title text-primary"),
                            html.P("Series Totales", className="card-text")
                        ])
                    ])
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4(f"{len(self.datos):,}", className="card-title text-success"),
                            html.P("Registros Totales", className="card-text")
                        ])
                    ])
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4(f"{self.datos['tipo'].nunique()}", className="card-title text-info"),
                            html.P("Tipos Únicos", className="card-text")
                        ])
                    ])
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4(f"{self.datos['categoria'].nunique()}", className="card-title text-warning"),
                            html.P("Categorías Únicas", className="card-text")
                        ])
                    ])
                ], width=3)
            ], className="mb-4")
        ])
        
        # Gráficos
        graficos = dbc.Container([
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
        
        # Layout completo
        self.app.layout = dbc.Container([
            header,
            controles,
            metricas,
            graficos
        ], fluid=True)
    
    def setup_callbacks(self):
        """Configura los callbacks para interactividad"""
        
        if not self.data_loaded:
            return
        
        @self.app.callback(
            [Output('grafico-series-temporales', 'figure'),
             Output('grafico-distribucion-tipos', 'figure'),
             Output('grafico-distribucion-categorias', 'figure'),
             Output('grafico-boxplot', 'figure'),
             Output('grafico-correlacion', 'figure')],
            [Input('dropdown-tipo', 'value'),
             Input('dropdown-categoria', 'value'),
             Input('date-picker-range', 'start_date'),
             Input('date-picker-range', 'end_date')]
        )
        def actualizar_graficos(tipo_seleccionado, categoria_seleccionada, fecha_inicio, fecha_fin):
            # Filtrar datos según selecciones
            datos_filtrados = self.datos.copy()
            
            if fecha_inicio and fecha_fin:
                datos_filtrados = datos_filtrados[
                    (datos_filtrados['fecha'] >= fecha_inicio) &
                    (datos_filtrados['fecha'] <= fecha_fin)
                ]
            
            # Gráfico de series temporales
            fig_temporal = px.line(
                datos_filtrados[datos_filtrados['tipo'] == tipo_seleccionado],
                x='fecha', y='valor', color='id_serie',
                title=f'📈 Series Temporales - Tipo: {tipo_seleccionado}',
                labels={'fecha': 'Fecha', 'valor': 'Valor'}
            )
            fig_temporal.update_layout(showlegend=False)
            
            # Distribución por tipos
            resumen_tipos = datos_filtrados.groupby('tipo').agg({
                'id_serie': 'nunique',
                'valor': 'count'
            }).reset_index()
            resumen_tipos.columns = ['tipo', 'series', 'registros']
            
            fig_tipos = px.bar(
                resumen_tipos, x='tipo', y='registros',
                title='📊 Registros por Tipo',
                color='series'
            )
            
            # Distribución por categorías
            resumen_cats = datos_filtrados.groupby('categoria').agg({
                'id_serie': 'nunique',
                'valor': 'count'
            }).reset_index()
            resumen_cats.columns = ['categoria', 'series', 'registros']
            
            fig_cats = px.pie(
                resumen_cats, values='registros', names='categoria',
                title='🥧 Distribución por Categoría'
            )
            
            # Boxplot por categoría
            fig_box = px.box(
                datos_filtrados[datos_filtrados['categoria'] == categoria_seleccionada],
                x='tipo', y='valor',
                title=f'📦 Distribución de Valores - Categoría: {categoria_seleccionada}'
            )
            
            # Matriz de correlación
            pivot_data = datos_filtrados.pivot_table(
                index='fecha', columns='tipo', values='valor', aggfunc='mean'
            )
            correlacion = pivot_data.corr()
            
            fig_corr = px.imshow(
                correlacion,
                title='🔥 Matriz de Correlación entre Tipos',
                color_continuous_scale='RdBu'
            )
            
            return fig_temporal, fig_tipos, fig_cats, fig_box, fig_corr
    
    def run(self, debug=True, host='127.0.0.1', port=8050):
        """Ejecuta la aplicación"""
        print(f"🚀 Iniciando dashboard en http://{host}:{port}")
        self.app.run(debug=debug, host=host, port=port)

def main():
    """Función principal"""
    dashboard = SeriesTemporalesDashboard()
    dashboard.run()

if __name__ == '__main__':
    main() 