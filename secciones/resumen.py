from dash import dcc, html


def layout_resumen():

    return (
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
                                html.P("Registros Históricos"),
                                html.H2(id="kpi-it"),
                            ],
                        ),
                        # ----------------------------------------------------------
                        # KPI 2
                        # ----------------------------------------------------------
                        html.Div(
                            className="tarjeta",
                            id="tarjeta2",
                            children=[
                                html.P("Indicadores Estratégicos"),
                                html.H2(id="kpi-ies"),
                            ],
                        ),
                        # ----------------------------------------------------------
                        # KPI 3
                        # ----------------------------------------------------------
                        html.Div(
                            className="tarjeta",
                            id="tarjeta3",
                            children=[
                                html.P("Indicadores del SGC"),
                                html.H2(id="kpi-its"),
                            ],
                        ),
                        # ----------------------------------------------------------
                        # KPI 4
                        # ----------------------------------------------------------
                        html.Div(
                            className="tarjeta",
                            id="tarjeta4",
                            children=[
                                html.P("Promedio de Resultados"),
                                html.H2(id="kpi-maximos"),
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
                            children=[dcc.Graph(id="grafico-pastel")],
                        ),
                        # ----------------------------------------------------------
                        # GRÁFICO BARRAS
                        # ----------------------------------------------------------
                        html.Div(
                            className="barras",
                            children=[dcc.Graph(id="grafico-barras")],
                        ),
                        # ----------------------------------------------------------
                        # GRÁFICO 3
                        # ----------------------------------------------------------
                        html.Div(
                            className="grafico-3",
                            children=[dcc.Graph(id="grafico-3")],
                        ),
                        # ----------------------------------------------------------
                        # GRÁFICO 4
                        # ----------------------------------------------------------
                        html.Div(
                            className="grafico-4",
                            children=[dcc.Graph(id="grafico-modalidad")],
                        ),
                        # ----------------------------------------------------------
                        # GRÁFICO 5
                        # ----------------------------------------------------------
                        html.Div(
                            className="grafico-5",
                            children=[dcc.Graph(id="grafico-linea")],
                        ),
                    ],
                ),
            ],
        )
    )
