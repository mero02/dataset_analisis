# 📋 Comandos de Python - Referencia Rápida

Este archivo contiene todos los comandos de Python que reemplazan las funcionalidades del Makefile eliminado.

## 🚀 Comandos Principales

### **Instalación**
```bash
# Instalar dependencias del proyecto
pip install -e .
pip install -r requirements.txt

# Instalar con dependencias de desarrollo
pip install -e ".[dev]"
```

### **Ejecutar Funcionalidades**
```bash
# Dashboard web interactivo
python main.py --modo dashboard

# Jupyter notebook para análisis
python main.py --modo notebook

# Ejecutar análisis básico y generar reportes
python main.py --modo analisis

# Generar reportes automáticos
python main.py --modo reportes

# Listar reportes generados
python main.py --modo listar-reportes

# Ejecutar análisis completo y lanzar dashboard
python main.py --modo completo
```

### **Comandos Alternativos**
```bash
# Ejecutar dashboard directamente
python visualizations/dashboard.py

# Abrir Jupyter Lab
jupyter lab notebooks/

# Ejecutar scripts específicos
python scripts/crear_datos_ejemplo.py
python scripts/generar_dataframe_categorias.py
```

## 🔧 Desarrollo

### **Testing**
```bash
# Ejecutar todas las pruebas
python -m pytest tests/ -v

# Pruebas con cobertura
python -m pytest tests/ --cov=src --cov-report=html --cov-report=term-missing

# Pruebas específicas
python -m pytest tests/test_reportes.py -v
```

### **Calidad de Código**
```bash
# Formatear código con black
black src/ tests/ main.py

# Verificar estilo del código (linting)
flake8 src/ tests/ main.py

# Verificar tipos con mypy
mypy src/ main.py

# Verificar calidad completa
flake8 src/ tests/ main.py
mypy src/ tests/ main.py
python -m pytest tests/ -v
```

### **Limpieza**
```bash
# Limpiar archivos temporales
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -delete
find . -type d -name "*.egg-info" -exec rm -rf {} +
rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/
```

## ⚙️ Configuración Completa

### **Configurar Proyecto Completo**
```bash
# Instalar dependencias
pip install -e .
pip install -r requirements.txt
pip install -e ".[dev]"

# Formatear código
black src/ tests/ main.py

# Ejecutar pruebas
python -m pytest tests/ -v
```

### **Configurar Entorno de Desarrollo**
```bash
# Instalar dependencias de desarrollo
pip install -e ".[dev]"

# Formatear código
black src/ tests/ main.py

# Verificar calidad
flake8 src/ tests/ main.py
mypy src/ tests/ main.py

# Ejecutar pruebas
python -m pytest tests/ -v
```

### **Configurar para Producción**
```bash
# Instalar para producción
pip install -e .

# Pruebas de producción
python main.py --modo reportes
python main.py --modo listar-reportes
```

## 📊 Generación de Reportes

### **Desde el Dashboard**
1. Ejecutar `python main.py --modo dashboard`
2. Abrir http://localhost:8050
3. Usar los botones de exportación en la interfaz

### **Desde Línea de Comandos**
```bash
# Generar todos los formatos
python main.py --modo reportes

# Ver reportes generados
python main.py --modo listar-reportes
```

## 🔍 Troubleshooting

### **Dependencias Faltantes**
```bash
# Reinstalar dependencias
pip install -e .
pip install -r requirements.txt
```

### **Archivo Excel No Encontrado**
```bash
# Colocar el archivo en data/raw/Datos_Series_Leo.xlsx
```

### **Error con WeasyPrint en Windows**
```bash
# Los reportes PDF pueden fallar en Windows
# Los reportes HTML y Word funcionan perfectamente
```

## 📝 Notas

- Todos los comandos deben ejecutarse desde el directorio raíz del proyecto (`dataset_analisis/`)
- El comando más importante para el dashboard es: `python main.py --modo dashboard`
- Para desarrollo, usa los comandos de testing y calidad de código antes de commits
- Los reportes se generan automáticamente en la carpeta `reportes_generados/` 