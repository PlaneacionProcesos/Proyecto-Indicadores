from dash import html


def layout_footer():

    return html.Footer(
        className="footer",
        children=[

            html.Div(
                className="footer-contenido",
                children=[

                    html.Strong(
                        "Datos tomados de [Fuente] - "
                        "con fecha de corte del 19 de agosto de 2026"
                    ),

                    html.Br(

                    ),

                    html.Strong(
                        "Todos los derechos reservados © UNIMINUTO"
                    ),

                ],
            ),

        ],
    )