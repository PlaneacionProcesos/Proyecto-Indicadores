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
                        id="tarjetas-contexto-sostenibilidad",
                        className="grid-tarjetas-contexto",
                    ),
                ],
            ),
        ],
    )