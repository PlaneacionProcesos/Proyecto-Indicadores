from dash import dcc, html
from componentes.estudiantes.tabla_estudiantes import tabla_estudiantes

def layout_estudiantes():

    return html.Div(
        className="contenedor-estudiantes",
        children=[
            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-estudiantes",
                children=[
                    html.H3(
                            "Indicadores - Años (2024-2026)",
                            className="titulo-tabla",
                        ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_estudiantes()],
                    ),
                ]
            )
        ],
    )