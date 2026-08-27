from dash import dcc, html

from componentes.resumen.tabla_agrupadores import tabla_agrupadores


def layout_resumen():

    return html.Div(
        className="graficas",
        children=[
            # ==================================================================
            # VISUALIZACIONES
            # ==================================================================
            html.Div(
                className="visualizaciones",
                children=[
                    # ----------------------------------------------------------
                    # TARJETAS
                    # ----------------------------------------------------------
                    html.Div(
                        className="tarjetas",
                        children=[
                            # ----------------------------------------------------------
                            # KPI 1: Registros Históricos
                            # ----------------------------------------------------------
                            html.Div(
                                className="tarjeta",
                                id="tarjeta1",
                                children=[
                                    html.Img(
                                        src="assets/indicadores_totales_icon.png", 
                                        className="icono-kpi",
                                        alt="Icono Registros",
                                    ),
                                    html.Div(
                                        className="info-kpi",
                                        children=[
                                            html.H2(id="kpi-it"),
                                            html.P("Registros Históricos"),
                                        ],
                                    ),
                                ],
                            ),
                            # ----------------------------------------------------------
                            # KPI 2: Indicadores Estratégicos
                            # ----------------------------------------------------------
                            html.Div(
                                className="tarjeta",
                                id="tarjeta2",
                                children=[
                                    html.Img(
                                        src="assets/indicadores_estrategicos_icon.png",  
                                        className="icono-kpi",
                                        alt="Icono Estratégicos",
                                    ),
                                    html.Div(
                                        className="info-kpi",
                                        children=[
                                            html.H2(id="kpi-ies"),
                                            html.P("Indicadores Estratégicos"),
                                        ],
                                    ),
                                ],
                            ),
                            # ----------------------------------------------------------
                            # KPI 3: Indicadores del SGC
                            # ----------------------------------------------------------
                            html.Div(
                                className="tarjeta",
                                id="tarjeta3",
                                children=[
                                    html.Img(
                                        src="assets/indicadores_sgc_icon.png",  
                                        className="icono-kpi",
                                        alt="Icono SGC",
                                    ),
                                    html.Div(
                                        className="info-kpi",
                                        children=[
                                            html.H2(id="kpi-its"),
                                            html.P("Indicadores del SGC"),
                                        ],
                                    ),
                                ],
                            ),
                            # ----------------------------------------------------------
                            # KPI 4: En Construcción
                            # ----------------------------------------------------------
                            html.Div(
                                className="tarjeta",
                                id="tarjeta4",
                                children=[
                                    html.Img(
                                        src="assets/iconos/kpi_construccion.png",  
                                        className="icono-kpi",
                                        alt="Icono En Construcción",
                                    ),
                                    html.Div(
                                        className="info-kpi",
                                        children=[
                                            html.H2(id="kpi-maximos"),
                                            html.P("En construccion"),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
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
                        className="tabla-agrupadores",
                        children=[
                            html.H3(
                                "Indicadores por agrupador",
                                className="titulo-tabla",
                            ),
                            html.Div(
                                className="tabla-contenedor",
                                children=[tabla_agrupadores()],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
