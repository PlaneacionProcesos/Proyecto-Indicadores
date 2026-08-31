import pandas as pd

# ============================================================
# CARGA DE DATOS DESDE EXCEL
# ============================================================

df_indicadores = pd.read_excel("data/indicadores.xlsx")
df_centros = pd.read_excel("data/centros_universitarios.xlsx")
df_resultados = pd.read_excel("data/resultados.xlsx")

# ============================================================
# RELACIONAR TABLAS (MERGES)
# ============================================================

resultados_completos = df_resultados.merge(
    df_indicadores, on="indicador_id", how="left"
)

resultados_completos = resultados_completos.merge(
    df_centros, on="centro_universitario_id", how="left"
)


# ============================================================
# UTILIDADES DE INSPECCIÓN / DEBUG
# ============================================================

def mostrar_tablas():
    print("\n" + "=" * 80)
    print("TABLA INDICADORES")
    print("=" * 80)
    print(df_indicadores.head(10))
    print(f"\nRegistros: {len(df_indicadores)} | Columnas: {df_indicadores.columns.tolist()}")

    print("\n" + "=" * 80)
    print("TABLA CENTROS UNIVERSITARIOS")
    print("=" * 80)
    print(df_centros.head(10))
    print(f"\nRegistros: {len(df_centros)} | Columnas: {df_centros.columns.tolist()}")

    print("\n" + "=" * 80)
    print("TABLA RESULTADOS")
    print("=" * 80)
    print(df_resultados.head(10))
    print(f"\nRegistros: {len(df_resultados)} | Columnas: {df_resultados.columns.tolist()}")

    print("\n" + "=" * 80)
    print("TABLA RESULTADOS COMPLETOS (MERGES)")
    print("=" * 80)
    print(resultados_completos.head(10))
    print(f"\nRegistros: {len(resultados_completos)} | Columnas: {resultados_completos.columns.tolist()}")


if __name__ == "__main__":
    mostrar_tablas()
