"""
Callbacks para la exportación de reportes
"""

import dash
from dash import Input, Output
from src.reportes import GeneradorReportes

def setup_export_callbacks(app, datos, metadatos):
    """Configura los callbacks para la exportación de reportes"""
    
    @app.callback(
        Output('alert-exportacion', 'children'),
        Output('alert-exportacion', 'is_open'),
        Output('alert-exportacion', 'color'),
        [Input('btn-pdf', 'n_clicks'),
         Input('btn-word', 'n_clicks'),
         Input('btn-html', 'n_clicks'),
         Input('btn-todos', 'n_clicks')],
        prevent_initial_call=True
    )
    def exportar_reporte(btn_pdf, btn_word, btn_html, btn_todos):
        """Maneja la exportación de reportes"""
        ctx = dash.callback_context
        if not ctx.triggered:
            return "", False, "info"
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        try:
            # Inicializar generador de reportes
            generador = GeneradorReportes(datos, metadatos)
            
            if button_id == 'btn-pdf':
                ruta = generador.generar_pdf()
                mensaje = f"✅ Reporte PDF generado: {ruta}"
                color = "success"
                
            elif button_id == 'btn-word':
                ruta = generador.generar_word()
                mensaje = f"✅ Reporte Word generado: {ruta}"
                color = "success"
                
            elif button_id == 'btn-html':
                ruta = generador.generar_html()
                mensaje = f"✅ Reporte HTML generado: {ruta}"
                color = "success"
                
            elif button_id == 'btn-todos':
                archivos = generador.generar_todos_formatos()
                mensaje = f"✅ Reportes generados: {len(archivos)} archivos creados"
                color = "success"
            else:
                mensaje = "❌ Botón no reconocido"
                color = "danger"
            
            # Mostrar estadísticas de reportes
            stats = generador.obtener_estadisticas_reportes()
            mensaje += f" | Total reportes: {stats['total_archivos']} en {stats['total_fechas']} fechas"
            
            return mensaje, True, color
            
        except Exception as e:
            mensaje = f"❌ Error al generar reporte: {str(e)}"
            return mensaje, True, "danger" 