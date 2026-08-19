from dash import dcc, html
from datos import resultados_completos

# ========================================================================================
#                              OPCIONES DE FILTROS
# ========================================================================================

# ------------------------------------------------------------------------------
# Centros Universitarios
# ------------------------------------------------------------------------------

opciones_centros = [
    {
        "label": centro,
        "value": centro,
    }
    for centro in sorted(
        resultados_completos["centro_universitario"]
        .dropna()
        .unique()
    )
]


# ------------------------------------------------------------------------------
# Periodos Académicos
# ------------------------------------------------------------------------------

opciones_periodos = [
    {
        "label": periodo,
        "value": periodo,
    }
    for periodo in sorted(
        resultados_completos["periodo academico"]
        .dropna()
        .unique()
    )
]


# ------------------------------------------------------------------------------
# Niveles Académicos
# ------------------------------------------------------------------------------

opciones_niveles = [
    {
        "label": nivel,
        "value": nivel,
    }
    for nivel in sorted(
        resultados_completos["nivel academico"]
        .dropna()
        .unique()
    )
]


# ------------------------------------------------------------------------------
# Modalidades
# ------------------------------------------------------------------------------

opciones_modalidades = [
    {
        "label": modalidad,
        "value": modalidad,
    }
    for modalidad in sorted(
        resultados_completos["modalidad"]
        .dropna()
        .unique()
    )
]


# ------------------------------------------------------------------------------
# Tipos de Indicador
# ------------------------------------------------------------------------------

opciones_tipos = [
    {
        "label": tipo,
        "value": tipo,
    }
    for tipo in sorted(
        resultados_completos["tipo de indicador"]
        .dropna()
        .unique()
    )
]

def layout_filtros():
    return(
        html.Div(
            className="segmentadores",
            children=[

                html.H3("Filtros"),


                # ------------------------------------------------------------------
                # AÑO
                # ------------------------------------------------------------------

                html.Label("Año"),

                dcc.Dropdown(
                    id="filtro-año",

                    options=[
                        {
                            "label": "Histórico",
                            "value": "Historico",
                        },
                        {
                            "label": "2026",
                            "value": "2026",
                        },
                        {
                            "label": "2025",
                            "value": "2025",
                        },
                        {
                            "label": "2024",
                            "value": "2024",
                        },
                    ],

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

                    options=[
                        {
                            "label": "Todos",
                            "value": "Todos",
                        },
                        *opciones_centros,
                    ],

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

                    options=[
                        {
                            "label": "Todos",
                            "value": "Todos",
                        },
                        *opciones_periodos,
                    ],

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

                    options=[
                        {
                            "label": "Todos",
                            "value": "Todos",
                        },
                        *opciones_niveles,
                    ],

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

                    options=[
                        {
                            "label": "Todas",
                            "value": "Todos",
                        },
                        *opciones_modalidades,
                    ],

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

                    options=[
                        {
                            "label": "Todos",
                            "value": "Todos",
                        },
                        *opciones_tipos,
                    ],

                    value="Todos",
                    clearable=False,
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
        )
    )