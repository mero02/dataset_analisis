"""
Utilidad para cargar y procesar datos del dashboard
"""

import os
import sys
sys.path.append('../src')

from src.analizar_series import construir_modelo
from src.utils import limpiar_dataframe

class DataLoader:
    """Clase para cargar y procesar datos del dashboard"""
    
    def __init__(self, archivo_excel='data/raw/Datos_Series_Leo.xlsx'):
        self.archivo_excel = archivo_excel
        self.metadatos = None
        self.datos = None
        self.data_loaded = False
    
    def cargar_datos(self):
        """Carga y procesa los datos"""
        try:
            # Verificar si el archivo existe
            if os.path.exists(self.archivo_excel):
                print("🔄 Cargando datos...")
                self.metadatos, self.datos = construir_modelo(self.archivo_excel)
                
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
                return True
            else:
                print(f"❌ No se encontró el archivo: {self.archivo_excel}")
                self.data_loaded = False
                return False
        except Exception as e:
            print(f"❌ Error al cargar datos: {e}")
            self.data_loaded = False
            return False
    
    def get_datos(self):
        """Retorna los datos procesados"""
        return self.datos
    
    def get_metadatos(self):
        """Retorna los metadatos procesados"""
        return self.metadatos
    
    def is_data_loaded(self):
        """Verifica si los datos están cargados"""
        return self.data_loaded 