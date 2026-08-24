from dash import Input, Output, html
from datos import resultados_completos
import pandas as pd

def registrar_callback_aprendizaje(app):

    @app.callback(
        Output("tabla-aprendizaje", "data"),
        Input("filtro-año", "value"),
        Input("filtro-centro", "value"),
        Input("filtro-periodo", "value"),
        Input("filtro-nivel", "value"),
        Input("filtro-modalidad", "value"),
        Input("filtro-tipo", "value"),
    )
    def datos_tabla(año, centro, periodo, nivel, modalidad, tipo):

        # --------------------------------------------------------------------------
        # 1. Copiar datos
        # --------------------------------------------------------------------------
        datos_filtrados = resultados_completos.copy()

        # --------------------------------------------------------------------------
        # 2. Aplicar Filtros
        # --------------------------------------------------------------------------
        if año is not None and año != "Historico":
            datos_filtrados = datos_filtrados[datos_filtrados["ano"] == int(año)]

        if centro != "Todos":
            datos_filtrados = datos_filtrados[datos_filtrados["centro_universitario"] == centro]

        if periodo != "Todos":
            datos_filtrados = datos_filtrados[datos_filtrados["periodo academico"] == periodo]

        if nivel != "Todos":
            datos_filtrados = datos_filtrados[datos_filtrados["nivel academico"] == nivel]

        if modalidad != "Todos":
            datos_filtrados = datos_filtrados[datos_filtrados["modalidad"] == modalidad]

        if tipo != "Todos":
            datos_filtrados = datos_filtrados[datos_filtrados["tipo de indicador"] == tipo]

        # --------------------------------------------------------------------------
        # 3. Procesar datos para la tabla
        # --------------------------------------------------------------------------
        if datos_filtrados.empty:
            df_resultado = pd.DataFrame(
                columns=[
                    "agrupador",
                    "descripcion",
                    "total_indicadores",
                ]
            )
        else:
            df_resultado = (
                datos_filtrados.groupby("agrupador")["indicador_id"]
                .nunique()
                .reset_index(name="total_indicadores")
            )

            df_resultado["descripcion"] = (
                df_resultado["agrupador"]
                .fillna("Sin descripción disponible.")
            )

            df_resultado = df_resultado[
                [
                    "agrupador",
                    "descripcion",
                    "total_indicadores",
                ]
            ]

        # 4. Retornar los registros en formato diccionario para la DataTable
        return df_resultado.to_dict("records")