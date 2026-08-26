from dash import dcc, html
from componentes.siac.tabla_siac import tabla_siac

def layout_siac():

    return html.Div(
        className="contenedor-siac",
        children=[
            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-siac",
                children=[
                    html.H3(
                            "Indicadores - Años (2024-2026)",
                            className="titulo-tabla",
                        ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_siac()],
                    ),
                ]
            )
        ],
    )