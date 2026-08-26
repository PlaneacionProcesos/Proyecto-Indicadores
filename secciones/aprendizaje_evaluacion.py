from dash import dcc, html
from componentes.aprendizaje_y_evaluacion.tabla_aprendizaje import tabla_aprendizaje

def layout_aprendizaje():

    return html.Div(
        className="contenedor-aprendizaje",
        children=[
            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-aprendizaje",
                children=[
                    html.H3(
                            "Indicadores - Años (2024-2026)",
                            className="titulo-tabla",
                        ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_aprendizaje()],
                    ),
                ]
            )
        ],
    )