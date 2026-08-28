from dash import dcc, html
from componentes.sostenibilidad.tabla_sostenibilidad import tabla_sostenibilidad
from componentes.modal_contexto import banner_ayuda_tabla, layout_modal_contexto


def layout_sostenibilidad():

    return html.Div(
        className="contenedor-sostenibilidad",
        children=[
            # ==================================================================
            # Modal de Contexto y Ficha Técnica
            # ==================================================================
            layout_modal_contexto("sostenibilidad"),

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
                    banner_ayuda_tabla(),
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
                                "Consulta el macroproceso, proceso y fórmula de cálculo de cada indicador. Al hacer clic en una fila de la tabla, su tarjeta se resaltará automáticamente.",
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