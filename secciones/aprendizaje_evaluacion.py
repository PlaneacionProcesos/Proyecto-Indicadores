from dash import dcc, html
from componentes.aprendizaje_y_evaluacion.tabla_aprendizaje import tabla_aprendizaje
from componentes.modal_contexto import banner_ayuda_tabla, layout_modal_contexto


def layout_aprendizaje():

    return html.Div(
        className="contenedor-aprendizaje",
        children=[
            # ==================================================================
            # Modal de Contexto y Ficha Técnica
            # ==================================================================
            layout_modal_contexto("aprendizaje"),

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
                    banner_ayuda_tabla(),
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
                                "Consulta el macroproceso, proceso y fórmula de cálculo de cada indicador. Al hacer clic en una fila de la tabla, su tarjeta se resaltará automáticamente.",
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

