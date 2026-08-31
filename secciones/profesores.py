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
                        id={"type": "titulo-tabla-seccion", "index": "profesores"},
                        className="titulo-tabla",
                        n_clicks=0,
                        style={"cursor": "pointer"},
                        title="Clic para gestionar/subir documentos",
                    ),
                    banner_ayuda_tabla(),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_profesores()],
                    ),
                ],
            ),
        ],
    )