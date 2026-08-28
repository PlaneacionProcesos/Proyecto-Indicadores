from dash import dcc, html
from componentes.profesores.tabla_profesores import tabla_profesores
from componentes.modal_contexto import banner_ayuda_tabla, layout_modal_contexto


def layout_profesores():

    return html.Div(
        className="contenedor-profesores",
        children=[
            # ==================================================================
            # Modal de Contexto y Ficha Técnica
            # ==================================================================
            layout_modal_contexto("profesores"),

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
                    banner_ayuda_tabla(),
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
                                "Consulta el macroproceso, proceso y fórmula de cálculo de cada indicador. Al hacer clic en una fila de la tabla, su tarjeta se resaltará automáticamente.",
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