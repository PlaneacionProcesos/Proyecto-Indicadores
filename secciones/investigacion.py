from dash import dcc, html
from componentes.investigacion.tabla_investigacion import tabla_investigacion

def layout_investigacion():

    return html.Div(
        className="contenedor-investigacion",
        children=[
            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-investigacion",
                children=[
                    html.H3(
                            "Indicadores - Años (2024-2026)",
                            className="titulo-tabla",
                        ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_investigacion()],
                    ),
                ]
            )
        ],
    )