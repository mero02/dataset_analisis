import pandas as pd
from src.analizar_series import construir_modelo
from src.utils import limpiar_dataframe
import matplotlib.pyplot as plt

def generar_dataframes_categorias(metadatos, datos):
    """
    Genera diccionarios de DataFrames filtrados por tipo y por categoría.
    """
    df_por_tipo = {}
    # Filtrar y agrupar los datos por tipo
    for tipo_unico in sorted(metadatos['tipo'].dropna().unique()):
        ids = metadatos.loc[metadatos['tipo'] == tipo_unico, 'id_serie']
        df_por_tipo[tipo_unico] = datos[datos['id_serie'].isin(ids)].copy()

    df_por_categoria = {}
    # Filtrar y agrupar los datos por categoría
    for cat_unica in sorted(metadatos['categoria'].dropna().unique()):
        ids = metadatos.loc[metadatos['categoria'] == cat_unica, 'id_serie']
        df_por_categoria[cat_unica] = datos[datos['id_serie'].isin(ids)].copy()

    return df_por_tipo, df_por_categoria


if __name__ == '__main__':
    # Cargar el modelo (metadatos y datos desde el archivo Excel)
    metadatos_series, datos_series = construir_modelo('Datos_Series_Leo.xlsx')

    # Limpieza previa de los datos (eliminar valores faltantes o incorrectos)
    print(f"Total registros originales: {len(datos_series)}")
    datos_series = limpiar_dataframe(datos_series)
    print(f"Total registros luego de limpiar datos: {len(datos_series)}\n")

    # Asegurar que metadatos tengan tipo y categoría válidos
    metadatos_series = metadatos_series.dropna(subset=['tipo', 'categoria']).copy()
    # Filtrar también los datos para que coincidan solo con series válidas
    series_validas = metadatos_series['id_serie'].unique()
    datos_series = datos_series[datos_series['id_serie'].isin(series_validas)].copy()

    # Generar diccionarios filtrados por tipo y por categoría
    df_por_tipo, df_por_categoria = generar_dataframes_categorias(metadatos_series, datos_series)

    # Limpiar valores NaN de cada dataframe
    df_por_tipo = {tipo: limpiar_dataframe(df) for tipo, df in df_por_tipo.items()}
    df_por_categoria = {categoria: limpiar_dataframe(df) for categoria, df in df_por_categoria.items()}

    # Mostrar resumen por tipo
    print("== RESUMEN POR TIPO ==")
    for tipo, df in df_por_tipo.items():
        print(f"• Tipo: {tipo}")
        print(f"   - Series:    {df['id_serie'].nunique()}")
        print(f"   - Registros: {len(df)}\n")

    # Mostrar resumen por categoría
    print("== RESUMEN POR CATEGORÍA ==")
    for categoria, df in df_por_categoria.items():
        print(f"• Categoría: {categoria}")
        print(f"   - Series:    {df['id_serie'].nunique()}")
        print(f"   - Registros: {len(df)}\n")

    # Exportar resúmenes a archivos CSV para un seguimiento posterior
    # Resumen por tipo
    resumen_tipos = pd.DataFrame([
        {"tipo": tipo, "series": df['id_serie'].nunique(), "registros": len(df)}
        for tipo, df in df_por_tipo.items()
    ])
    resumen_tipos.to_csv("resumen_por_tipo.csv", index=False)

    # Resumen por categoría
    resumen_categorias = pd.DataFrame([
        {"categoria": cat, "series": df['id_serie'].nunique(), "registros": len(df)}
        for cat, df in df_por_categoria.items()
    ])
    resumen_categorias.to_csv("resumen_por_categoria.csv", index=False)

    # Gráfico de barras para tipos
    resumen_tipos = pd.DataFrame([
        {"tipo": tipo, "series": df['id_serie'].nunique(), "registros": len(df)}
        for tipo, df in df_por_tipo.items()
    ])
    resumen_tipos.sort_values('registros', ascending=False).plot.bar(
        x='tipo', y='registros', figsize=(10, 6), title='Registros por tipo'
    )
    plt.tight_layout()
    plt.savefig('registros_por_tipo.png')
    plt.close()

    # Gráfico de barras para categorías
    resumen_categorias = pd.DataFrame([
        {"categoria": cat, "series": df['id_serie'].nunique(), "registros": len(df)}
        for cat, df in df_por_categoria.items()
    ])
    resumen_categorias.sort_values('registros', ascending=False).plot.bar(
        x='categoria', y='registros', figsize=(10, 6), title='Registros por categoría'
    )
    plt.tight_layout()
    plt.savefig('registros_por_categoria.png')
    plt.close()
    
    # Mensaje final indicando que los archivos se guardaron correctamente
    print("\nResúmenes exportados a CSV: 'resumen_por_tipo.csv' y 'resumen_por_categoria.csv'")
