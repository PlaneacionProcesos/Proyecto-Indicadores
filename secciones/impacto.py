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
                        id={"type": "titulo-tabla-seccion", "index": "impacto"},
                        className="titulo-tabla",
                        n_clicks=0,
                        style={"cursor": "pointer"},
                        title="Clic para gestionar/subir documentos",
                    ),
                    banner_ayuda_tabla(),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_impacto()],
                    ),
                ],
            ),
        ],
    )