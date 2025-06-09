import pandas as pd
def limpiar_dataframe(df):
    """
    Limpia el DataFrame eliminando filas con valores faltantes en columnas clave.
    """
    columnas_a_filtrar = ['id_serie', 'fecha', 'valor']  # todas claves
    columnas_presentes = [col for col in columnas_a_filtrar if col in df.columns]
    return df.dropna(subset=columnas_presentes).reset_index(drop=True)
