from dash import dcc, html
from componentes.siac.tabla_siac import tabla_siac
from componentes.modal_contexto import banner_ayuda_tabla, layout_modal_contexto


def layout_siac():

    return html.Div(
        className="contenedor-siac",
        children=[
            # ==================================================================
            # Modal de Contexto y Ficha Técnica
            # ==================================================================
            layout_modal_contexto("siac"),

            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-siac",
                children=[
                    html.H3(
                        "Indicadores - SIAC",
                        id={"type": "titulo-tabla-seccion", "index": "siac"},
                        className="titulo-tabla",
                        n_clicks=0,
                        style={"cursor": "pointer"},
                        title="Clic para gestionar/subir documentos",
                    ),
                    banner_ayuda_tabla(),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_siac()],
                    ),
                ],
            ),
        ],
    )