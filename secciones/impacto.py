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
                ],
            ),
            # ==================================================================
            # Contexto y Fichas de Indicadores (Tarjetas de detalle)
            # ==================================================================
            html.Div(
                className="seccion-contexto-indicadores",
                children=[
                    html.Div(
                        className="encabezado-contexto-indicadores",
                        children=[
                            html.H3(
                                "Contexto y Metodología de los Indicadores",
                                className="titulo-contexto",
                            ),
                            html.P(
                                "Haz clic en 'Ver detalles' en cualquier tarjeta para desplegar el macroproceso, proceso y fórmula de cálculo correspondiente.",
                                className="subtitulo-contexto",
                            ),
                        ],
                    ),
                    html.Div(
                        id="tarjetas-contexto-impacto",
                        className="grid-tarjetas-contexto",
                    ),
                ],
            ),
        ],
    )