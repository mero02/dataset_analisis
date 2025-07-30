# 🔬 Análisis de Series Temporales

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.0+-orange.svg)](https://plotly.com/)
[![Dash](https://img.shields.io/badge/Dash-2.0+-purple.svg)](https://dash.plotly.com/)

Sistema completo para analizar y visualizar series temporales desde Excel con dashboard web interactivo.

## 🚀 Instalación Rápida

```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/analisis-series-temporales.git
cd analisis-series-temporales

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Colocar tu Excel en data/raw/Datos_Series_Leo.xlsx

# 4. Ejecutar
python main.py --modo completo
```

## 💡 Modos de Uso

| Comando | Descripción |
|---------|-------------|
| `python main.py --modo analisis` | Procesa datos y genera CSV |
| `python main.py --modo dashboard` | Dashboard web en http://localhost:8050 |
| `python main.py --modo notebook` | Jupyter notebook interactivo |
| `python main.py --modo completo` | Análisis + Dashboard |

## 📊 Formato del Excel

Cada hoja debe tener esta estructura:

| Fila | Contenido |
|------|-----------|
| 2 | Fecha inicio |
| 3 | Tipo (Económico, Social, etc.) |
| 4 | Categoría (PIB, Población, etc.) |
| 5 | Unidad de medida |
| 6 | Fecha fin |
| 7+ | Fechas y valores |

## 🌟 Características

- ✅ **Dashboard Web Interactivo** con filtros y gráficos dinámicos
- ✅ **Jupyter Notebook** para análisis detallado
- ✅ **Procesamiento Automático** de Excel
- ✅ **Visualizaciones Profesionales** con Plotly
- ✅ **Múltiples Modos** de ejecución

## 📁 Estructura

```
dataset_analisis/
├── src/                    # Código fuente
├── data/raw/              # Tu Excel aquí
├── data/processed/        # CSV generados
├── notebooks/             # Jupyter notebooks
├── visualizations/        # Dashboard web
└── main.py               # Script principal
```

## 🛠️ Tecnologías

- **Pandas** - Análisis de datos
- **Plotly** - Visualizaciones interactivas
- **Dash** - Dashboard web
- **Jupyter** - Notebooks interactivos

## 🐛 Problemas Comunes

**Error: "No se encontró el archivo"**
- Verifica que `Datos_Series_Leo.xlsx` esté en `data/raw/`

**Error de dependencias**
```bash
pip install -r requirements.txt --upgrade
```

**Puerto ocupado**
```bash
python main.py --modo dashboard --port 8051
```

## 📞 Soporte

1. Verifica el formato del Excel
2. Ejecuta `python main.py --modo help`
3. Crea un issue en GitHub

## 📝 Licencia

MIT License - Libre para uso personal y comercial.

---
