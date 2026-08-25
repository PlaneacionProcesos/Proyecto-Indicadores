import os

from dotenv import load_dotenv
from dash import Input, Output, State, html, ctx, dcc, ALL, no_update

from componentes.db.crud import (
    subir_documento,
    listar_documentos,
    obtener_documento,
    eliminar_documento,
)

from componentes.db.categorias import CATEGORIAS_DOCUMENTOS

load_dotenv()

PASSWORD_ADMIN = os.getenv("PASSWORD_ADMIN")


# ==========================================================
# CATEGORÍAS VÁLIDAS
# ==========================================================

CATEGORIAS_VALIDAS = {categoria["value"] for categoria in CATEGORIAS_DOCUMENTOS}


def obtener_nombre_categoria(valor):
    """
    Convierte el valor interno de una categoría
    en el nombre que verá el usuario.
    """

    for categoria in CATEGORIAS_DOCUMENTOS:
        if categoria["value"] == valor:
            return categoria["label"]

    return "Sin categoría"


def registrar_callbacks_db(app):

    # ======================================================
    # 1. MOSTRAR / OCULTAR PANEL ADMIN
    # ======================================================

    @app.callback(
        Output("panel-admin", "style"),
        Input("btn-login-admin", "n_clicks"),
        State("input-clave-admin", "value"),
        prevent_initial_call=True,
    )
    def verificar_admin(n_clicks, clave):

        if clave and clave == PASSWORD_ADMIN:
            return {"display": "block"}

        return {"display": "none"}

    # ======================================================
    # 2. SUBIR DOCUMENTO
    # ======================================================

    @app.callback(
        Output("mensaje-subida", "children"),
        Input("upload-documento", "contents"),
        State("upload-documento", "filename"),
        State("seccion-actual", "data"),
        prevent_initial_call=True,
    )
    def procesar_subida(
        contenido,
        nombre,
        categoria,
    ):

        if not contenido or not nombre:
            return no_update

        # ----------------------------------------------
        # Validar categoría contextual
        # ----------------------------------------------

        if not categoria:
            return html.Div(
                "Error: No se pudo determinar la sección actual.",
                style={"color": "red"},
            )

        if categoria not in CATEGORIAS_VALIDAS:
            return html.Div(
                f"La sección actual '{categoria}' no admite documentos.",
                style={"color": "red"},
            )

        # ----------------------------------------------
        # Guardar documento
        # ----------------------------------------------

        try:

            subir_documento(
                contenido,
                nombre,
                categoria,
            )

            nombre_categoria = obtener_nombre_categoria(categoria)

            return html.Div(
                (
                    f"Archivo '{nombre}' subido "
                    f"exitosamente en la categoría "
                    f"'{nombre_categoria}'."
                ),
                style={"color": "green"},
            )

        except Exception as e:

            return html.Div(
                f"Error al subir el archivo: {str(e)}",
                style={"color": "red"},
            )

    # ======================================================
    # 3. RENDERIZAR LISTA DE DOCUMENTOS
    # ======================================================

    @app.callback(
        Output(
            "lista-documentos-ui",
            "children",
        ),
        Input(
            "mensaje-subida",
            "children",
        ),
        Input(
            "input-clave-admin",
            "value",
        ),
        Input(
            "seccion-actual",
            "data",
        ),
    )
    def actualizar_lista(
        mensaje,
        clave,
        categoria,
    ):

        # Validar que exista una categoría seleccionada antes de consultar a Mongo
        if not categoria:
            return html.Div(
                "Cargando sección...",
                style={"color": "#666", "marginTop": "15px"},
            )

        try:
            # Ahora le pasas la categoría para que Mongo filtre desde el backend
            docs = listar_documentos(categoria)

        except Exception as e:

            return html.Div(
                f"Error al cargar los documentos: {str(e)}",
                style={"color": "red"},
            )

        es_admin = clave and clave == PASSWORD_ADMIN

        elementos_lista = []

        for doc in docs:

            cat_doc = doc.get(
                "categoria",
                "Sin categoría",
            )

            nombre_categoria = obtener_nombre_categoria(cat_doc)

            # ------------------------------------------
            # Botón descargar
            # ------------------------------------------

            botones = [
                html.Button(
                    "Descargar",
                    id={
                        "type": "btn-descargar",
                        "index": doc["id"],
                    },
                    className="btn-descargar",
                )
            ]

            # ------------------------------------------
            # Botón eliminar para administrador
            # ------------------------------------------

            if es_admin:

                botones.append(
                    html.Button(
                        "Eliminar",
                        id={
                            "type": "btn-eliminar",
                            "index": doc["id"],
                        },
                        className="btn-eliminar",
                    )
                )

            # ------------------------------------------
            # Elemento del documento
            # ------------------------------------------

            item = html.Li(
                className="gestor-item",
                children=[
                    html.Div(
                        className="gestor-item-info",
                        children=[
                            html.Span(doc["nombre"], className="gestor-item-titulo"),
                            html.Span(
                                (
                                    f"Categoría: {nombre_categoria} | "
                                    f"Fecha: {doc['fecha'].strftime('%Y-%m-%d')}"
                                ),
                                className="gestor-item-meta",
                            ),
                        ],
                    ),
                    html.Div(className="gestor-acciones", children=botones),
                ],
            )

            elementos_lista.append(item)

        # ----------------------------------------------
        # No hay documentos
        # ----------------------------------------------

        if not elementos_lista:
            nombre_seccion_actual = obtener_nombre_categoria(categoria)
            return html.Div(
                f"No hay documentos disponibles para la sección '{nombre_seccion_actual}'.",
                style={
                    "color": "var(--text-soft)",
                    "textAlign": "center",
                    "padding": "20px 0",
                    "fontWeight": "600",
                },
            )

        return html.Ul(elementos_lista, className="gestor-lista")

    # ======================================================
    # 4. DESCARGAR / ELIMINAR DOCUMENTO
    # ======================================================

    @app.callback(
        Output(
            "descargar-documento",
            "data",
        ),
        Output(
            "mensaje-subida",
            "children",
            allow_duplicate=True,
        ),
        Input(
            {
                "type": "btn-descargar",
                "index": ALL,
            },
            "n_clicks",
        ),
        Input(
            {
                "type": "btn-eliminar",
                "index": ALL,
            },
            "n_clicks",
        ),
        prevent_initial_call=True,
    )
    def accion_documento(
        btn_descargas,
        btn_eliminaciones,
    ):

        trigger_id = ctx.triggered_id

        if not trigger_id:
            return no_update, no_update

        # ==================================================
        # ⚠️ SOLUCIÓN AL BUG DE DESCARGA AUTOMÁTICA
        # ==================================================
        trigger_value = ctx.triggered[0]["value"]
        if trigger_value is None:
            return no_update, no_update

        doc_id = trigger_id["index"]
        accion = trigger_id["type"]

        # ==================================================
        # DESCARGAR
        # ==================================================

        if accion == "btn-descargar":

            try:

                contenido_bytes, nombre = obtener_documento(doc_id)

                if not contenido_bytes:

                    return (
                        no_update,
                        html.Div(
                            "No se encontró el documento.",
                            style={"color": "red"},
                        ),
                    )

                return (
                    dcc.send_bytes(
                        lambda buffer: buffer.write(contenido_bytes),
                        nombre,
                    ),
                    no_update,
                )

            except Exception as e:

                return (
                    no_update,
                    html.Div(
                        ("Error al descargar " f"el archivo: {str(e)}"),
                        style={"color": "red"},
                    ),
                )

        # ==================================================
        # ELIMINAR
        # ==================================================

        if accion == "btn-eliminar":

            try:

                eliminar_documento(doc_id)

                return (
                    no_update,
                    html.Div(
                        "Archivo eliminado correctamente.",
                        style={"color": "green"},
                    ),
                )

            except Exception as e:

                return (
                    no_update,
                    html.Div(
                        ("Error al eliminar " f"el archivo: {str(e)}"),
                        style={"color": "red"},
                    ),
                )

        return no_update, no_update
