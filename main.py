#!/usr/bin/env python3
"""
Script Principal para Análisis de Series Temporales

Este script proporciona una interfaz unificada para ejecutar todos los
componentes del análisis de series temporales.

Uso:
    python main.py --modo [analisis|dashboard|notebook]
    
Opciones:
    analisis  : Ejecuta el análisis básico y genera reportes
    dashboard : Lanza el dashboard web interactivo
    notebook  : Abre Jupyter Lab con el notebook de análisis
    completo  : Ejecuta análisis y lanza dashboard
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

# Agregar src y scripts al path
sys.path.append('src')
sys.path.append('scripts')

def verificar_estructura():
    """Verifica que la estructura de directorios sea correcta"""
    directorios_requeridos = [
        'src', 'data', 'data/raw', 'data/processed', 
        'notebooks', 'visualizations'
    ]
    
    for directorio in directorios_requeridos:
        Path(directorio).mkdir(parents=True, exist_ok=True)
    
    print("✅ Estructura de directorios verificada")

def verificar_dependencias():
    """Verifica que las dependencias estén instaladas"""
    try:
        import pandas
        import matplotlib
        import seaborn
        import plotly
        import jupyter
        import dash
        print("✅ Dependencias verificadas")
        return True
    except ImportError as e:
        print(f"❌ Dependencia faltante: {e}")
        print("   Ejecuta: pip install -r requirements.txt")
        return False

def ejecutar_analisis():
    """Ejecuta el análisis básico de las series"""
    print("🔄 Ejecutando análisis básico...")
    
    try:
        # Importar y ejecutar análisis
        from src.analizar_series import construir_modelo
        from src.utils import limpiar_dataframe
        from scripts.generar_dataframe_categorias import generar_dataframes_categorias
        
        archivo_excel = 'data/raw/Datos_Series_Leo.xlsx'
        
        if not os.path.exists(archivo_excel):
            print(f"❌ No se encontró el archivo: {archivo_excel}")
            print("   Por favor, coloca el archivo en la carpeta data/raw/")
            return False
        
        # Cargar y procesar datos
        metadatos, datos = construir_modelo(archivo_excel)
        datos = limpiar_dataframe(datos)
        
        # Generar análisis por categorías
        metadatos_validos = metadatos.dropna(subset=['tipo', 'categoria'])
        series_validas = metadatos_validos['id_serie'].unique()
        datos_finales = datos[datos['id_serie'].isin(series_validas)]
        
        df_por_tipo, df_por_categoria = generar_dataframes_categorias(
            metadatos_validos, datos_finales
        )
        
        # Crear directorio de salida
        Path('data/processed').mkdir(parents=True, exist_ok=True)
        
        # Exportar resúmenes
        import pandas as pd
        
        resumen_tipos = pd.DataFrame([
            {"tipo": tipo, "series": df['id_serie'].nunique(), "registros": len(df)}
            for tipo, df in df_por_tipo.items()
        ])
        resumen_tipos.to_csv("data/processed/resumen_por_tipo.csv", index=False)
        
        resumen_categorias = pd.DataFrame([
            {"categoria": cat, "series": df['id_serie'].nunique(), "registros": len(df)}
            for cat, df in df_por_categoria.items()
        ])
        resumen_categorias.to_csv("data/processed/resumen_por_categoria.csv", index=False)
        
        print("✅ Análisis completado exitosamente")
        print("📁 Archivos generados en data/processed/:")
        print("   - resumen_por_tipo.csv")
        print("   - resumen_por_categoria.csv")
        
        return True
        
    except Exception as e:
        print(f"❌ Error durante el análisis: {e}")
        return False

def lanzar_dashboard():
    """Lanza el dashboard web interactivo"""
    print("🚀 Lanzando dashboard web...")
    
    try:
        from visualizations.dashboard import SeriesTemporalesDashboard
        
        dashboard = SeriesTemporalesDashboard()
        dashboard.run(debug=False)
        
    except Exception as e:
        print(f"❌ Error al lanzar dashboard: {e}")
        return False

def abrir_notebook():
    """Abre Jupyter Lab con el notebook de análisis"""
    print("📓 Abriendo Jupyter Lab...")
    
    try:
        # Cambiar al directorio del proyecto
        os.chdir('notebooks')
        
        # Lanzar Jupyter Lab
        subprocess.run(['jupyter', 'lab', 'analisis_exploratorio.ipynb'])
        
    except Exception as e:
        print(f"❌ Error al abrir notebook: {e}")
        return False

def generar_reportes():
    """Genera reportes automáticos en múltiples formatos"""
    print("📊 Generando reportes automáticos...")
    
    try:
        # Importar módulos necesarios
        from src.analizar_series import construir_modelo
        from src.utils import limpiar_dataframe
        from src.reportes import GeneradorReportes
        
        archivo_excel = 'data/raw/Datos_Series_Leo.xlsx'
        
        if not os.path.exists(archivo_excel):
            print(f"❌ No se encontró el archivo: {archivo_excel}")
            print("   Por favor, coloca el archivo en la carpeta data/raw/")
            return False
        
        # Cargar y procesar datos
        print("🔄 Cargando datos...")
        metadatos, datos = construir_modelo(archivo_excel)
        datos = limpiar_dataframe(datos)
        
        # Filtrar datos válidos
        metadatos_validos = metadatos.dropna(subset=['tipo', 'categoria'])
        series_validas = metadatos_validos['id_serie'].unique()
        datos_finales = datos[datos['id_serie'].isin(series_validas)]
        
        # Agregar información de tipo y categoría
        datos_finales['tipo'] = datos_finales['id_serie'].map(
            metadatos_validos.set_index('id_serie')['tipo']
        )
        datos_finales['categoria'] = datos_finales['id_serie'].map(
            metadatos_validos.set_index('id_serie')['categoria']
        )
        
        # Generar reportes
        print("🔄 Generando reportes...")
        generador = GeneradorReportes(datos_finales, metadatos_validos)
        
        # Generar todos los formatos
        archivos_generados = generador.generar_todos_formatos()
        
        print("✅ Reportes generados exitosamente")
        print("📁 Archivos generados en reportes_generados/:")
        for formato, ruta in archivos_generados.items():
            print(f"   - {formato.upper()}: {ruta}")
        
        # Mostrar estadísticas de trazabilidad
        stats = generador.obtener_estadisticas_reportes()
        print(f"\n📊 Estadísticas de Reportes:")
        print(f"   - Total archivos: {stats['total_archivos']}")
        print(f"   - Fechas disponibles: {stats['total_fechas']}")
        print(f"   - Por tipo: PDF={stats['tipos']['pdf']}, Word={stats['tipos']['word']}, HTML={stats['tipos']['html']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al generar reportes: {e}")
        return False

def listar_reportes():
    """Lista todos los reportes generados con trazabilidad"""
    print("📋 Listando reportes generados...")
    
    try:
        from src.reportes import GeneradorReportes
        import pandas as pd
        
        # Crear un generador temporal para acceder a las funciones de listado
        generador = GeneradorReportes(pd.DataFrame(), pd.DataFrame())
        
        # Obtener estadísticas
        stats = generador.obtener_estadisticas_reportes()
        
        if stats['total_archivos'] == 0:
            print("📭 No se encontraron reportes generados")
            return True
        
        print(f"📊 Estadísticas Generales:")
        print(f"   - Total archivos: {stats['total_archivos']}")
        print(f"   - Fechas disponibles: {stats['total_fechas']}")
        print(f"   - Por tipo: PDF={stats['tipos']['pdf']}, Word={stats['tipos']['word']}, HTML={stats['tipos']['html']}")
        
        print(f"\n📁 Reportes por Fecha:")
        reportes = generador.listar_reportes_generados()
        
        for fecha, archivos in reportes.items():
            print(f"\n📅 {fecha}:")
            for archivo in archivos:
                # Extraer solo el nombre del archivo y tipo
                nombre_archivo = os.path.basename(archivo)
                tipo = os.path.dirname(archivo).split(os.sep)[-1]
                print(f"   📄 {tipo.upper()}: {nombre_archivo}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al listar reportes: {e}")
        return False

def mostrar_ayuda():
    """Muestra información de ayuda"""
    print("""
