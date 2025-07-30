"""
Utilidades para la generación de reportes

Funciones auxiliares para exportar gráficos y generar estadísticas
que se incluirán en los reportes.
"""

import os
import base64
import io
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def exportar_grafico_plotly(fig, formato='png', width=800, height=600):
    """
    Exporta un gráfico de Plotly a formato base64 para incluir en reportes
    
    Args:
        fig: Figura de Plotly
        formato: Formato de exportación ('png', 'svg', 'pdf')
        width: Ancho de la imagen
        height: Alto de la imagen
    
    Returns:
        str: Imagen codificada en base64
    """
    try:
        # Convertir figura a imagen
        img_bytes = fig.to_image(format=formato, width=width, height=height)
        
        # Codificar en base64
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        
        return img_base64
    except Exception as e:
        print(f"Error al exportar gráfico: {e}")
        return None

def generar_estadisticas(datos, metadatos):
    """
    Genera estadísticas descriptivas para incluir en reportes
    
    Args:
        datos: DataFrame con los datos de las series
        metadatos: DataFrame con metadatos de las series
    
    Returns:
        dict: Diccionario con estadísticas calculadas
    """
    estadisticas = {
        'fecha_generacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_series': len(metadatos),
        'total_datos': len(datos),
        'rango_fechas': {
            'inicio': datos['fecha'].min().strftime('%Y-%m-%d'),
            'fin': datos['fecha'].max().strftime('%Y-%m-%d')
        },
        'tipos_unicos': metadatos['tipo'].nunique(),
        'categorias_unicas': metadatos['categoria'].nunique(),
        'estadisticas_numericas': {
            'valor_min': datos['valor'].min(),
            'valor_max': datos['valor'].max(),
            'valor_promedio': datos['valor'].mean(),
            'valor_mediana': datos['valor'].median(),
            'desviacion_estandar': datos['valor'].std()
        }
    }
    
    # Estadísticas por tipo
    stats_por_tipo = datos.groupby('tipo')['valor'].agg([
        'count', 'mean', 'std', 'min', 'max'
    ]).round(2).to_dict('index')
    
    estadisticas['estadisticas_por_tipo'] = stats_por_tipo
    
    # Estadísticas por categoría
    stats_por_categoria = datos.groupby('categoria')['valor'].agg([
        'count', 'mean', 'std', 'min', 'max'
    ]).round(2).to_dict('index')
    
    estadisticas['estadisticas_por_categoria'] = stats_por_categoria
    
    return estadisticas

def crear_grafico_resumen(datos, metadatos):
    """
    Crea un gráfico de resumen para incluir en reportes
    
    Args:
        datos: DataFrame con los datos
        metadatos: DataFrame con metadatos
    
    Returns:
        plotly.graph_objects.Figure: Gráfico de resumen
    """
    # Crear subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Distribución por Tipo', 'Distribución por Categoría', 
                       'Evolución Temporal', 'Box Plot por Tipo'),
        specs=[[{"type": "pie"}, {"type": "bar"}],
               [{"type": "scatter"}, {"type": "box"}]]
    )
    
    # Gráfico 1: Distribución por tipo
    tipo_counts = metadatos['tipo'].value_counts()
    fig.add_trace(
        go.Pie(labels=tipo_counts.index, values=tipo_counts.values, name="Por Tipo"),
        row=1, col=1
    )
    
    # Gráfico 2: Distribución por categoría
    categoria_counts = metadatos['categoria'].value_counts().head(10)
    fig.add_trace(
        go.Bar(x=categoria_counts.index, y=categoria_counts.values, name="Por Categoría"),
        row=1, col=2
    )
    
    # Gráfico 3: Evolución temporal (promedio por mes)
    datos_mensual = datos.groupby(datos['fecha'].dt.to_period('M'))['valor'].mean().reset_index()
    datos_mensual['fecha'] = datos_mensual['fecha'].dt.to_timestamp()
    
    fig.add_trace(
        go.Scatter(x=datos_mensual['fecha'], y=datos_mensual['valor'], 
                  mode='lines', name="Evolución Temporal"),
        row=2, col=1
    )
    
    # Gráfico 4: Box plot por tipo
    for tipo in datos['tipo'].unique():
        datos_tipo = datos[datos['tipo'] == tipo]['valor']
        fig.add_trace(
            go.Box(y=datos_tipo, name=tipo, showlegend=False),
            row=2, col=2
        )
    
    fig.update_layout(
        height=800,
        title_text="Resumen de Análisis de Series Temporales",
        showlegend=True
    )
    
    return fig

def formatear_numero(numero, decimales=2):
    """
    Formatea números para mostrar en reportes
    
    Args:
        numero: Número a formatear
        decimales: Número de decimales
    
    Returns:
        str: Número formateado
    """
    if pd.isna(numero):
        return "N/A"
    
    if isinstance(numero, (int, float)):
        return f"{numero:,.{decimales}f}"
    
    return str(numero) 