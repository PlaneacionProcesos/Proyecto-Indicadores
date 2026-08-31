from dash import html
from componentes.factory.tabla import crear_tabla_seccion
from componentes.modal_contexto import banner_ayuda_tabla, layout_modal_contexto


def crear_layout_seccion(seccion_id: str, titulo: str):
    """
    Genera el contenedor completo de una sección (modal, banner, tabla y títulos).
    Reemplaza la duplicación de los 7 archivos secciones/*.py.
    """
    return html.Div(
        className=f"contenedor-{seccion_id}",
        children=[
            # ==================================================================
            # Modal de Contexto y Ficha Técnica
            # ==================================================================
            layout_modal_contexto(seccion_id),

            # ==================================================================
            # Tabla de indicadores de la sección
            # ==================================================================
            html.Div(
                className=f"tabla-{seccion_id}",
                children=[
                    html.H3(
                        f"Indicadores - {titulo}",
                        id={"type": "titulo-tabla-seccion", "index": seccion_id},
                        className="titulo-tabla",
                        n_clicks=0,
                        style={"cursor": "pointer"},
                        title="Clic para gestionar/subir documentos",
                    ),
                    banner_ayuda_tabla(),
                    html.Div(
                        className="tabla-contenedor",
                        children=[crear_tabla_seccion(seccion_id)],
                    ),
                ],
            ),
        ],
    )

