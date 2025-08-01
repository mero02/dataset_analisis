# 🧪 Guía de Testing

Esta guía explica cómo ejecutar y escribir tests para el proyecto de análisis de series temporales.

## 📋 Índice

- [Ejecutar Tests](#-ejecutar-tests)
- [Estructura de Tests](#-estructura-de-tests)
- [Escribir Tests](#-escribir-tests)
- [Fixtures](#-fixtures)
- [Cobertura de Código](#-cobertura-de-código)
- [Mejores Prácticas](#-mejores-prácticas)

## 🚀 Ejecutar Tests

### Comandos Básicos

```bash
# Ejecutar todos los tests
python -m pytest tests/

# Ejecutar con verbose
python -m pytest tests/ -v

# Ejecutar tests específicos
python -m pytest tests/test_utils.py -v

# Ejecutar test específico
python -m pytest tests/test_utils.py::TestLimpiarDataframe::test_limpiar_dataframe_basico -v
```

### Usando el Script

```bash
# Ejecutar todos los tests
python scripts/run_tests.py

# Ejecutar solo tests unitarios
python scripts/run_tests.py --type unit

# Ejecutar tests con cobertura
python scripts/run_tests.py --type coverage

# Ejecutar tests rápidos (excluir slow)
python scripts/run_tests.py --fast
```

### Tests con Cobertura

```bash
# Ejecutar con cobertura
python -m pytest tests/ --cov=src --cov-report=html --cov-report=term-missing

# Verificar cobertura mínima (80%)
python -m pytest tests/ --cov=src --cov-fail-under=80
```

## 📁 Estructura de Tests

```
tests/
├── conftest.py              # Configuración y fixtures comunes
├── test_utils.py            # Tests para src/utils.py
├── test_config.py           # Tests para src/config.py
├── test_analizar_series.py  # Tests para src/analizar_series.py
└── test_reportes.py         # Tests existentes para reportes
```

## ✍️ Escribir Tests

### Estructura de un Test

```python
def test_nombre_del_test(self, fixture_requerida):
    """Docstring descriptivo del test"""
    # Arrange - Preparar datos
    input_data = fixture_requerida
    
    # Act - Ejecutar función
    result = funcion_a_testear(input_data)
    
    # Assert - Verificar resultado
    assert isinstance(result, pd.DataFrame)
    assert len(result) > 0
```

### Patrón AAA (Arrange-Act-Assert)

1. **Arrange**: Preparar los datos y condiciones necesarias
2. **Act**: Ejecutar la función o método que se está probando
3. **Assert**: Verificar que el resultado es el esperado

### Ejemplo Completo

```python
class TestMiFuncion:
    """Tests para mi_funcion"""
    
    def test_mi_funcion_basico(self, sample_dataframe):
        """Test básico de mi_funcion"""
        # Arrange
        df_original = sample_dataframe.copy()
        expected_rows = len(df_original.dropna())
        
        # Act
        resultado = mi_funcion(df_original)
        
        # Assert
        assert isinstance(resultado, pd.DataFrame)
        assert len(resultado) == expected_rows
        assert 'columna_esperada' in resultado.columns
    
    def test_mi_funcion_con_datos_vacios(self):
        """Test con DataFrame vacío"""
        # Arrange
        df_vacio = pd.DataFrame()
        
        # Act
        resultado = mi_funcion(df_vacio)
        
        # Assert
        assert isinstance(resultado, pd.DataFrame)
        assert len(resultado) == 0
```

## 🔧 Fixtures

### Fixtures Disponibles

- `sample_dataframe`: DataFrame de ejemplo con datos válidos
- `sample_dataframe_with_missing`: DataFrame con valores faltantes
- `sample_metadatos`: Metadatos de ejemplo
- `temp_excel_file`: Archivo Excel temporal para testing
- `mock_config`: Configuración mock

### Usar Fixtures

```python
def test_con_fixture(self, sample_dataframe):
    """Test que usa una fixture"""
    # La fixture se inyecta automáticamente
    assert len(sample_dataframe) > 0
    assert 'id_serie' in sample_dataframe.columns
```

### Crear Fixtures Personalizadas

```python
@pytest.fixture
def mi_fixture_personalizada():
    """Fixture personalizada"""
    return {
        'datos': [1, 2, 3],
        'config': {'key': 'value'}
    }
```

## 📊 Cobertura de Código

### Verificar Cobertura

```bash
# Generar reporte HTML
python -m pytest tests/ --cov=src --cov-report=html

# Ver en navegador
open htmlcov/index.html
```

### Cobertura Mínima

El proyecto requiere una cobertura mínima del **80%**. Si no se alcanza, los tests fallarán.

### Excluir Código de Cobertura

```python
# Excluir líneas específicas
if __name__ == '__main__':  # pragma: no cover
    main()
```

## 🎯 Mejores Prácticas

### 1. Nombres Descriptivos

```python
# ✅ Bueno
def test_limpiar_dataframe_elimina_filas_con_nan(self):

# ❌ Malo
def test_limpiar(self):
```

### 2. Tests Independientes

Cada test debe ser independiente y no depender de otros tests.

### 3. Usar Fixtures

Reutilizar datos de prueba con fixtures en lugar de crear datos en cada test.

### 4. Testear Casos Edge

```python
def test_con_dataframe_vacio(self):
def test_con_datos_invalidos(self):
def test_con_valores_extremos(self):
```

### 5. Usar Mocks para Dependencias Externas

```python
@patch('pandas.ExcelFile')
def test_con_archivo_excel(self, mock_excel):
    # Configurar mock
    mock_excel.return_value.sheet_names = ['Hoja1']
    # Test...
```

### 6. Documentar Tests

Cada test debe tener un docstring que explique qué está probando.

### 7. Usar Markers

```python
@pytest.mark.slow
def test_funcion_lenta(self):
    # Test que tarda mucho...

@pytest.mark.integration
def test_integracion_completa(self):
    # Test de integración...
```

## 🚨 Troubleshooting

### Problemas Comunes

**Error de importación:**
```bash
# Asegurarse de estar en el directorio raíz
cd /path/to/project
python -m pytest tests/
```

**Tests que fallan intermitentemente:**
- Verificar que los tests son determinísticos
- Usar `random.seed()` para tests con aleatoriedad
- Evitar dependencias de estado global

**Cobertura baja:**
- Revisar qué líneas no están cubiertas
- Agregar tests para casos edge
- Excluir código que no necesita testing

### Debugging Tests

```bash
# Ejecutar con debugger
python -m pytest tests/ --pdb

# Ejecutar test específico con debugger
python -m pytest tests/test_utils.py::test_especifico --pdb
```

## 📚 Recursos Adicionales

- [Documentación de pytest](https://docs.pytest.org/)
- [Documentación de coverage.py](https://coverage.readthedocs.io/)
- [Mejores prácticas de testing en Python](https://realpython.com/python-testing/) 