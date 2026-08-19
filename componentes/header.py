from dash import html


def layout_header():

    return html.Div(
        className="header",
        children=[

            html.Img(
                className="logo",
                src="assets/Logo_Unificado.png"
            ),

            html.Div(
                className="titulo",
                children=[

                    html.H1(
                        "Indicadores Generales"
                    ),

                    html.Span(
                        "Indicadores estratégicos y del SGC que permiten "
                        "hacer seguimiento al cumplimiento de los procesos "
                        "y al logro de los objetivos institucionales."
                    )

                ]
            ),

            html.Div(
                className="fecha-actualizacion",
                children=[

                    html.Img(
                        className="icono-calendario",
                        src="assets/calendario.png"
                    ),

                    html.Div(
                        className="informacion-periodo",
                        children=[

                            html.P(
                                "PERIODO ACADÉMICO"
                            ),

                            html.Strong(
                                "Semestre 2"
                            ),

                            html.Strong(
                                "Año: 2026"
                            ),

                        ],
                    ),

                ],
            ),

        ],
    )