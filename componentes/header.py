from dash import dcc, html

def layout_header():
    return(
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
        )
    )