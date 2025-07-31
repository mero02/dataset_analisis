"""
Callbacks para los gráficos del dashboard
"""

import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output

def setup_chart_callbacks(app, datos):
    """Configura los callbacks para los gráficos"""
    
    @app.callback(
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
        """Actualiza todos los gráficos basado en las selecciones"""
        # Filtrar datos según selecciones
        datos_filtrados = datos.copy()
        
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