# 🔬 Análisis de Series Temporales

Sistema completo de análisis de series temporales con visualización interactiva y generación automática de reportes en múltiples formatos.

## 🚀 Características Principales

- **📊 Análisis Exploratorio**: Análisis completo de series temporales desde archivos Excel
- **📈 Visualizaciones Interactivas**: Dashboard web con gráficos dinámicos
- **📄 Reportes Automáticos**: Generación de PDF, Word y HTML con gráficos embebidos
- **🎯 Trazabilidad Completa**: Organización automática de reportes por fecha y tipo
- **🔧 Arquitectura Modular**: Código organizado y mantenible
- **📋 Sistema de Pruebas**: Pruebas unitarias y de integración

## 📁 Estructura del Proyecto

```
analisis_datos/
├── 📁 src/                          # Código fuente principal
│   ├── 📁 reportes/                 # Sistema de reportes automáticos
│   ├── analizar_series.py           # Análisis de series temporales
│   ├── config.py                    # Configuración global
│   └── utils.py                     # Utilidades generales
├── 📁 tests/                        # Pruebas unitarias
├── 📁 scripts/                      # Scripts de utilidad
├── 📁 docs/                         # Documentación técnica
├── 📁 data/                         # Datos del proyecto
├── 📁 notebooks/                    # Jupyter notebooks
├── 📁 visualizations/               # Dashboard web
└── 📁 reportes_generados/           # Reportes organizados por fecha
```

## 🛠️ Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación Rápida
```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd analisis_datos

# Instalar dependencias
pip install -e .
pip install -r requirements.txt
```

### Instalación para Desarrollo
```bash
# Instalar con dependencias de desarrollo
pip install -e ".[dev]"

# Configurar entorno completo
pip install -e ".[dev]"
black src/ tests/ main.py
flake8 src/ tests/ main.py
mypy src/ tests/ main.py
python -m pytest tests/ -v
```

## 🚀 Uso Rápido

### Comandos Principales
```bash
# Dashboard web interactivo
python main.py --modo dashboard

# Jupyter notebook para análisis
python main.py --modo notebook

# Generar reportes automáticos
python main.py --modo reportes

# Listar reportes generados
python main.py --modo listar-reportes
```

### Comandos Alternativos
```bash
# Ejecutar dashboard directamente
python visualizations/dashboard.py

# Abrir Jupyter Lab
jupyter lab notebooks/

# Ejecutar análisis básico
python main.py --modo analisis
```

## 📊 Funcionalidades

### 1. Análisis de Series Temporales
- Carga automática desde archivos Excel
- Limpieza y validación de datos
- Análisis estadístico completo
- Detección de patrones y tendencias

### 2. Dashboard Web Interactivo
- Filtros dinámicos por tipo y categoría
- Gráficos interactivos con Plotly
- Exportación directa de reportes
- Interfaz responsive y moderna

### 3. Sistema de Reportes Automáticos
- **📄 HTML**: Reportes web con gráficos interactivos
- **📝 Word**: Documentos editables con tablas y estadísticas
- **📋 PDF**: Reportes profesionales (limitado en Windows)
- **🎯 Trazabilidad**: Organización automática por fecha

### 4. Notebooks de Análisis
- Análisis exploratorio interactivo
- Experimentación con diferentes técnicas
- Documentación de hallazgos

## 📋 Formato de Datos

### Estructura del Excel
El archivo Excel debe tener la siguiente estructura:

| Fecha Inicio | Tipo | Categoría | Unidad | Fecha Fin |
|--------------|------|-----------|--------|-----------|
| 2020-01-01   | Población | PIB | Millones | 2023-12-31 |
| ...          | ...  | ...       | ...    | ...       |

**Datos de Series:**
| Fecha | Valor |
|-------|-------|
| 2020-01-01 | 100.5 |
| 2020-01-02 | 101.2 |
| ... | ... |

## 🔧 Desarrollo

### Comandos de Desarrollo
```bash
# Ejecutar pruebas
python -m pytest tests/ -v

# Formatear código
black src/ tests/ main.py

# Verificar calidad
flake8 src/ tests/ main.py
mypy src/ tests/ main.py
python -m pytest tests/ -v

# Limpiar archivos temporales
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -delete
find . -type d -name "*.egg-info" -exec rm -rf {} +
rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/
```

### Estructura de Pruebas
```bash
# Ejecutar todas las pruebas
python -m pytest tests/ -v

# Pruebas con cobertura
python -m pytest tests/ --cov=src --cov-report=html --cov-report=term-missing

# Pruebas específicas
python -m pytest tests/test_reportes.py -v
```

## 📈 Generación de Reportes

### Desde el Dashboard
1. Ejecutar `python main.py --modo dashboard`
2. Abrir http://localhost:8050
3. Usar los botones de exportación en la interfaz

### Desde Línea de Comandos
```bash
# Generar todos los formatos
python main.py --modo reportes

# Ver reportes generados
python main.py --modo listar-reportes
```

### Estructura de Reportes
```
reportes_generados/
├── 2025-07-30/
│   ├── html/
│   │   └── reporte_series_temporales_20250730_131342.html
│   ├── word/
│   │   └── reporte_series_temporales_20250730_131342.docx
│   └── pdf/
└── [fechas anteriores]/
```

## 🎯 Casos de Uso

### Para Analistas de Datos
- Análisis exploratorio rápido
- Generación automática de reportes
- Visualización interactiva de resultados

### Para Presentaciones
- Dashboard web para demos
- Reportes profesionales en múltiples formatos
- Gráficos de alta calidad

### Para Desarrollo
- Código modular y mantenible
- Sistema de pruebas completo
- Documentación técnica detallada

## 🔍 Troubleshooting

### Problemas Comunes

**Error con WeasyPrint en Windows:**
```bash
# Los reportes PDF pueden fallar en Windows
# Los reportes HTML y Word funcionan perfectamente
```

**Dependencias faltantes:**
```bash
# Reinstalar dependencias
pip install -e .
pip install -r requirements.txt
```

**Archivo Excel no encontrado:**
```bash
# Colocar el archivo en data/raw/Datos_Series_Leo.xlsx
```

## 📚 Documentación Adicional

- [Estructura del Proyecto](docs/ESTRUCTURA_PROYECTO.md)
- [Guía de Desarrollo](docs/README_GITHUB.md)
- [API de Reportes](src/reportes/)

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

- **Issues**: Reportar bugs y solicitar features
- **Documentación**: Ver `docs/` para guías detalladas
- **Ejemplos**: Ver `notebooks/` para casos de uso

---

**🎉 ¡Gracias por usar nuestro sistema de análisis de series temporales!**
