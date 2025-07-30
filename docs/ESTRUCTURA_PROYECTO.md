# Estructura del Proyecto - Análisis de Series Temporales

## 📁 Estructura de Directorios

```
analisis_datos/
├── 📁 src/                          # Código fuente principal
│   ├── 📁 reportes/                 # Sistema de reportes automáticos
│   │   ├── 📁 templates/            # Plantillas HTML para reportes
│   │   ├── __init__.py
│   │   ├── generador_reportes.py    # Generador principal de reportes
│   │   └── utils_reportes.py        # Utilidades para reportes
│   ├── __init__.py
│   ├── analizar_series.py           # Análisis de series temporales
│   ├── config.py                    # Configuración global del proyecto
│   └── utils.py                     # Utilidades generales
│
├── 📁 tests/                        # Pruebas unitarias y de integración
│   ├── __init__.py
│   └── test_reportes.py             # Pruebas del sistema de reportes
│
├── 📁 scripts/                      # Scripts de utilidad
│   ├── __init__.py
│   ├── crear_datos_ejemplo.py       # Generador de datos de ejemplo
│   └── generar_dataframe_categorias.py  # Script de análisis por categorías
│
├── 📁 docs/                         # Documentación del proyecto
│   ├── README_GITHUB.md             # README para GitHub
│   └── ESTRUCTURA_PROYECTO.md       # Este archivo
│
├── 📁 data/                         # Datos del proyecto
│   ├── 📁 raw/                      # Datos originales (Excel)
│   └── 📁 processed/                # Datos procesados
│
├── 📁 notebooks/                    # Jupyter notebooks
│   └── analisis.ipynb               # Notebook de análisis exploratorio
│
├── 📁 visualizations/               # Visualizaciones y dashboard
│   └── dashboard.py                 # Dashboard web con Dash
│
├── 📁 reportes_generados/           # Reportes automáticos generados
│   └── 📁 YYYY-MM-DD/               # Organizados por fecha
│       ├── 📁 html/                 # Reportes HTML
│       ├── 📁 word/                 # Reportes Word
│       └── 📁 pdf/                  # Reportes PDF
│
├── 📄 main.py                       # Punto de entrada principal
├── 📄 requirements.txt              # Dependencias del proyecto
├── 📄 pyproject.toml                # Configuración moderna del proyecto
├── 📄 .gitignore                    # Archivos ignorados por Git
├── 📄 .gitignore                    # Archivos ignorados por Git
└── 📄 README.md                     # Documentación principal
```

## 🎯 Propósito de Cada Directorio

### **src/** - Código Fuente Principal
- **reportes/**: Sistema completo de generación de reportes automáticos
- **analizar_series.py**: Lógica principal de análisis de series temporales
- **config.py**: Configuración centralizada del proyecto
- **utils.py**: Funciones utilitarias reutilizables

### **tests/** - Pruebas
- Pruebas unitarias para cada módulo
- Pruebas de integración del sistema completo
- Verificación de funcionalidades críticas

### **scripts/** - Scripts de Utilidad
- Scripts independientes para tareas específicas
- Generadores de datos de ejemplo
- Herramientas de mantenimiento

### **docs/** - Documentación
- Documentación técnica del proyecto
- Guías de usuario
- Documentación para desarrolladores

### **data/** - Datos
- **raw/**: Datos originales en formato Excel
- **processed/**: Datos procesados y limpios

### **notebooks/** - Análisis Interactivo
- Jupyter notebooks para exploración de datos
- Análisis ad-hoc y experimentación

### **visualizations/** - Visualizaciones
- Dashboard web interactivo
- Gráficos y visualizaciones

### **reportes_generados/** - Salida de Reportes
- Organización automática por fecha
- Separación por tipo de formato

## 🚀 Archivos de Configuración

### **pyproject.toml**
- Configuración moderna del proyecto Python
- Metadatos del proyecto
- Dependencias y configuración de herramientas

### **requirements.txt**
- Lista de dependencias específicas
- Versiones exactas para reproducibilidad

## 🔧 Comandos Principales

### **Desarrollo**
```bash
# Instalar dependencias
pip install -e .
pip install -r requirements.txt

# Configurar entorno de desarrollo
pip install -e ".[dev]"
black src/ tests/ main.py
flake8 src/ tests/ main.py
mypy src/ tests/ main.py
python -m pytest tests/ -v

# Ejecutar pruebas
python -m pytest tests/ -v

# Formatear código
black src/ tests/ main.py

# Verificar calidad
flake8 src/ tests/ main.py
mypy src/ tests/ main.py
python -m pytest tests/ -v
```

### **Uso del Sistema**
```bash
# Dashboard web
python main.py --modo dashboard

# Jupyter notebook
python main.py --modo notebook

# Generar reportes
python main.py --modo reportes

# Listar reportes
python main.py --modo listar-reportes
```

### **Producción**
```bash
# Instalar para producción
pip install -e .

# Pruebas de producción
python main.py --modo reportes
python main.py --modo listar-reportes
```

## 📋 Convenciones de Nomenclatura

### **Archivos Python**
- **snake_case**: Para nombres de archivos y funciones
- **PascalCase**: Para nombres de clases
- **UPPER_CASE**: Para constantes

### **Directorios**
- **lowercase**: Para nombres de directorios
- **descriptive**: Nombres que describen el contenido

### **Documentación**
- **README.md**: Documentación principal
- **docs/**: Documentación técnica adicional
- **Comentarios**: En español para consistencia

## 🔄 Flujo de Trabajo

1. **Desarrollo**: Trabajar en `src/` con pruebas en `tests/`
2. **Pruebas**: Ejecutar `python -m pytest tests/ -v` antes de commits
3. **Formateo**: Usar `black src/ tests/ main.py` para consistencia
4. **Documentación**: Mantener `docs/` actualizada
5. **Scripts**: Usar `scripts/` para tareas específicas

## 🎯 Beneficios de esta Estructura

- **✅ Mantenibilidad**: Código organizado y modular
- **✅ Escalabilidad**: Fácil agregar nuevas funcionalidades
- **✅ Testabilidad**: Pruebas separadas y organizadas
- **✅ Documentación**: Estructura clara y documentada
- **✅ Automatización**: Comandos Python para tareas comunes
- **✅ Profesionalismo**: Estructura estándar de la industria 