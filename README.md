# Análisis de Series Temporales desde Excel

Este proyecto permite procesar un archivo de Excel con series temporales distribuidas en hojas y columnas. Extrae metadatos, limpia los datos, agrupa por tipo y categoría, y genera archivos CSV resumen.

## Archivos del Proyecto

- `analizar_series.py`: Carga el archivo Excel, extrae y muestra metadatos y una vista previa de los datos.
- `generar_dataframe_categorias.py`: Limpia, agrupa y exporta los datos por tipo y categoría.
- `utils.py`: Contiene funciones auxiliares como la limpieza de `DataFrames`.
- `Datos_Series_Leo.xlsx`: Archivo de entrada con las series temporales (no incluido por defecto en el repo).

## Requisitos

- Python 3.8 o superior
- pandas

### Instalación de dependencias

```bash
pip install -r requirements.txt
```

## Uso

1. Asegurate de tener el archivo `Datos_Series_Leo.xlsx` en el mismo directorio del proyecto.

2. Podés ejecutar los scripts por separado según lo que necesites hacer:

---

### Opción 1: Solo cargar y visualizar los datos

```bash
python analizar_series.py
```

Este script:

- Carga el archivo `.xlsx`
- Extrae metadatos de cada serie
- Imprime una tabla con los metadatos
- Muestra las primeras 10 filas de los datos numéricos

---

### Opción 2: Procesar, limpiar y exportar los datos

```bash
python generar_dataframe_categorias.py
```

Este script:

- Carga los datos desde el Excel
- Aplica limpieza de filas incompletas
- Agrupa las series por `tipo` y `categoría`
- Exporta resúmenes a los archivos:

  - `resumen_por_tipo.csv`
  - `resumen_por_categoria.csv`

También imprime un resumen por consola con la cantidad de series y registros por cada grupo.

---

## Formato del archivo Excel

Cada hoja del archivo Excel debe seguir esta estructura:

| Fila | Contenido              |
|------|------------------------|
| 2    | Fecha de inicio        |
| 3    | Tipo                   |
| 4    | Categoría              |
| 5    | Unidad de medida       |
| 6    | Fecha de fin           |
| 7+   | Fechas y valores       |

Cada columna representa una serie diferente dentro de la hoja.  
La primera columna contiene las fechas, el resto los valores.

---

## Salidas esperadas

- `resumen_por_tipo.csv`
- `resumen_por_categoria.csv`

Estos archivos permiten un seguimiento general de la información agrupada.

---

## Notas

- Las series sin tipo o categoría válida son descartadas.
- Las filas con datos faltantes en columnas clave (`id_serie`, `fecha`, `valor`) también se eliminan.
