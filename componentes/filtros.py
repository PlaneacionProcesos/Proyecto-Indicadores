from dash import Input, Output, ctx, dcc, html
from datos import resultados_completos

# ========================================================================================
# MAPA DE SECCIONES A AGRUPADORES
# ========================================================================================

MAPA_SECCION_AGRUPADOR = {
    "resumen": None,
    "estudiantes": "Estudiantes",
    "profesores": "Profesores",
    "aprendizaje_evaluacion": "Aprendizaje y Evaluacion",
    "investigacion": "Investigacion",
    "impacto": "Impacto",
    "sostenibilidad": "Sostenibilidad",
    "siac": "SIAC - Rendicion de Cuentas",
}


# ========================================================================================
# FUNCIÓN GENERADORA DE OPCIONES POR AGRUPADOR
# ========================================================================================

def obtener_opciones_filtros(agrupador=None):
    """
    Genera las opciones exactas y disponibles para cada dropdown
    según el agrupador (o el total si agrupador es None).
    """
    if agrupador is None:
        df = resultados_completos
    else:
        df = resultados_completos[resultados_completos["agrupador"] == agrupador]

    # Año
    anos = sorted([int(y) for y in df["ano"].dropna().unique()], reverse=True)
    opt_ano = [{"label": "Histórico", "value": "Historico"}] + [
        {"label": str(y), "value": str(y)} for y in anos
    ]

    # Centros
    centros = sorted([c for c in df["centro_universitario"].dropna().unique() if c != "Todos"])
    opt_centro = [{"label": "Todos", "value": "Todos"}] + [
        {"label": c, "value": c} for c in centros
    ]

    # Periodos
    periodos = sorted([p for p in df["periodo academico"].dropna().unique() if p != "Todos"])
    opt_periodo = [{"label": "Todos", "value": "Todos"}] + [
        {"label": p, "value": p} for p in periodos
    ]

    # Niveles
    niveles = sorted([n for n in df["nivel academico"].dropna().unique() if n != "Todos"])
    opt_nivel = [{"label": "Todos", "value": "Todos"}] + [
        {"label": n, "value": n} for n in niveles
    ]

    # Modalidades
    modalidades = sorted([m for m in df["modalidad"].dropna().unique() if m != "Todos"])
    opt_modalidad = [{"label": "Todas", "value": "Todos"}] + [
        {"label": m, "value": m} for m in modalidades
    ]

    # Tipos
    tipos = sorted([t for t in df["tipo de indicador"].dropna().unique() if t != "Todos"])
    opt_tipo = [{"label": "Todos", "value": "Todos"}] + [
        {"label": t, "value": t} for t in tipos
    ]

    # Tiempos de Reporte
    tiempos = sorted([
        str(t)
        for t in df["tiempo de reporte"].dropna().astype(str).unique()
        if str(t) != "Todos"
    ])
    opt_tiempo = [{"label": "Todos", "value": "Todos"}] + [
        {"label": t, "value": t} for t in tiempos
    ]

    return (
        opt_ano,
        opt_centro,
        opt_periodo,
        opt_nivel,
        opt_modalidad,
        opt_tipo,
        opt_tiempo,
    )


# Opciones iniciales por defecto (Resumen / General)
(
    _opt_ano_def,
    _opt_centro_def,
    _opt_periodo_def,
    _opt_nivel_def,
    _opt_modalidad_def,
    _opt_tipo_def,
    _opt_tiempo_def,
) = obtener_opciones_filtros(None)


