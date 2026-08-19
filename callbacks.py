from dash import Input, Output, ctx, html
from app import app
from secciones.resumen import layout_resumen
from datos import resultados_completos

from funciones import (
    total_registros,
    total_indicadores_estrategicos,
    total_indicadores_sgc,
)

import plotly.express as px


# ========================================================================================
#                                      BOOKMARKS
# ========================================================================================

# @callback(
#     Output("seccion-actual", "data"),

#     Input("btn-resumen", "n_clicks"),
#     Input("btn-calidad", "n_clicks"),
#     Input("btn-procesos", "n_clicks"),
#     Input("btn-sgc", "n_clicks"),
#     Input("btn-objetivos", "n_clicks"),
# )
# def cambiar_seccion(
#     resumen,
#     calidad,
#     procesos,
#     sgc,
#     objetivos
# ):

#     ctx = dash.callback_context

#     if not ctx.triggered:
#         return "resumen"

#     boton = ctx.triggered[0]["prop_id"].split(".")[0]

#     mapa = {
#         "btn-resumen": "resumen",
#         "btn-calidad": "calidad",
#         "btn-procesos": "procesos",
#         "btn-sgc": "sgc",
#         "btn-objetivos": "objetivos",
#     }

#     return mapa[boton]
# # ========================================================================================
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
        "Todos",      # Centro
        "Todos",      # Periodo
        "Todos",      # Nivel
        "Todos",      # Modalidad
        "Todos",      # Tipo
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

        datos_filtrados = datos_filtrados[datos_filtrados["nivel academico"] == nivel]

    # --------------------------------------------------------------------------
    # FILTRO MODALIDAD
    # --------------------------------------------------------------------------

    if modalidad != "Todos":

        datos_filtrados = datos_filtrados[datos_filtrados["modalidad"] == modalidad]

    # --------------------------------------------------------------------------
    # FILTRO TIPO DE INDICADOR
    # --------------------------------------------------------------------------

    if tipo != "Todos":

        datos_filtrados = datos_filtrados[datos_filtrados["tipo de indicador"] == tipo]

    # ==========================================================================
    # KPIs
    # ==========================================================================

    total = total_registros(datos_filtrados)

    estrategicos = total_indicadores_estrategicos(datos_filtrados)

    sgc = total_indicadores_sgc(datos_filtrados)

    # Promedio de resultados
    promedio = datos_filtrados["resultado"].mean()

    # ==========================================================================
    # FORMATEAR
    # ==========================================================================

    kpi_total = f"{total:,}"

    kpi_estrategicos = f"{estrategicos:,}"

    kpi_sgc = f"{sgc:,}"

    kpi_promedio = f"{promedio:,.2f}" if not datos_filtrados.empty else "0"

    # ==========================================================================
    # RETORNAR
    # ==========================================================================

    return (
        kpi_total,
        kpi_estrategicos,
        kpi_sgc,
        kpi_promedio,
    )


# ========================================================================================
#                                      GRÁFICAS
# ========================================================================================


