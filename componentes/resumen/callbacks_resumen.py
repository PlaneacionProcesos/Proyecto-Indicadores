from dash import Input, Output, html
from dash.exceptions import PreventUpdate
from datos import resultados_completos
from configuraciones.agrupadores import DESCRIPCIONES_AGRUPADORES
import pandas as pd
import plotly.express as px


def registrar_callbacks_resumen(app):

    # ========================================================================================
    #                                      KPIs
    # ========================================================================================
    @app.callback(
        Output("filtro-año", "value"),
        Output("filtro-centro", "value"),
        Output("filtro-periodo", "value"),
        Output("filtro-nivel", "value"),
        Output("filtro-modalidad", "value"),
        Output("filtro-tipo", "value"),
        Input("btn-borrar-filtros", "n_clicks"),
        prevent_initial_call=True,
    )
    def borrar_filtros(n_clicks):

        return (
            "Historico",  # Año
            "Todos",  # Centro
            "Todos",  # Periodo
            "Todos",  # Nivel
            "Todos",  # Modalidad
            "Todos",  # Tipo
        )

    @app.callback(
        Output("kpi-it", "children"),
        Output("kpi-ies", "children"),
        Output("kpi-its", "children"),
        Output("kpi-maximos", "children"),
        Input("filtro-año", "value"),
        Input("filtro-centro", "value"),
        Input("filtro-periodo", "value"),
        Input("filtro-nivel", "value"),
        Input("filtro-modalidad", "value"),
        Input("filtro-tipo", "value"),
    )
    def actualizar_kpis(
        año,
        centro,
        periodo,
        nivel,
        modalidad,
        tipo,
    ):
        # --------------------------------------------------------------------------
        # Validar filtro
        # --------------------------------------------------------------------------

        if año is None:
            return (
                "Selecciona un valor",
                "Selecciona un valor",
                "Selecciona un valor",
                "Selecciona un valor",
            )

        # --------------------------------------------------------------------------
        # Copiar datos históricos
        # --------------------------------------------------------------------------

        datos_filtrados = resultados_completos.copy()

        # --------------------------------------------------------------------------
        # FILTRO AÑO
        # --------------------------------------------------------------------------

        if año != "Historico":

            datos_filtrados = datos_filtrados[datos_filtrados["ano"] == int(año)]

        # --------------------------------------------------------------------------
        # FILTRO CENTRO UNIVERSITARIO
        # --------------------------------------------------------------------------

        if centro != "Todos":

            datos_filtrados = datos_filtrados[
                datos_filtrados["centro_universitario"] == centro
            ]

        # --------------------------------------------------------------------------
        # FILTRO PERIODO ACADÉMICO
        # --------------------------------------------------------------------------

        if periodo != "Todos":

            datos_filtrados = datos_filtrados[
                datos_filtrados["periodo academico"] == periodo
            ]

        # --------------------------------------------------------------------------
        # FILTRO NIVEL ACADÉMICO
        # --------------------------------------------------------------------------

        if nivel != "Todos":

            datos_filtrados = datos_filtrados[
                datos_filtrados["nivel academico"] == nivel
            ]

        # --------------------------------------------------------------------------
        # FILTRO MODALIDAD
        # --------------------------------------------------------------------------

        if modalidad != "Todos":

            datos_filtrados = datos_filtrados[datos_filtrados["modalidad"] == modalidad]

        # --------------------------------------------------------------------------
        # FILTRO TIPO DE INDICADOR
        # --------------------------------------------------------------------------

        if tipo != "Todos":

            datos_filtrados = datos_filtrados[
                datos_filtrados["tipo de indicador"] == tipo
            ]

        # ==========================================================================
        # KPIs
        # ==========================================================================

        def total_registros(df):
            return df["numero_ind"].nunique()

        def total_indicadores_estrategicos(df):

            return df[df["tipo de indicador"] == "Estrategico"]["numero_ind"].nunique()

        def total_indicadores_sgc(df):

            return df[df["tipo de indicador"] == "SGC"]["numero_ind"].nunique()

        total = total_registros(datos_filtrados)

        estrategicos = total_indicadores_estrategicos(datos_filtrados)

        sgc = total_indicadores_sgc(datos_filtrados)

        # Promedio de resultados
        en_contruccion = "--"

        # ==========================================================================
        # FORMATEAR
        # ==========================================================================

        kpi_total = f"{total:,}"

        kpi_estrategicos = f"{estrategicos:,}"

        kpi_sgc = f"{sgc:,}"

        # ==========================================================================
        # RETORNAR
        # ==========================================================================

        return (
            kpi_total,
            kpi_estrategicos,
            kpi_sgc,
            en_contruccion,
        )

    # ========================================================================================
    #                                      GRÁFICAS
    # ========================================================================================

    @app.callback(
        Output("grafico-pastel", "figure"),
        Output("grafico-barras", "figure"),
        Output("grafico-modalidad", "figure"),
        Output("tabla-agrupadores", "data"),
        Input("filtro-año", "value"),
        Input("filtro-centro", "value"),
        Input("filtro-periodo", "value"),
        Input("filtro-nivel", "value"),
        Input("filtro-modalidad", "value"),
        Input("filtro-tipo", "value"),
    )
    def actualizar_graficas(
        año,
        centro,
        periodo,
        nivel,
        modalidad,
        tipo,
    ):
        # --------------------------------------------------------------------------
        # Copiar datos
        # --------------------------------------------------------------------------

        datos_filtrados = resultados_completos.copy()

        # --------------------------------------------------------------------------
        # FILTRO AÑO
        # --------------------------------------------------------------------------

        if año != "Historico":

            datos_filtrados = datos_filtrados[datos_filtrados["ano"] == int(año)]

        # --------------------------------------------------------------------------
        # FILTRO CENTRO
        # --------------------------------------------------------------------------

        if centro != "Todos":

            datos_filtrados = datos_filtrados[
                datos_filtrados["centro_universitario"] == centro
            ]

        # --------------------------------------------------------------------------
        # FILTRO PERIODO
        # --------------------------------------------------------------------------

        if periodo != "Todos":

            datos_filtrados = datos_filtrados[
                datos_filtrados["periodo academico"] == periodo
            ]

        # --------------------------------------------------------------------------
        # FILTRO NIVEL
        # --------------------------------------------------------------------------

        if nivel != "Todos":

            datos_filtrados = datos_filtrados[
                datos_filtrados["nivel academico"] == nivel
            ]

        # --------------------------------------------------------------------------
        # FILTRO MODALIDAD
        # --------------------------------------------------------------------------

        if modalidad != "Todos":

            datos_filtrados = datos_filtrados[datos_filtrados["modalidad"] == modalidad]

        # --------------------------------------------------------------------------
        # FILTRO TIPO
        # --------------------------------------------------------------------------

        if tipo != "Todos":

            datos_filtrados = datos_filtrados[
                datos_filtrados["tipo de indicador"] == tipo
            ]

        # ==========================================================================
        # GRÁFICO PASTEL
        # ==========================================================================

        if datos_filtrados.empty:

            grafico_pastel = px.pie(title="No hay datos para los filtros seleccionados")

        else:

            datos_pastel = datos_filtrados.groupby("modalidad", as_index=False)[
                "resultado"
            ].sum()

        colores_modalidad = {
            "Presencial": "#053074",
            "Virtual": "#36A2EB",
            "Distancia": "#FED103",
            "No Aplica": "#AEAEAE",
        }

        grafico_pastel = px.pie(
            datos_pastel,
            names="modalidad",
            values="resultado",
            title="Distribución de resultados por modalidad",
            color="modalidad",
            color_discrete_map=colores_modalidad,
        )

        grafico_pastel.update_layout(
            title=dict(
                text="Distribución de resultados por modalidad",
                x=0.5,
                xanchor="center",
                font=dict(
                    family="Arial",
                    size=18,
                    color="#080b0d",
                ),
            ),
            font=dict(
                family="Arial",
                color="#080b0d",
            ),
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(
                l=30,
                r=30,
                t=60,
                b=30,
            ),
        )

        grafico_pastel.update_traces(
            textfont=dict(
                color="black",
                size=14,
            )
        )

        # ==========================================================================
        # GRÁFICO DE BARRAS APILADAS - INDICADOR X MARCROPROCESO
        # ==========================================================================

        COLORES_MACROPROCESO = {
            "Aseguramiento de la Calidad Academica": "#0B3D91",
            "Bienestar Institucional e Identidad Misional": "#145DA0",
            "Calidad Integral": "#1E6FBA",
            "Desarrollo Integral del Talento Humano": "#2878C8",
            "Direccionamiento Estrategico": "#328CC1",
            "Docencia": "#3FA7D6",
            "Gestion Administrativa y Financiera": "#5AA9E6",
            "Gestion de la Infraestructura Fisica y Tecnologica": "#74B9E8",
            "Gestion de la Planeacion y Control": "#8CC8ED",
            "Gestion de Mercadeo y Posicionamiento": "#A7D5F2",
            "Gestion Juridica": "#C2E2F5",
            "Investigacion": "#D6ECF8",
            "Proyeccion Social": "#E8F5FB",
            "Relaciones Interinstitucionales": "#F5FBFE",
        }

        if datos_filtrados.empty:

            grafico_barras = px.bar(title="No hay datos para los filtros seleccionados")

        else:

            datos_barras = (
                datos_filtrados.groupby("macroproceso")["numero_ind"]
                .nunique()
                .reset_index(name="cantidad_indicadores")
                .sort_values("cantidad_indicadores", ascending=False)
            )

            grafico_barras = px.bar(
                datos_barras,
                x="cantidad_indicadores",
                y="macroproceso",
                orientation="h",
                title="Indicadores por agrupador",
                color="macroproceso",
                color_discrete_map=COLORES_MACROPROCESO,
                category_orders={"macroproceso": datos_barras["macroproceso"].tolist()},
            )

            # ========================================================================
            # ESTILO
            # ========================================================================

            grafico_barras.update_layout(
                title=dict(
                    x=0.5,
                    xanchor="center",
                    font=dict(
                        family="Arial",
                        size=18,
                        color="#080b0d",
                    ),
                ),
                font=dict(
                    family="Arial",
                    color="#080b0d",
                ),
                paper_bgcolor="white",
                plot_bgcolor="white",
                margin=dict(
                    l=30,
                    r=30,
                    t=60,
                    b=30,
                ),
                showlegend=False,
            )

            # ========================================================================
            # EJES
            # ========================================================================

            grafico_barras.update_xaxes(
                title=None,
                showgrid=True,
                gridcolor="#eef1f4",
                zeroline=False,
            )

            grafico_barras.update_yaxes(
                title=None,
                showgrid=False,
                zeroline=False,
                autorange="reversed",
            )

        # ==========================================================================
        # TABLA DE AGRUPADORES
        # ==========================================================================

        if datos_filtrados.empty:

            datos_tabla = pd.DataFrame(
                columns=[
                    "agrupador",
                    "descripcion",
                    "total_indicadores",
                ]
            )

        else:

            datos_tabla = (
                datos_filtrados.groupby("agrupador")["numero_ind"]
                .nunique()
                .reset_index(name="total_indicadores")
            )

            datos_tabla["descripcion"] = (
                datos_tabla["agrupador"]
                .map(DESCRIPCIONES_AGRUPADORES)
                .fillna("Sin descripción disponible.")
            )

            datos_tabla = datos_tabla[
                [
                    "agrupador",
                    "descripcion",
                    "total_indicadores",
                ]
            ]

        # ==========================================================================
        # GRÁFICA 4
        # PROMEDIO POR MODALIDAD
        # ==========================================================================

        if datos_filtrados.empty:

            grafico_modalidad = px.bar(
                title="No hay datos para los filtros seleccionados"
            )

        else:

            datos_modalidad = (
                datos_filtrados.dropna(subset=["modalidad", "resultado"])
                .groupby("modalidad", as_index=False)["resultado"]
                .mean()
                .sort_values("resultado", ascending=False)
            )

            colores_modalidad = {
                "Presencial": "#053074",
                "Distancia": "#FED103",
                "No Aplica": "#AEAEAE",
            }

            grafico_modalidad = px.bar(
                datos_modalidad,
                x="modalidad",
                y="resultado",
                title="Promedio de resultados por modalidad",
                text_auto=".2f",
                color="modalidad",
                color_discrete_map=colores_modalidad,
            )

            grafico_modalidad.update_traces(textposition="outside")

            grafico_modalidad.update_yaxes(visible=False)

            grafico_modalidad.update_layout(
                title=dict(
                    x=0.5,
                    xanchor="center",
                    font=dict(
                        family="Arial",
                        size=18,
                        color="#080b0d",
                    ),
                ),
                font=dict(
                    family="Arial",
                    color="#080b0d",
                ),
                paper_bgcolor="white",
                plot_bgcolor="white",
                xaxis_title="Modalidad",
                yaxis_title="Promedio de resultado",
                margin=dict(
                    l=30,
                    r=30,
                    t=60,
                    b=30,
                ),
            )

        # ==========================================================================
        # RETORNAR GRÁFICAS
        # ==========================================================================

        return (
            grafico_pastel,
            grafico_barras,
            grafico_modalidad,
            datos_tabla.to_dict("records"),
        )
