from dash import dcc, html
from componentes.estudiantes.tabla_estudiantes import tabla_estudiantes

def layout_estudiantes():

    return html.Div(
        className="contenedor-estudiantes",
        children=[
            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-estudiantes",
                children=[
                    html.H3(
                        "Indicadores - Estudiantes",
                        className="titulo-tabla",
                    ),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_estudiantes()],
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
                        id="tarjetas-contexto-estudiantes",
                        className="grid-tarjetas-contexto",
                    ),
                ],
            ),
        ],
    )