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
                        "UNIMINUTO Sede Bogotá"
                    ),

                    html.Span(
                        "Indicadores de seguimiento SGC - Estrategicos."
                    )

                ]
            ),

            html.Img(
                className="adorno-lineas",
                src="assets/adorno_header_transparente_110px.png"
            )


        ],
    )