import pandas as pd
import unicodedata
import re


# ========================================================================================
#                                   FUNCIONES
# ========================================================================================


def separar_responsable_area(texto):

    if pd.isna(texto):
        return None, None

    texto = str(texto).strip()

    # Responsable (Área)
    resultado = re.search(r"^(.*?)\s*\((.*?)\)", texto)

    if resultado:
        responsable = resultado.group(1).strip()
        area = resultado.group(2).strip()

        return responsable, area

    # Responsable / Área
    if "/" in texto:
        responsable, area = texto.split("/", 1)

        responsable = responsable.split("-", 1)[0].strip()
        area = area.split("-", 1)[0].strip()

        return responsable, area

    # Solo responsable
    return texto, None


# ========================================================================================
#                                   EXTRACT
# ========================================================================================

df = pd.read_excel(
    "etl/matriz.xlsx"
)


# ========================================================================================
#                                   TRANSFORM
# ========================================================================================

# ------------------------------------------------------------------------------
# Limpieza de nombres de columnas
# ------------------------------------------------------------------------------

df.columns = df.columns.str.lower().str.strip()

# Quitar tildes de nombres de columnas
df.columns = [
    unicodedata.normalize("NFKD", col)
    .encode("ascii", "ignore")
    .decode("utf-8")
    for col in df.columns
]


# ------------------------------------------------------------------------------
# Correcciones específicas de calidad de datos
# ------------------------------------------------------------------------------

df["responsable medicion"] = df["responsable medicion"].replace(
    "Astrid Viviana Rodriguez Dirección Bienestar Asuntos estudiantiles",
    "Astrid Viviana Rodriguez / Dirección Bienestar Asuntos estudiantiles",
)


# ------------------------------------------------------------------------------
# Separar responsable y área
# ------------------------------------------------------------------------------

df[["responsable", "area"]] = (
    df["responsable medicion"]
    .apply(separar_responsable_area)
    .apply(pd.Series)
)

# Eliminar columna original
df = df.drop(columns=["responsable medicion"])


# ------------------------------------------------------------------------------
# Limpieza de datos
# ------------------------------------------------------------------------------

columnas_texto = [
    "agrupador",
    "proceso",
    "macroproceso",
    "nombre indicador",
    "formula de calculo",
    "sede - c.u",
    "centro_universitario",
    "localidad",
    "periodo academico",
    "nivel academico",
    "modalidad",
    "tiempo de reporte",
    "responsable",
    "area",
    "correo electronico",
    "tipo de indicador",
    "analisis cualitativo",
]


for columna in columnas_texto:

    df[columna] = (
        df[columna]
        .astype("string")
        .str.strip()
        .str.normalize("NFKD")
        .str.encode("ascii", "ignore")
        .str.decode("utf-8")
    )


# Resultado numérico
df["resultado"] = pd.to_numeric(
    df["resultado"],
    errors="coerce"
)


# Año numérico
df["ano"] = pd.to_numeric(
    df["ano"],
    errors="coerce"
)


# ========================================================================================
#                                   MODELO
# ========================================================================================

# ========================================================================================
# 1. TABLA INDICADORES
# ========================================================================================

columnas_indicadores = [
    "numero_ind",
    "agrupador",
    "proceso",
    "macroproceso",
    "nombre indicador",
    "formula de calculo",
    "tipo de indicador",
    "responsable",
    "area",
    "correo electronico",
]


indicadores = (
    df[columnas_indicadores]
    .drop_duplicates()
    .reset_index(drop=True)
)


# PK artificial
indicadores.insert(
    0,
    "indicador_id",
    range(1, len(indicadores) + 1)
)


# ========================================================================================
# 2. TABLA CENTROS UNIVERSITARIOS
# ========================================================================================

columnas_centros = [
    "sede - c.u",
    "centro_universitario",
    "localidad",
]


centros_universitarios = (
    df[columnas_centros]
    .drop_duplicates()
    .reset_index(drop=True)
)


