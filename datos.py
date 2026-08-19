import pandas as pd

df = pd.DataFrame(
    {
        "mes": ["Enero", "Enero", "Febrero", "Febrero"],
        "producto": ["A", "B", "A", "B"],
        "ventas": [100, 150, 120, 180],
    }
)


df_indicadores = pd.read_excel("data/indicadores.xlsx")

df_centros = pd.read_excel("data/centros_universitarios.xlsx")

df_resultados = pd.read_excel("data/resultados.xlsx")


# ============================================================
# RELACIONAR TABLAS
# ============================================================

resultados_completos = df_resultados.merge(
    df_indicadores, on="indicador_id", how="left"
)

resultados_completos = resultados_completos.merge(
    df_centros, on="centro_universitario_id", how="left"
)


def mostrar_tablas():

    print("\n")
    print("=" * 80)
    print("TABLA INDICADORES")
    print("=" * 80)

    print(df_indicadores.head(10))
    print("\nRegistros:", len(df_indicadores))
    print("Columnas:", df_indicadores.columns.tolist())

    print("\n")
    print("=" * 80)
    print("TABLA CENTROS UNIVERSITARIOS")
    print("=" * 80)

    print(df_centros.head(10))
    print("\nRegistros:", len(df_centros))
    print("Columnas:", df_centros.columns.tolist())

    print("\n")
    print("=" * 80)
    print("TABLA RESULTADOS")
    print("=" * 80)

    print(df_resultados.head(10))
    print("\nRegistros:", len(df_resultados))
    print("Columnas:", df_resultados.columns.tolist())


# ============================================================
# FUNCIONES PARA EL DASHBOARD
# ============================================================


def total_indicadores():
    return resultados_completos["resultado_id"].count()

def total_indicadores_estrategicos():
    return resultados_completos[resultados_completos["tipo de indicador"] == "Estrategico"]["indicador_id"].nunique()

def total_indicadores_sgc():
    return resultados_completos[resultados_completos["tipo de indicador"] == "SGC"]["indicador_id"].nunique()

def resultados_por_ano():

    resultado = resultados_completos.groupby("ano")["resultado"].mean().reset_index()

    return resultado


def resultados_por_indicador():

    resultado = (
        resultados_completos.groupby("nombre indicador")["resultado"]
        .mean()
        .reset_index()
    )

    return resultado


def resultados_por_centro():

    resultado = (
        resultados_completos.groupby("centro_universitario")["resultado"]
        .mean()
        .reset_index()
    )

    return resultado


def resultados_por_modalidad():

    resultado = (
        resultados_completos.groupby("modalidad")["resultado"].mean().reset_index()
    )

    return resultado


# ============================================================
# EJECUCIÓN DIRECTA
# ============================================================

if __name__ == "__main__":

    mostrar_tablas()
