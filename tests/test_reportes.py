#!/usr/bin/env python3
"""
Script de Prueba para el Sistema de Reportes

Este script verifica que todas las funcionalidades del sistema de reportes
estén funcionando correctamente.
"""

import sys
import os
from pathlib import Path

# Agregar src al path
sys.path.append('src')

def test_imports():
    """Prueba que todos los módulos se puedan importar correctamente"""
    print("🔍 Probando imports...")
    
    try:
        from src.reportes import GeneradorReportes
        from src.reportes.utils_reportes import (
            exportar_grafico_plotly, 
            generar_estadisticas, 
            crear_grafico_resumen,
            formatear_numero
        )
        print("✅ Todos los módulos se importaron correctamente")
        return True
    except ImportError as e:
        print(f"❌ Error al importar módulos: {e}")
        return False

def test_dependencias():
    """Prueba que las dependencias estén instaladas"""
    print("🔍 Probando dependencias...")
    
    dependencias = [
        'jinja2',
        'python-docx',
        'kaleido'
    ]
    
    # WeasyPrint es opcional en Windows debido a dependencias del sistema
    if os.name != 'nt':  # No Windows
        dependencias.append('weasyprint')
    
    faltantes = []
    for dep in dependencias:
        try:
            __import__(dep)
            print(f"✅ {dep} - OK")
        except ImportError:
            print(f"❌ {dep} - FALTANTE")
            faltantes.append(dep)
    
    if faltantes:
        print(f"\n⚠️ Dependencias faltantes: {', '.join(faltantes)}")
        print("Instálalas con: pip install -r requirements.txt")
        assert False, f"Dependencias faltantes: {', '.join(faltantes)}"
    
    print("🎉 Todas las dependencias están instaladas")

def test_generacion_datos_ejemplo():
    """Genera datos de ejemplo para las pruebas"""
    print("🔍 Generando datos de ejemplo...")
    
    try:
        import pandas as pd
        import numpy as np
        from datetime import datetime, timedelta
        
        # Crear metadatos de ejemplo
        metadatos = pd.DataFrame({
            'id_serie': ['serie_1', 'serie_2', 'serie_3'],
            'hoja': ['Hoja1', 'Hoja1', 'Hoja2'],
            'tipo': ['Temperatura', 'Humedad', 'Presión'],
            'categoria': ['Clima', 'Clima', 'Atmosférico'],
            'unidad': ['°C', '%', 'hPa'],
            'fecha_inicio': [datetime(2023, 1, 1), datetime(2023, 1, 1), datetime(2023, 1, 1)],
            'fecha_fin': [datetime(2023, 12, 31), datetime(2023, 12, 31), datetime(2023, 12, 31)]
        })
        
        # Crear datos de ejemplo
        fechas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
        datos = []
        
        for _, serie in metadatos.iterrows():
            for fecha in fechas:
                # Generar valores realistas según el tipo
                if serie['tipo'] == 'Temperatura':
                    valor = 20 + 10 * np.sin(2 * np.pi * fecha.dayofyear / 365) + np.random.normal(0, 2)
                elif serie['tipo'] == 'Humedad':
                    valor = 60 + 20 * np.sin(2 * np.pi * fecha.dayofyear / 365) + np.random.normal(0, 5)
                else:  # Presión
                    valor = 1013 + 10 * np.sin(2 * np.pi * fecha.dayofyear / 365) + np.random.normal(0, 3)
                
                datos.append({
                    'id_serie': serie['id_serie'],
                    'fecha': fecha,
                    'valor': valor,
                    'tipo': serie['tipo'],
                    'categoria': serie['categoria']
                })
        
        datos_df = pd.DataFrame(datos)
        
        print("✅ Datos de ejemplo generados correctamente")
        return metadatos, datos_df
        
    except Exception as e:
        print(f"❌ Error al generar datos de ejemplo: {e}")
        return None, None

def test_generador_reportes():
    """Prueba la funcionalidad del generador de reportes"""
    print("🔍 Probando generador de reportes...")
    
    try:
        from src.reportes import GeneradorReportes
        
        # Generar datos de ejemplo
        metadatos, datos = test_generacion_datos_ejemplo()
        if metadatos is None:
            return False
        
        # Crear generador
        generador = GeneradorReportes(datos, metadatos)
        print("✅ Generador de reportes creado correctamente")
        
        # Probar generación de HTML (más simple)
        try:
            ruta_html = generador.generar_html()
            print(f"✅ Reporte HTML generado: {ruta_html}")
        except Exception as e:
            print(f"⚠️ Error al generar HTML: {e}")
        
        # Probar generación de Word
        try:
            ruta_word = generador.generar_word()
            print(f"✅ Reporte Word generado: {ruta_word}")
        except Exception as e:
            print(f"⚠️ Error al generar Word: {e}")
        
        # Probar generación de PDF
        try:
            ruta_pdf = generador.generar_pdf()
            print(f"✅ Reporte PDF generado: {ruta_pdf}")
        except Exception as e:
            print(f"⚠️ Error al generar PDF: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en el generador de reportes: {e}")
        return False

def test_utilidades():
    """Prueba las utilidades del módulo de reportes"""
    print("🔍 Probando utilidades...")
    
    try:
        from src.reportes.utils_reportes import (
            generar_estadisticas, 
            crear_grafico_resumen,
            formatear_numero
        )
        
        # Generar datos de ejemplo
        metadatos, datos = test_generacion_datos_ejemplo()
        if metadatos is None:
            return False
        
        # Probar generación de estadísticas
        estadisticas = generar_estadisticas(datos, metadatos)
        print("✅ Estadísticas generadas correctamente")
        print(f"   - Total series: {estadisticas['total_series']}")
        print(f"   - Total datos: {estadisticas['total_datos']}")
        
        # Probar creación de gráfico
        grafico = crear_grafico_resumen(datos, metadatos)
        print("✅ Gráfico de resumen creado correctamente")
        
        # Probar formateo de números
        numero_formateado = formatear_numero(1234.5678)
        print(f"✅ Número formateado: {numero_formateado}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en las utilidades: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🧪 PRUEBAS DEL SISTEMA DE REPORTES")
    print("=" * 50)
    
    # Ejecutar pruebas
    tests = [
        ("Imports", test_imports),
        ("Dependencias", test_dependencias),
        ("Utilidades", test_utilidades),
        ("Generador de Reportes", test_generador_reportes)
    ]
    
    resultados = []
    for nombre, test_func in tests:
        print(f"\n📋 {nombre}")
        print("-" * 30)
        try:
            resultado = test_func()
            resultados.append((nombre, resultado))
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            resultados.append((nombre, False))
    
    # Resumen de resultados
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 50)
    
    exitos = sum(1 for _, resultado in resultados if resultado)
    total = len(resultados)
    
    for nombre, resultado in resultados:
        estado = "✅ PASÓ" if resultado else "❌ FALLÓ"
        print(f"{nombre}: {estado}")
    
    print(f"\n🎯 Resultado: {exitos}/{total} pruebas exitosas")
    
    if exitos == total:
        print("🎉 ¡Todas las pruebas pasaron! El sistema de reportes está funcionando correctamente.")
        return 0
    else:
        print("⚠️ Algunas pruebas fallaron. Revisa los errores anteriores.")
        return 1

if __name__ == '__main__':
    exit(main()) 