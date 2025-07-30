"""
Script para crear datos de ejemplo para probar el sistema de análisis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def crear_datos_ejemplo():
    """Crea un archivo Excel de ejemplo con el formato correcto"""
    
    # Crear el directorio si no existe
    os.makedirs('data/raw', exist_ok=True)
    
    # Configurar fechas
    fecha_inicio = datetime(2020, 1, 1)
    fecha_fin = datetime(2023, 12, 31)
    fechas = pd.date_range(start=fecha_inicio, end=fecha_fin, freq='M')
    
    # Crear libro de Excel
    with pd.ExcelWriter('data/raw/Datos_Series_Leo.xlsx', engine='openpyxl') as writer:
        
        # Hoja 1: Series Económicas
        df_economicas = pd.DataFrame()
        
        # Estructura de metadatos
        df_economicas.loc[0, 0] = None  # Fila 1 vacía
        df_economicas.loc[1, 0] = fecha_inicio  # Fecha inicio
        df_economicas.loc[2, 0] = 'Económico'   # Tipo
        df_economicas.loc[3, 0] = 'PIB'         # Categoría
        df_economicas.loc[4, 0] = 'Millones USD'  # Unidad
        df_economicas.loc[5, 0] = fecha_fin     # Fecha fin
        
        # Columna 1: PIB
        df_economicas.loc[1, 1] = fecha_inicio
        df_economicas.loc[2, 1] = 'Económico'
        df_economicas.loc[3, 1] = 'PIB'
        df_economicas.loc[4, 1] = 'Millones USD'
        df_economicas.loc[5, 1] = fecha_fin
        
        # Columna 2: Inflación
        df_economicas.loc[1, 2] = fecha_inicio
        df_economicas.loc[2, 2] = 'Económico'
        df_economicas.loc[3, 2] = 'Inflación'
        df_economicas.loc[4, 2] = 'Porcentaje'
        df_economicas.loc[5, 2] = fecha_fin
        
        # Datos temporales (fila 6 en adelante)
        for i, fecha in enumerate(fechas):
            fila = i + 6
            df_economicas.loc[fila, 0] = fecha  # Columna de fechas
            
            # PIB con tendencia creciente + ruido
            pib_base = 1000000 + i * 5000
            pib_ruido = np.random.normal(0, 50000)
            df_economicas.loc[fila, 1] = pib_base + pib_ruido
            
            # Inflación con ciclos
            inflacion_base = 3.0 + 2.0 * np.sin(i * 0.5)
            inflacion_ruido = np.random.normal(0, 0.5)
            df_economicas.loc[fila, 2] = max(0, inflacion_base + inflacion_ruido)
        
        df_economicas.to_excel(writer, sheet_name='Economicas', index=False, header=False)
        
        # Hoja 2: Series Sociales
        df_sociales = pd.DataFrame()
        
        # Metadatos para series sociales
        df_sociales.loc[1, 0] = fecha_inicio
        df_sociales.loc[2, 0] = 'Social'
        df_sociales.loc[3, 0] = 'Población'
        df_sociales.loc[4, 0] = 'Miles de personas'
        df_sociales.loc[5, 0] = fecha_fin
        
        df_sociales.loc[1, 1] = fecha_inicio
        df_sociales.loc[2, 1] = 'Social'
        df_sociales.loc[3, 1] = 'Población'
        df_sociales.loc[4, 1] = 'Miles de personas'
        df_sociales.loc[5, 1] = fecha_fin
        
        df_sociales.loc[1, 2] = fecha_inicio
        df_sociales.loc[2, 2] = 'Social'
        df_sociales.loc[3, 2] = 'Empleo'
        df_sociales.loc[4, 2] = 'Porcentaje'
        df_sociales.loc[5, 2] = fecha_fin
        
        # Datos temporales
        for i, fecha in enumerate(fechas):
            fila = i + 6
            df_sociales.loc[fila, 0] = fecha
            
            # Población con crecimiento constante
            poblacion = 50000 + i * 100 + np.random.normal(0, 50)
            df_sociales.loc[fila, 1] = poblacion
            
            # Tasa de empleo con variaciones
            empleo_base = 85.0 + 5.0 * np.sin(i * 0.3)
            empleo_ruido = np.random.normal(0, 2.0)
            df_sociales.loc[fila, 2] = max(70, min(95, empleo_base + empleo_ruido))
        
        df_sociales.to_excel(writer, sheet_name='Sociales', index=False, header=False)
        
        # Hoja 3: Series Ambientales
        df_ambientales = pd.DataFrame()
        
        # Metadatos
        df_ambientales.loc[1, 0] = fecha_inicio
        df_ambientales.loc[2, 0] = 'Ambiental'
        df_ambientales.loc[3, 0] = 'Temperatura'
        df_ambientales.loc[4, 0] = 'Grados Celsius'
        df_ambientales.loc[5, 0] = fecha_fin
        
        df_ambientales.loc[1, 1] = fecha_inicio
        df_ambientales.loc[2, 1] = 'Ambiental'
        df_ambientales.loc[3, 1] = 'Temperatura'
        df_ambientales.loc[4, 1] = 'Grados Celsius'
        df_ambientales.loc[5, 1] = fecha_fin
        
        df_ambientales.loc[1, 2] = fecha_inicio
        df_ambientales.loc[2, 2] = 'Ambiental'
        df_ambientales.loc[3, 2] = 'Precipitación'
        df_ambientales.loc[4, 2] = 'mm'
        df_ambientales.loc[5, 2] = fecha_fin
        
        # Datos temporales
        for i, fecha in enumerate(fechas):
            fila = i + 6
            df_ambientales.loc[fila, 0] = fecha
            
            # Temperatura con ciclo anual
            mes = fecha.month
            temp_base = 15 + 10 * np.sin((mes - 3) * np.pi / 6)
            temp_ruido = np.random.normal(0, 2)
            df_ambientales.loc[fila, 1] = temp_base + temp_ruido
            
            # Precipitación estacional
            precip_base = 100 + 50 * np.sin((mes - 6) * np.pi / 6)
            precip_ruido = np.random.normal(0, 20)
            df_ambientales.loc[fila, 2] = max(0, precip_base + precip_ruido)
        
        df_ambientales.to_excel(writer, sheet_name='Ambientales', index=False, header=False)
    
    print("✅ Archivo de ejemplo creado: data/raw/Datos_Series_Leo.xlsx")
    print("📊 Contenido:")
    print("   - Hoja 'Economicas': PIB e Inflación (2020-2023)")
    print("   - Hoja 'Sociales': Población y Empleo (2020-2023)")
    print("   - Hoja 'Ambientales': Temperatura y Precipitación (2020-2023)")
    print("   - 48 registros por serie (mensuales)")

if __name__ == '__main__':
    crear_datos_ejemplo() 