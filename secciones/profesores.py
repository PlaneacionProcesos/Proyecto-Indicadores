from dash import dcc, html
from componentes.profesores.tabla_profesores import tabla_profesores

def layout_profesores():

    return html.Div(
        className="contenedor-profesores",
        children=[
            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-profesores",
                children=[
                    html.H3(
                            "Indicadores - Profesores",
                            className="titulo-tabla",
                        ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_profesores()],
                    ),
                ]
            )
        ],
    )