# PK artificial
centros_universitarios.insert(
    0,
    "centro_universitario_id",
    range(1, len(centros_universitarios) + 1)
)


# ========================================================================================
# 3. TABLA RESULTADOS
# ========================================================================================

columnas_resultados = [
    "numero_ind",
    "formula de calculo",
    "sede - c.u",
    "centro_universitario",
    "periodo academico",
    "nivel academico",
    "modalidad",
    "tiempo de reporte",
    "ano",
    "resultado",
    "analisis cualitativo",
]


resultados = df[columnas_resultados].copy()


# ------------------------------------------------------------------------------
# Asociar indicador_id
# ------------------------------------------------------------------------------
#
# Importante:
# numero_ind por sí solo no necesariamente identifica un registro único
# dentro de la tabla indicadores.
#
# Ejemplo:
# ID-EST-GI-037 tiene diferentes fórmulas.
#
# Por eso usamos numero_ind + formula de calculo para identificar
# correctamente el indicador.
# ------------------------------------------------------------------------------

resultados = resultados.merge(
    indicadores[
        [
            "numero_ind",
            "formula de calculo",
            "indicador_id",
        ]
    ],
    on=[
        "numero_ind",
        "formula de calculo",
    ],
    how="left",
)


# ------------------------------------------------------------------------------
# Asociar centro_universitario_id
# ------------------------------------------------------------------------------

resultados = resultados.merge(
    centros_universitarios[
        [
            "sede - c.u",
            "centro_universitario",
            "centro_universitario_id",
        ]
    ],
    on=[
        "sede - c.u",
        "centro_universitario",
    ],
    how="left",
)


# ------------------------------------------------------------------------------
# Estructura final de RESULTADOS
# ------------------------------------------------------------------------------

resultados = resultados[
    [
        "indicador_id",
        "centro_universitario_id",
        "periodo academico",
        "nivel academico",
        "modalidad",
        "tiempo de reporte",
        "ano",
        "resultado",
        "analisis cualitativo",
    ]
].reset_index(drop=True)


# ------------------------------------------------------------------------------
# PK artificial de resultados
# ------------------------------------------------------------------------------

resultados.insert(
    0,
    "resultado_id",
    range(1, len(resultados) + 1)
)


# ========================================================================================
#                                   VALIDACIONES
# ========================================================================================

print("\n")
print("=" * 80)
print("                         VALIDACIONES")
print("=" * 80)


# ------------------------------------------------------------------------------
# Validación 1 - Indicadores sin asociación
# ------------------------------------------------------------------------------

indicadores_sin_asociar = resultados[
    resultados["indicador_id"].isna()
]


if indicadores_sin_asociar.empty:

    print("OK - Todos los resultados tienen un indicador asociado.")

else:

    print(
        f"ERROR - {len(indicadores_sin_asociar)} "
        "resultados no tienen indicador asociado."
    )


# ------------------------------------------------------------------------------
# Validación 2 - Centros sin asociación
# ------------------------------------------------------------------------------

centros_sin_asociar = resultados[
    resultados["centro_universitario_id"].isna()
]


if centros_sin_asociar.empty:

    print("OK - Todos los resultados tienen centro asociado.")

else:

    print(
        f"ERROR - {len(centros_sin_asociar)} "
        "resultados no tienen centro asociado."
    )


# ------------------------------------------------------------------------------
# Validación 3 - Unicidad de indicadores
# ------------------------------------------------------------------------------

clave_indicador = [
    "numero_ind",
    "formula de calculo",
]


duplicados_indicadores = indicadores[
    indicadores.duplicated(
        subset=clave_indicador,
        keep=False
    )
]


if duplicados_indicadores.empty:

    print(
        "OK - La combinación "
        "(numero_ind, formula de calculo) "
        "es única en indicadores."
    )

else:

    print(
        "ERROR - Existen indicadores duplicados."
    )

    print(duplicados_indicadores)


