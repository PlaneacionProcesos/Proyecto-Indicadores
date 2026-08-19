from dash import Dash, dcc, html

from datos import resultados_completos


app = Dash(__name__)


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


# ========================================================================================
#                                      LAYOUT
# ========================================================================================

app.layout = html.Div(
    [

        # ==================================================================================
        # HEADER
        # ==================================================================================

        html.Div(
            className="header",
            children=[

                html.Img(
                    className="logo",
                    src="assets/Logo_Unificado.png"
                    ),

                html.Div(
                    className="titulo",
                    children=[
                        html.H1("Indicadores Generales"),
                        html.Span(
                            "Indicadores estratégicos y del SGC que permiten hacer seguimiento al cumplimiento de los procesos y al logro de los objetivos institucionales."
                        )
                    ]
                ),

                html.Div(
                    className="fecha-actualizacion",
                    children=[
                        html.Span(
                            "Fecha de actualización"
                        ),
                        html.Strong(
                            "18 de agosto de 2026"
                        ),
                    ],
                ),

            ],
        ),

        # ==================================================================================
        # NAVEGACION
        # ==================================================================================

        html.Div(
            className="navegacion",
            children=[

                html.Button(
                    "Resumen",
                    id="btn-resumen",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Profesores",
                    id="btn-profesores",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Aprendizaje y Evaluación",
                    id="btn-aprendizaje-evaluacion",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Estudiantes",
                    id="btn-estudiantes",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Impacto",
                    id="btn-impacto",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Investigación",
                    id="btn-investigacion",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "SIAC",
                    id="btn-siac",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Sostenibilidad",
                    id="btn-sostenibilidad",
                    className="marcador",
                    n_clicks=0
                ),

            ],
        ),

        dcc.Store(
            id="seccion-actual",
            data="resumen"
        ),


        # ==================================================================================
        # CONTENEDOR PRINCIPAL
        # ==================================================================================

        html.Div(
            className="contenedor",
            children=[


                # ==========================================================================
                # FILTROS
                # ==========================================================================

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
                ),


                # ==========================================================================
                # DASHBOARD
                # ==========================================================================

                html.Div(
                    className="graficas",
                    children=[


                        # ==================================================================
                        # TARJETAS
                        # ==================================================================

                        html.Div(
                            className="tarjetas",


                            children=[


                                # ----------------------------------------------------------
                                # KPI 1
                                # ----------------------------------------------------------

                                html.Div(
                                    className="tarjeta",

                                    id="tarjeta1",

                                    children=[

                                        html.P(
                                            "Registros Históricos"
                                        ),

                                        html.H2(
                                            id="kpi-it"
                                        ),

                                    ],
                                ),


                                # ----------------------------------------------------------
                                # KPI 2
                                # ----------------------------------------------------------

                                html.Div(
                                    className="tarjeta",

                                    id="tarjeta2",

                                    children=[

                                        html.P(
                                            "Indicadores Estratégicos"
                                        ),

                                        html.H2(
                                            id="kpi-ies"
                                        ),

                                    ],
                                ),


                                # ----------------------------------------------------------
                                # KPI 3
                                # ----------------------------------------------------------

                                html.Div(
                                    className="tarjeta",

                                    id="tarjeta3",

                                    children=[

                                        html.P(
                                            "Indicadores del SGC"
                                        ),

                                        html.H2(
                                            id="kpi-its"
                                        ),

                                    ],
                                ),


                                # ----------------------------------------------------------
                                # KPI 4
                                # ----------------------------------------------------------

                                html.Div(
                                    className="tarjeta",

                                    id="tarjeta4",

                                    children=[

                                        html.P(
                                            "Promedio de Resultados"
                                        ),

                                        html.H2(
                                            id="kpi-maximos"
                                        ),

                                    ],
                                ),

                            ],
                        ),


                        # ==================================================================
                        # VISUALIZACIONES
                        # ==================================================================

                        html.Div(
                            className="visualizaciones",

                            children=[


                                # ----------------------------------------------------------
                                # GRÁFICO PASTEL
                                # ----------------------------------------------------------

                                html.Div(
                                    className="pastel",

                                    children=[
                                        dcc.Graph(
                                            id="grafico-pastel"
                                        )
                                    ],
                                ),


                                # ----------------------------------------------------------
                                # GRÁFICO BARRAS
                                # ----------------------------------------------------------

                                html.Div(
                                    className="barras",

                                    children=[
                                        dcc.Graph(
                                            id="grafico-barras"
                                        )
                                    ],
                                ),

                                # ----------------------------------------------------------
                                # GRÁFICO 3
                                # ----------------------------------------------------------

                                html.Div(
                                    className="grafico-3",

                                    children=[
                                        dcc.Graph(
                                            id="grafico-3"
                                        )
                                    ],
                                ),

                                # ----------------------------------------------------------
                                # GRÁFICO 4
                                # ----------------------------------------------------------

                                html.Div(
                                    className="grafico-4",

                                    children=[
                                        dcc.Graph(
                                            id="grafico-modalidad"
                                        )
                                    ],
                                ),


                                # ----------------------------------------------------------
                                # GRÁFICO 5
                                # ----------------------------------------------------------

                                html.Div(
                                    className="grafico-5",

                                    children=[
                                        dcc.Graph(
                                            id="grafico-linea"
                                        )
                                    ],
                                ),

                    

                            ],
                        ),

                    ],
                ),

            ],
        ),

    ]
)


# ========================================================================================
#                                      CALLBACKS
# ========================================================================================

from callbacks import *


# ========================================================================================
#                                      EJECUCIÓN
# ========================================================================================

if __name__ == "__main__":
    app.run(debug=True)