def layout_filtros():

    return html.Div(
        className="contenedor-filtros",
        id="contenedor-filtros",

        children=[

            # ======================================================================
            # BOTÓN / PESTAÑA DE FILTROS
            # ======================================================================

            html.Button(
                "◀",
                id="btn-toggle-filtros",
                n_clicks=0,
                className="btn-toggle-filtros",
            ),

            # ======================================================================
            # PANEL DE FILTROS
            # ======================================================================

            html.Div(
                className="segmentadores",
                id="segmentadores",

                children=[

                    html.H3("Filtros"),

                    # ------------------------------------------------------------------
                    # AÑO
                    # ------------------------------------------------------------------

                    html.Label("Año"),

                    dcc.Dropdown(
                        id="filtro-año",
                        options=_opt_ano_def,
                        value="Historico",
                        clearable=False,
                    ),

                    html.Br(),

                    # ------------------------------------------------------------------
                    # CENTRO UNIVERSITARIO
                    # ------------------------------------------------------------------

                    html.Label(
                        "Centro Universitario"
                    ),

                    dcc.Dropdown(
                        id="filtro-centro",
                        options=_opt_centro_def,
                        value="Todos",
                        clearable=False,
                        searchable=True,
                    ),

                    html.Br(),

                    # ------------------------------------------------------------------
                    # PERIODO ACADÉMICO
                    # ------------------------------------------------------------------

                    html.Label(
                        "Periodo Académico"
                    ),

                    dcc.Dropdown(
                        id="filtro-periodo",
                        options=_opt_periodo_def,
                        value="Todos",
                        clearable=False,
                        searchable=True,
                    ),

                    html.Br(),

                    # ------------------------------------------------------------------
                    # NIVEL ACADÉMICO
                    # ------------------------------------------------------------------

                    html.Label(
                        "Nivel Académico"
                    ),

                    dcc.Dropdown(
                        id="filtro-nivel",
                        options=_opt_nivel_def,
                        value="Todos",
                        clearable=False,
                    ),

                    html.Br(),

                    # ------------------------------------------------------------------
                    # MODALIDAD
                    # ------------------------------------------------------------------

                    html.Label(
                        "Modalidad"
                    ),

                    dcc.Dropdown(
                        id="filtro-modalidad",
                        options=_opt_modalidad_def,
                        value="Todos",
                        clearable=False,
                    ),

                    html.Br(),

                    # ------------------------------------------------------------------
                    # TIPO DE INDICADOR
                    # ------------------------------------------------------------------

                    html.Label(
                        "Tipo de Indicador"
                    ),

                    dcc.Dropdown(
                        id="filtro-tipo",
                        options=_opt_tipo_def,
                        value="Todos",
                        clearable=False,
                    ),

                    html.Br(),

                    # ------------------------------------------------------------------
                    # TIEMPO DE REPORTE
                    # ------------------------------------------------------------------

                    html.Label(
                        "Tiempo de Reporte"
                    ),

                    dcc.Dropdown(
                        id="filtro-tiempo-reporte",
                        options=_opt_tiempo_def,
                        value="Todos",
                        clearable=False,
                        searchable=True,
                    ),

                    html.Br(),

                    # ------------------------------------------------------------------
                    # BOTÓN BORRAR FILTROS
                    # ------------------------------------------------------------------

                    html.Button(
                        "Borrar filtros",
                        id="btn-borrar-filtros",
                        n_clicks=0,
                        className="btn-borrar-filtros",
                    ),
                ],
            ),
        ],
    )


# ========================================================================================
# CALLBACKS DE DINÁMICA DE FILTROS POR SECCIÓN
# ========================================================================================

def registrar_callbacks_filtros(app):
    @app.callback(
        Output("filtro-año", "options"),
        Output("filtro-año", "value"),
        Output("filtro-centro", "options"),
        Output("filtro-centro", "value"),
        Output("filtro-periodo", "options"),
        Output("filtro-periodo", "value"),
        Output("filtro-nivel", "options"),
        Output("filtro-nivel", "value"),
        Output("filtro-modalidad", "options"),
        Output("filtro-modalidad", "value"),
        Output("filtro-tipo", "options"),
        Output("filtro-tipo", "value"),
        Output("filtro-tiempo-reporte", "options"),
        Output("filtro-tiempo-reporte", "value"),
        Input("seccion-actual", "data"),
        Input("btn-borrar-filtros", "n_clicks"),
    )
    def actualizar_filtros_por_seccion(seccion, n_clicks):
        if not seccion:
            seccion = "resumen"

        agrupador = MAPA_SECCION_AGRUPADOR.get(seccion)
        (
            opt_ano,
            opt_centro,
            opt_periodo,
            opt_nivel,
            opt_modalidad,
            opt_tipo,
            opt_tiempo,
        ) = obtener_opciones_filtros(agrupador)

        return (
            opt_ano,
            "Historico",
            opt_centro,
            "Todos",
            opt_periodo,
            "Todos",
            opt_nivel,
            "Todos",
            opt_modalidad,
            "Todos",
            opt_tipo,
            "Todos",
            opt_tiempo,
            "Todos",
        )