# ------------------------------------------------------------------------------
# Validación 4 - Unicidad de resultados
# ------------------------------------------------------------------------------

clave_resultado = [
    "indicador_id",
    "centro_universitario_id",
    "periodo academico",
    "nivel academico",
    "modalidad",
    "tiempo de reporte",
    "ano",
]


duplicados_resultados = resultados[
    resultados.duplicated(
        subset=clave_resultado,
        keep=False
    )
]


if duplicados_resultados.empty:

    print(
        "OK - La clave de RESULTADOS es única."
    )

else:

    print(
        f"ERROR - Existen {len(duplicados_resultados)} "
        "registros duplicados en RESULTADOS."
    )

    print(duplicados_resultados)


# ------------------------------------------------------------------------------
# Validación 5 - IDs únicos
# ------------------------------------------------------------------------------

if indicadores["indicador_id"].is_unique:

    print("OK - indicador_id es único.")

else:

    print("ERROR - indicador_id contiene duplicados.")


if centros_universitarios[
    "centro_universitario_id"
].is_unique:

    print("OK - centro_universitario_id es único.")

else:

    print(
        "ERROR - centro_universitario_id "
        "contiene duplicados."
    )


if resultados["resultado_id"].is_unique:

    print("OK - resultado_id es único.")

else:

    print("ERROR - resultado_id contiene duplicados.")


# ========================================================================================
#                                   DATASET LIMPIO
# ========================================================================================

columnas_dimensiones = [
    "agrupador",
    "numero_ind",
    "proceso",
    "macroproceso",
    "nombre indicador",
    "formula de calculo",
    "sede - c.u",
    "centro_universitario",
    "localidad",
    "periodo academico",
    "nivel academico",
    "modalidad",
    "tiempo de reporte",
    "responsable",
    "area",
    "correo electronico",
    "tipo de indicador",
    "ano",
]


columnas_hechos = [
    "resultado",
    "analisis cualitativo",
]


df_completo = df[
    columnas_dimensiones + columnas_hechos
]


# ========================================================================================
#                                   OUTPUT
# ========================================================================================

try:

    # --------------------------------------------------------------------------
    # Dataset completo y limpio
    # --------------------------------------------------------------------------

    df_completo.to_excel(
        "data/resultado_final_etl.xlsx",
        index=False
    )


    # --------------------------------------------------------------------------
    # Tabla Indicadores
    # --------------------------------------------------------------------------

    indicadores.to_excel(
        "data/indicadores.xlsx",
        index=False
    )


    # --------------------------------------------------------------------------
    # Tabla Centros Universitarios
    # --------------------------------------------------------------------------

    centros_universitarios.to_excel(
        "data/centros_universitarios.xlsx",
        index=False
    )


    # --------------------------------------------------------------------------
    # Tabla Resultados
    # --------------------------------------------------------------------------

    resultados.to_excel(
        "data/resultados.xlsx",
        index=False
    )


    print("\n")
    print("=" * 80)
    print("                    ETL PROCESADO CON EXITO")
    print("=" * 80)

    print(
        f"Indicadores:            {len(indicadores)}"
    )

    print(
        f"Centros universitarios: {len(centros_universitarios)}"
    )

    print(
        f"Resultados:             {len(resultados)}"
    )

    print(
        f"Dataset completo:       {len(df_completo)}"
    )

    print("=" * 80)


except Exception as e:

    print("\nERROR DURANTE LA EXPORTACION")
    print(e)


# ========================================================================================
#                                   DEBUG
# ========================================================================================

# Descomenta si quieres inspeccionar los DataFrames

# pd.set_option("display.max_columns", None)

# print("\n")
# print("TABLA INDICADORES")
# print(indicadores.head())

# print("\n")
# print("TABLA CENTROS UNIVERSITARIOS")
# print(centros_universitarios.head())

# print("\n")
# print("TABLA RESULTADOS")
# print(resultados.head())

# print("\n")
# print("DATASET COMPLETO")
# print(df_completo.head())