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
                        id="tarjetas-contexto-profesores",
                        className="grid-tarjetas-contexto",
                    ),
                ],
            ),
        ],
    )