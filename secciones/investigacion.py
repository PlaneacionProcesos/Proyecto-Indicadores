from dash import dcc, html
from componentes.investigacion.tabla_investigacion import tabla_investigacion
from componentes.modal_contexto import banner_ayuda_tabla, layout_modal_contexto


def layout_investigacion():

    return html.Div(
        className="contenedor-investigacion",
        children=[
            # ==================================================================
            # Modal de Contexto y Ficha Técnica
            # ==================================================================
            layout_modal_contexto("investigacion"),

            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-investigacion",
                children=[
                    html.H3(
                        "Indicadores - Investigación",
                        id={"type": "titulo-tabla-seccion", "index": "investigacion"},
                        className="titulo-tabla",
                        n_clicks=0,
                        style={"cursor": "pointer"},
                        title="Clic para gestionar/subir documentos",
                    ),
                    banner_ayuda_tabla(),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_investigacion()],
                    ),
                ],
            ),
        ],
    )