🔬 Análisis de Series Temporales - Guía de Uso
===============================================

Este proyecto te permite analizar series temporales desde archivos Excel 
con múltiples opciones de visualización y generación de reportes automáticos.

📁 Estructura del Proyecto:
├── src/                    # Código fuente
│   └── reportes/          # Sistema de reportes
├── data/
│   ├── raw/               # Datos originales (coloca aquí tu Excel)
│   └── processed/         # Datos procesados
├── notebooks/             # Jupyter notebooks
├── visualizations/        # Dashboard web
├── reportes_generados/    # Reportes automáticos
└── requirements.txt       # Dependencias

🚀 Modos de Ejecución:

1. Análisis Básico:
   python main.py --modo analisis
   
2. Dashboard Web Interactivo:
   python main.py --modo dashboard
   
3. Jupyter Notebook:
   python main.py --modo notebook
   
4. Generar Reportes:
   python main.py --modo reportes
   
5. Listar Reportes Generados:
   python main.py --modo listar-reportes
   
6. Análisis Completo + Dashboard:
   python main.py --modo completo

📊 Funcionalidades de Reportes:
- Generación automática de PDF, Word y HTML
- Gráficos embebidos y estadísticas detalladas
- Templates personalizables
- Exportación desde dashboard web
- Metadatos completos de las series

📋 Requisitos:
- Archivo 'Datos_Series_Leo.xlsx' en data/raw/
- Python 3.8+ con dependencias instaladas
- pip install -r requirements.txt

💡 Recomendaciones:
- Usa 'reportes' para generar documentación automática
- Usa 'completo' para análisis completo con visualizaciones
- Usa 'notebook' para análisis interactivo y exploración
- Usa 'dashboard' para presentaciones y demos con exportación
""")

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description='Análisis de Series Temporales'
    )
    parser.add_argument(
        '--modo', 
        choices=['analisis', 'dashboard', 'notebook', 'reportes', 'listar-reportes', 'completo', 'help'],
        default='help',
        help='Modo de ejecución'
    )
    
    args = parser.parse_args()
    
    print("🔬 Análisis de Series Temporales")
    print("=" * 50)
    
    if args.modo == 'help':
        mostrar_ayuda()
        return
    
    # Verificaciones previas
    verificar_estructura()
    
    if not verificar_dependencias():
        print("\n❌ Por favor, instala las dependencias antes de continuar:")
        print("   pip install -r requirements.txt")
        return
    
    # Ejecutar según el modo seleccionado
    if args.modo == 'analisis':
        ejecutar_analisis()
        
    elif args.modo == 'dashboard':
        lanzar_dashboard()
        
    elif args.modo == 'notebook':
        abrir_notebook()
        
    elif args.modo == 'reportes':
        generar_reportes()
        
    elif args.modo == 'listar-reportes':
        listar_reportes()
        
    elif args.modo == 'completo':
        if ejecutar_analisis():
            print("\n" + "="*50)
            lanzar_dashboard()
    
    print("\n🎯 Proceso completado")

if __name__ == '__main__':
    main() 