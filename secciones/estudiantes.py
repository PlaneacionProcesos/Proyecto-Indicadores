from dash import dcc, html
from componentes.estudiantes.tabla_estudiantes import tabla_estudiantes
from componentes.modal_contexto import banner_ayuda_tabla, layout_modal_contexto


def layout_estudiantes():

    return html.Div(
        className="contenedor-estudiantes",
        children=[
            # ==================================================================
            # Modal de Contexto y Ficha Técnica
            # ==================================================================
            layout_modal_contexto("estudiantes"),

            # ==================================================================
            # Tabla de indicadores de la seccion
            # ==================================================================
            html.Div(
                className="tabla-estudiantes",
                children=[
                    html.H3(
                        "Indicadores - Estudiantes",
                        id={"type": "titulo-tabla-seccion", "index": "estudiantes"},
                        className="titulo-tabla",
                        n_clicks=0,
                        style={"cursor": "pointer"},
                        title="Clic para gestionar/subir documentos",
                    ),
                    banner_ayuda_tabla(),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_estudiantes()],
                    ),
                ],
            ),
        ],
    )