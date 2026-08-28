from dash import dcc, html
from componentes.impacto.tabla_impacto import tabla_impacto
from componentes.modal_contexto import banner_ayuda_tabla, layout_modal_contexto


def layout_impacto():

    return html.Div(
        className="contenedor-impacto",
        children=[
            # ==================================================================
            # Modal de Contexto y Ficha Técnica
            # ==================================================================
            layout_modal_contexto("impacto"),

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
                    banner_ayuda_tabla(),
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
                                "Consulta el macroproceso, proceso y fórmula de cálculo de cada indicador. Al hacer clic en una fila de la tabla, su tarjeta se resaltará automáticamente.",
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