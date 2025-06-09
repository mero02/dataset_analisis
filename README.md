# 🔬 Análisis de Series Temporales

Sistema completo para el análisis y visualización de series temporales desde archivos Excel, con múltiples opciones de exploración interactiva.

## 🌟 Características

- **📊 Análisis Exploratorio**: Procesamiento automático de datos desde Excel
- **🎨 Visualizaciones Interactivas**: Gráficos dinámicos con Plotly
- **🚀 Dashboard Web**: Interfaz web para exploración en tiempo real
- **📓 Jupyter Notebooks**: Análisis interactivo paso a paso
- **📁 Estructura Organizada**: Proyecto bien estructurado y modular

## 📁 Estructura del Proyecto

```
dataset_analisis/
├── src/                           # Código fuente
│   ├── __init__.py               # Inicialización del paquete
│   ├── analizar_series.py        # Carga y análisis de datos
│   ├── generar_dataframe_categorias.py  # Agrupación por categorías
│   └── utils.py                  # Utilidades de limpieza
├── data/
│   ├── raw/                      # Datos originales (Excel)
│   └── processed/                # Datos procesados (CSV)
├── notebooks/
│   └── analisis_exploratorio.ipynb  # Notebook principal
├── visualizations/
│   └── dashboard.py              # Dashboard web interactivo
├── main.py                       # Script principal
├── requirements.txt              # Dependencias
└── README.md                     # Esta documentación
```

## 🚀 Instalación y Configuración

### 1. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2. Preparar Datos

Coloca tu archivo `Datos_Series_Leo.xlsx` en la carpeta `data/raw/`

### 3. Verificar Instalación

```bash
python main.py --modo help
```

## 💡 Modos de Uso

### 🔍 Análisis Básico
Ejecuta el procesamiento y genera resúmenes CSV:
```bash
python main.py --modo analisis
```

### 🚀 Dashboard Web Interactivo
Lanza una aplicación web con visualizaciones dinámicas:
```bash
python main.py --modo dashboard
```
Abre tu navegador en `http://localhost:8050`

### 📓 Jupyter Notebook
Abre el notebook para análisis interactivo:
```bash
python main.py --modo notebook
```

### ⚡ Análisis Completo
Ejecuta análisis + dashboard:
```bash
python main.py --modo completo
```

## 📊 Formato del Archivo Excel

Cada hoja debe seguir esta estructura:

| Fila | Contenido              |
|------|------------------------|
| 2    | Fecha de inicio        |
| 3    | Tipo                   |
| 4    | Categoría              |
| 5    | Unidad de medida       |
| 6    | Fecha de fin           |
| 7+   | Fechas y valores       |

## 🎯 Funcionalidades del Dashboard

- **Filtros Interactivos**: Por tipo, categoría y rango de fechas
- **Métricas en Tiempo Real**: Contadores dinámicos
- **Visualizaciones Múltiples**:
  - Series temporales por tipo
  - Distribución por categorías
  - Box plots de valores
  - Matrices de correlación
- **Interfaz Responsiva**: Compatible con dispositivos móviles

## 📈 Visualizaciones Incluidas

### En Jupyter Notebook:
- Análisis exploratorio completo
- Gráficos de distribución temporal
- Heatmaps de correlación
- Análisis estadístico avanzado

### En Dashboard Web:
- Gráficos interactivos con zoom y pan
- Filtros dinámicos
- Métricas en tiempo real
- Exportación de gráficos

## 🛠️ Tecnologías Utilizadas

- **Análisis de Datos**: Pandas, NumPy
- **Visualización**: Plotly, Matplotlib, Seaborn
- **Dashboard Web**: Dash, Dash Bootstrap Components
- **Notebooks**: Jupyter Lab
- **Procesamiento**: openpyxl para Excel

## 📋 Dependencias

```
pandas>=1.3.0          # Manipulación de datos
matplotlib>=3.5.0       # Gráficos estáticos
seaborn>=0.11.0        # Visualizaciones estadísticas
plotly>=5.0.0          # Gráficos interactivos
jupyter>=1.0.0         # Notebooks
ipywidgets>=7.6.0      # Widgets interactivos
openpyxl>=3.0.0        # Lectura de Excel
numpy>=1.21.0          # Computación numérica
scipy>=1.7.0           # Análisis científico
dash>=2.0.0            # Framework web
dash-bootstrap-components>=1.0.0  # Componentes UI
```

## 🔧 Uso Avanzado

### Ejecutar Solo el Dashboard
```python
from visualizations.dashboard import SeriesTemporalesDashboard
dashboard = SeriesTemporalesDashboard()
dashboard.run()
```

### Importar Módulos
```python
from src.analizar_series import construir_modelo
from src.utils import limpiar_dataframe

metadatos, datos = construir_modelo('data/raw/tu_archivo.xlsx')
datos_limpios = limpiar_dataframe(datos)
```

## 🎨 Personalización

### Cambiar Colores del Dashboard
Edita `visualizations/dashboard.py` y modifica:
```python
external_stylesheets=[dbc.themes.BOOTSTRAP]  # Cambiar tema
```

### Agregar Nuevas Visualizaciones
1. Crea nuevas funciones en `dashboard.py`
2. Añade callbacks para interactividad
3. Incluye en el layout

## 🐛 Resolución de Problemas

### Error: "No se encontró el archivo"
- Verifica que `Datos_Series_Leo.xlsx` esté en `data/raw/`
- Verifica que el formato del Excel sea correcto

### Error de Dependencias
```bash
pip install -r requirements.txt --upgrade
```

### Puerto Ocupado (Dashboard)
```python
dashboard.run(port=8051)  # Cambia el puerto
```

## 📞 Soporte

Para reportar problemas o sugerir mejoras:
1. Verifica que el archivo Excel tenga el formato correcto
2. Ejecuta `python main.py --modo help` para ver opciones
3. Revisa que todas las dependencias estén instaladas

## 🎯 Roadmap

- [ ] Exportación de reportes PDF
- [ ] Análisis de estacionalidad
- [ ] Predicciones básicas
- [ ] API REST para integración
- [ ] Autenticación de usuarios

## 📝 Licencia

Este proyecto está bajo licencia MIT. Consulta el archivo LICENSE para más detalles.

---

**¡Disfruta analizando tus series temporales! 📊✨**
