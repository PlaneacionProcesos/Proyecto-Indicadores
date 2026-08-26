from dash import dcc, html
from componentes.impacto.tabla_impacto import tabla_impacto

def layout_impacto():

    return html.Div(
        className="contenedor-impacto",
        children=[
            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-impacto",
                children=[
                    html.H3(
                            "Indicadores - Años (2024-2026)",
                            className="titulo-tabla",
                        ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_impacto()],
                    ),
                ]
            )
        ],
    )