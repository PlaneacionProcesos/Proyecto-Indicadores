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
                        id={"type": "titulo-tabla-seccion", "index": "sostenibilidad"},
                        className="titulo-tabla",
                        n_clicks=0,
                        style={"cursor": "pointer"},
                        title="Clic para gestionar/subir documentos",
                    ),
                    banner_ayuda_tabla(),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_sostenibilidad()],
                    ),
                ],
            ),
        ],
    )