@app.callback(
    Output("grafico-pastel", "figure"),
    Output("grafico-barras", "figure"),
    Output("grafico-linea", "figure"),
    Output("grafico-modalidad", "figure"),

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

        datos_filtrados = datos_filtrados[datos_filtrados["nivel academico"] == nivel]

    # --------------------------------------------------------------------------
    # FILTRO MODALIDAD
    # --------------------------------------------------------------------------

    if modalidad != "Todos":

        datos_filtrados = datos_filtrados[datos_filtrados["modalidad"] == modalidad]

    # --------------------------------------------------------------------------
    # FILTRO TIPO
    # --------------------------------------------------------------------------

    if tipo != "Todos":

        datos_filtrados = datos_filtrados[datos_filtrados["tipo de indicador"] == tipo]

    # ==========================================================================
    # GRÁFICO PASTEL
    # ==========================================================================

    if datos_filtrados.empty:

        grafico_pastel = px.pie(title="No hay datos para los filtros seleccionados")

    else:

        datos_pastel = datos_filtrados.groupby("modalidad", as_index=False)[
            "resultado"
        ].sum()

        grafico_pastel = px.pie(
            datos_pastel,
            names="modalidad",
            values="resultado",
            title="Distribución de resultados por modalidad",
        )

    grafico_pastel.update_layout(
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

    # ==========================================================================
    # GRÁFICO DE BARRAS
    # ==========================================================================

    if datos_filtrados.empty:

        grafico_barras = px.bar(title="No hay datos para los filtros seleccionados")

    else:

        datos_barras = (
            datos_filtrados.groupby("agrupador")["indicador_id"]
            .nunique()
            .reset_index(name="cantidad_indicadores")
        )

        grafico_barras = px.bar(
            datos_barras,
            x="cantidad_indicadores",
            y="agrupador",
            orientation="h",
            title="Indicadores por agrupador",
            text="cantidad_indicadores",
            color="agrupador",
        )

    grafico_barras.update_layout(
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

    # ==========================================================================
    # GRÁFICA 3
    # REGISTROS HISTÓRICOS POR AÑO
    # ==========================================================================

    if datos_filtrados.empty:

        grafico_linea = px.line(
            title="No hay datos para los filtros seleccionados"
        )

    else:

        datos_registros = (
            datos_filtrados
            .groupby("ano")
            .size()
            .reset_index(name="total_registros")
            .sort_values("ano")
        )

        grafico_linea = px.line(
            datos_registros,
            x="ano",
            y="total_registros",
            markers=True,
            title="Registros históricos por año",
        )


    grafico_linea.update_layout(
        font=dict(
            family="Arial",
            color="#080b0d",
        ),

        paper_bgcolor="white",
        plot_bgcolor="white",

        xaxis_title="Año",
        yaxis_title="Total de registros",

        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30,
        ),
    )


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
            datos_filtrados
            .dropna(subset=["modalidad", "resultado"])
            .groupby("modalidad", as_index=False)["resultado"]
            .mean()
            .sort_values("resultado", ascending=False)
        )

        grafico_modalidad = px.bar(
            datos_modalidad,
            x="modalidad",
            y="resultado",
            title="Promedio de resultados por modalidad",
            text_auto=".2f",
            color="modalidad",
        )


    grafico_modalidad.update_layout(
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
        grafico_linea,
        grafico_modalidad
    )



# ========================================================================================
# NAVEGACIÓN ENTRE SECCIONES
# ========================================================================================

@app.callback(
    Output("seccion-actual", "data"),

    Output("btn-resumen", "className"),
    Output("btn-profesores", "className"),
    Output("btn-aprendizaje-evaluacion", "className"),
    Output("btn-estudiantes", "className"),
    Output("btn-impacto", "className"),
    Output("btn-investigacion", "className"),
    Output("btn-siac", "className"),
    Output("btn-sostenibilidad", "className"),

    Input("btn-resumen", "n_clicks"),
    Input("btn-profesores", "n_clicks"),
    Input("btn-aprendizaje-evaluacion", "n_clicks"),
    Input("btn-estudiantes", "n_clicks"),
    Input("btn-impacto", "n_clicks"),
    Input("btn-investigacion", "n_clicks"),
    Input("btn-siac", "n_clicks"),
    Input("btn-sostenibilidad", "n_clicks"),
)
def cambiar_seccion(
    resumen,
    profesores,
    aprendizaje_evaluacion,
    estudiantes,
    impacto,
    investigacion,
    siac,
    sostenibilidad,
):

    mapa_secciones = {
        "btn-resumen": "resumen",
        "btn-profesores": "profesores",
        "btn-aprendizaje-evaluacion": "aprendizaje-evaluacion",
        "btn-estudiantes": "estudiantes",
        "btn-impacto": "impacto",
        "btn-investigacion": "investigacion",
        "btn-siac": "siac",
        "btn-sostenibilidad": "sostenibilidad",
    }

    if not ctx.triggered_id:
        seccion = "resumen"
    else:
        seccion = mapa_secciones[ctx.triggered_id]

    clases = []

    for boton, nombre_seccion in mapa_secciones.items():

        if nombre_seccion == seccion:
            clases.append("marcador activo")
        else:
            clases.append("marcador")

    return (
        seccion,
        *clases,
    )

# ========================================================================================
# CONTENIDO DE LA SECCIÓN
# ========================================================================================

@app.callback(
    Output("contenido-seccion", "children"),
    Input("seccion-actual", "data"),
)
def mostrar_seccion(seccion):

    if seccion == "resumen":
        return layout_resumen()

    return html.Div(
        className="seccion-en-construccion",
        children=[
            html.H2(
                seccion.replace("-", " ").title()
            ),
            html.P(
                "Esta sección se encuentra en construcción."
            ),
        ],
    )