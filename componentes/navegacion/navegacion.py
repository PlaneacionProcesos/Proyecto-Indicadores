from dash import html

# ==============================================================================
# CONFIGURACIÓN DE ICONOS DE NAVEGACIÓN (NORMAL Y ACTIVO / SELECCIONADO)
# ==============================================================================
# Define aquí las rutas para el icono por defecto y el icono cuando la sección esté seleccionada:
ICONOS_NAVEGACION = {
    "resumen": {
        "normal": "assets/iconos/resumen_icon.png",        # <- Icono por defecto
        "activo": "assets/iconos/seleccionados/resumen_select_icon.png",       # <- Icono cuando está seleccionado
    },
    "profesores": {
        "normal": "assets/iconos/profesores.png",           # <- Icono por defecto
        "activo": "assets/iconos/seleccionados/profesores_select_icon.png",    # <- Icono cuando está seleccionado
    },
    "aprendizaje_evaluacion": {
        "normal": "assets/iconos/aprendizaje.png",          # <- Icono por defecto
        "activo": "assets/iconos/seleccionados/aprendizaje_select_icon.png",   # <- Icono cuando está seleccionado
    },
    "estudiantes": {
        "normal": "assets/iconos/estudiantes.png",          # <- Icono por defecto
        "activo": "assets/iconos/seleccionados/estudiantes_select_icon.png",   # <- Icono cuando está seleccionado
    },
    "impacto": {
        "normal": "assets/iconos/impacto.png",              # <- Icono por defecto
        "activo": "assets/iconos/seleccionados/impacto_select_icon.png",       # <- Icono cuando está seleccionado
    },
    "investigacion": {
        "normal": "assets/iconos/investigacion.png",        # <- Icono por defecto
        "activo": "assets/iconos/seleccionados/investigacion_select_icon.png", # <- Icono cuando está seleccionado
    },
    "siac": {
        "normal": "assets/iconos/SIAC.png",                 # <- Icono por defecto
        "activo": "assets/iconos/seleccionados/SIAC_select_icon.png",          # <- Icono cuando está seleccionado
    },
    "sostenibilidad": {
        "normal": "assets/iconos/sostenibilidad.png",       # <- Icono por defecto
        "activo": "assets/iconos/seleccionados/sostenibilidad_select_icon.png", # <- Icono cuando está seleccionado
    },
}


def layout_navegacion():
    return html.Div(
        className="navegacion",
        children=[
            html.Button(
                children=[
                    html.Img(id="icono-resumen", src=ICONOS_NAVEGACION["resumen"]["normal"], className="icono-marcador"),
                    html.Span("Resumen"),
                ],
                id="btn-resumen",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(id="icono-profesores", src=ICONOS_NAVEGACION["profesores"]["normal"], className="icono-marcador"),
                    html.Span("Profesores"),
                ],
                id="btn-profesores",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(id="icono-aprendizaje", src=ICONOS_NAVEGACION["aprendizaje_evaluacion"]["normal"], className="icono-marcador"),
                    html.Span("Aprendizaje y Evaluación"),
                ],
                id="btn-aprendizaje-evaluacion",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(id="icono-estudiantes", src=ICONOS_NAVEGACION["estudiantes"]["normal"], className="icono-marcador"),
                    html.Span("Estudiantes"),
                ],
                id="btn-estudiantes",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(id="icono-impacto", src=ICONOS_NAVEGACION["impacto"]["normal"], className="icono-marcador"),
                    html.Span("Impacto"),
                ],
                id="btn-impacto",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(id="icono-investigacion", src=ICONOS_NAVEGACION["investigacion"]["normal"], className="icono-marcador"),
                    html.Span("Investigación"),
                ],
                id="btn-investigacion",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(id="icono-siac", src=ICONOS_NAVEGACION["siac"]["normal"], className="icono-marcador"),
                    html.Span("SIAC"),
                ],
                id="btn-siac",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(id="icono-sostenibilidad", src=ICONOS_NAVEGACION["sostenibilidad"]["normal"], className="icono-marcador"),
                    html.Span("Sostenibilidad"),
                ],
                id="btn-sostenibilidad",
                className="marcador",
                n_clicks=0,
            ),
        ],
    )
