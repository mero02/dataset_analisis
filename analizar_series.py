import pandas as pd
from pandas import Timestamp

def construir_modelo(ruta_archivo):
    libro = pd.ExcelFile(ruta_archivo)

    filas_meta = []
    for hoja in libro.sheet_names:
        df = libro.parse(hoja, header=None)
        for col in df.columns:
            id_serie = f"{hoja}__col{col}"

            inicio_raw    = df.iloc[1, col]
            tipo_raw      = df.iloc[2, col]
            categoria_raw = df.iloc[3, col]
            unidad        = df.iloc[4, col]
            fin_raw       = df.iloc[5, col]

            tipo = None if isinstance(tipo_raw, Timestamp) else str(tipo_raw).strip()
            categoria = None if isinstance(categoria_raw, Timestamp) else str(categoria_raw).strip()

            fecha_inicio = pd.to_datetime(inicio_raw, errors='coerce')
            fecha_fin    = pd.to_datetime(fin_raw,    errors='coerce')

            filas_meta.append({
                'id_serie':     id_serie,
                'hoja':         hoja,
                'tipo':         tipo,
                'categoria':    categoria,
                'unidad':       unidad,
                'fecha_inicio': fecha_inicio,
                'fecha_fin':    fecha_fin
            })

    metadatos = (
        pd.DataFrame(filas_meta)
          .dropna(subset=['tipo','categoria'])
          [['id_serie','hoja','tipo','categoria','unidad','fecha_inicio','fecha_fin']]
          .reset_index(drop=True)
    )

    filas_datos = []
    for hoja in libro.sheet_names:
        df = libro.parse(hoja, header=None)
        idx_fecha = df.columns[0]
        fechas    = pd.to_datetime(df.iloc[6:, idx_fecha], errors='coerce')

        for col in df.columns.drop(idx_fecha):
            id_serie = f"{hoja}__col{col}"
            valores  = pd.to_numeric(df.iloc[6:, col], errors='coerce')
            for fecha, valor in zip(fechas, valores):
                filas_datos.append({'id_serie': id_serie, 'fecha': fecha, 'valor': valor})

    datos = (
        pd.DataFrame(filas_datos)
          .dropna(subset=['fecha'])
          .reset_index(drop=True)
    )

    ids_con_valor = datos.dropna(subset=['valor'])['id_serie'].unique()
    metadatos = metadatos[metadatos['id_serie'].isin(ids_con_valor)].reset_index(drop=True)
    datos     = datos    [datos['id_serie'].isin(ids_con_valor)].reset_index(drop=True)

    return metadatos, datos

if __name__ == '__main__':
    ruta = 'Datos_Series_Leo.xlsx'
    metadatos_series, datos_series = construir_modelo(ruta)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 200)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', 100)

    print("\n=== METADATOS DE SERIES ===")
    print(metadatos_series.to_markdown(index=False))

    print("\n=== PRIMERAS 10 FILAS DE DATOS DE SERIES ===")
    print(datos_series.head(10).to_markdown(index=False))
