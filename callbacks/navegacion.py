from dash import Input, Output, ctx, html

from app import app

from secciones.resumen import layout_resumen


# ==========================================================================
# NAVEGACIÓN ENTRE SECCIONES
# ==========================================================================

@app.callback(
    Output("seccion-actual", "data"),

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

    if not ctx.triggered_id:
        return "resumen"

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

    return mapa_secciones[ctx.triggered_id]


# ==========================================================================
# CONTENIDO DE LA SECCIÓN
# ==========================================================================

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