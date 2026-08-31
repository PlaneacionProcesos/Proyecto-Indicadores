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
                        id={"type": "titulo-tabla-seccion", "index": "aprendizaje_evaluacion"},
                        className="titulo-tabla",
                        n_clicks=0,
                        style={"cursor": "pointer"},
                        title="Clic para gestionar/subir documentos",
                    ),
                    banner_ayuda_tabla(),
                    html.Div(
                        className="tabla-contenedor",
                        children=[tabla_aprendizaje()],
                    ),
                ],
            ),
        ],
    )

