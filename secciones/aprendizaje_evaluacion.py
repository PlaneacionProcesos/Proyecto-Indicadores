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
                        "Indicadores - Aprendizaje y Evaluación",
                        className="titulo-tabla",
                    ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_aprendizaje()],
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
                        id="tarjetas-contexto-aprendizaje",
                        className="grid-tarjetas-contexto",
                    ),
                ],
            ),
        ],
    )
