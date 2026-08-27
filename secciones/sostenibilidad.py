from dash import dcc, html
from componentes.sostenibilidad.tabla_sostenibilidad import tabla_sostenibilidad

def layout_sostenibilidad():

    return html.Div(
        className="contenedor-sostenibilidad",
        children=[
            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-sostenibilidad",
                children=[
                    html.H3(
                            "Indicadores - Sostenibilidad",
                            className="titulo-tabla",
                        ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_sostenibilidad()],
                    ),
                ]
            )
        ],
    )