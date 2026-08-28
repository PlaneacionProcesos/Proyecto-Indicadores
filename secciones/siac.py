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
                        "Indicadores - SIAC",
                        className="titulo-tabla",
                    ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_siac()],
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
                        id="tarjetas-contexto-siac",
                        className="grid-tarjetas-contexto",
                    ),
                ],
            ),
        ],
    )