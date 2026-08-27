from dash import dcc, html
from componentes.impacto.tabla_impacto import tabla_impacto

def layout_impacto():

    return html.Div(
        className="contenedor-impacto",
        children=[
            # ==================================================================
            # Tabla de indicadores de la sección
            # ==================================================================
            html.Div(
                className="tabla-impacto",
                children=[
                    html.H3(
                            "Indicadores - Impacto",
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