import os

from dotenv import load_dotenv
from dash import Input, Output, State, html, ctx, dcc, ALL, no_update

from componentes.db.crud import (
    subir_documento,
    listar_documentos,
    obtener_documento,
    eliminar_documento,
)

from componentes.db.categorias import CATEGORIAS_DOCUMENTOS, TIPOS_DOCUMENTOS
from datos import resultados_completos

load_dotenv()

PASSWORD_ADMIN = os.getenv("PASSWORD_ADMIN")


# ==========================================================
# CATEGORÍAS VÁLIDAS Y MAPEO CON AGRUPADORES
# ==========================================================

CATEGORIAS_VALIDAS = {categoria["value"] for categoria in CATEGORIAS_DOCUMENTOS}

MAPEO_SECCION_AGRUPADOR = {
    "profesores": "Profesores",
    "aprendizaje_evaluacion": "Aprendizaje y Evaluacion",
    "estudiantes": "Estudiantes",
    "impacto": "Impacto",
    "investigacion": "Investigacion",
    "siac": "SIAC - Rendicion de Cuentas",
    "sostenibilidad": "Sostenibilidad",
}


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
    # 0. POBLAR OPCIONES DE INDICADORES EN EL DROPDOWN DE SUBIDA
    # ======================================================

    @app.callback(
        Output("dropdown-numero-ind-subida", "options"),
        Output("dropdown-numero-ind-subida", "value"),
        Input("seccion-actual", "data"),
    )
    def actualizar_opciones_indicadores(seccion):
        if not seccion:
            return [], None

        agrupador = MAPEO_SECCION_AGRUPADOR.get(seccion)
        if not agrupador:
            return [], None

        df_sec = resultados_completos[resultados_completos["agrupador"] == agrupador]
        df_unicos = df_sec[["numero_ind", "nombre indicador"]].dropna().drop_duplicates()

        opciones = []
        for _, row in df_unicos.iterrows():
            num = str(row["numero_ind"]).strip()
            nom = str(row["nombre indicador"]).strip()
            if num and num.lower() != "nan":
                opciones.append({
                    "label": f"{num} — {nom}",
                    "value": num,
                })

        opciones.sort(key=lambda x: x["label"])
        return opciones, None

    # ======================================================
    # 1. MOSTRAR / OCULTAR MODAL DE GESTOR DE DOCUMENTOS
    # ======================================================

    @app.callback(
        Output("modal-gestor-documentos", "style"),
        Output("titulo-gestor-modal", "children"),
        Input({"type": "titulo-tabla-seccion", "index": ALL}, "n_clicks"),
        Input("btn-cerrar-gestor-modal", "n_clicks"),
        Input("btn-entendido-gestor-modal", "n_clicks"),
        State("seccion-actual", "data"),
        prevent_initial_call=True,
    )
    def controlar_modal_gestor(clics_titulos, n_close_x, n_close_btn, seccion_actual):
        trigger = ctx.triggered_id

        # Si se hace clic en alguno de los botones de cerrar el modal
        if trigger in ("btn-cerrar-gestor-modal", "btn-entendido-gestor-modal"):
            return {"display": "none"}, "Documentos de la Sección"

        # Si se hace clic en algún título de tabla de la sección (requiere 3 clics)
        if isinstance(trigger, dict) and trigger.get("type") == "titulo-tabla-seccion":
            val_clic = ctx.triggered[0]["value"] if ctx.triggered else 0
            if val_clic and val_clic >= 3 and val_clic % 3 == 0:
                nombre_sec = obtener_nombre_categoria(seccion_actual)
                return {"display": "flex"}, f"Documentos y Evidencias - {nombre_sec}"

        return no_update, no_update

    # ======================================================
    # 2. MOSTRAR / OCULTAR ZONA DE LOGIN ADMIN
    # ======================================================

    @app.callback(
        Output("zona-login-admin", "style"),
        Output("input-clave-admin", "value"),
        Input("btn-mostrar-login-admin", "n_clicks"),
        Input("btn-cerrar-admin", "n_clicks"),
        State("zona-login-admin", "style"),
        prevent_initial_call=True,
    )
    def toggle_login_admin(clics_mostrar, clics_cerrar, estilo_actual):
        trigger = ctx.triggered_id

        if trigger == "btn-cerrar-admin":
            return {"display": "none"}, ""

        if trigger == "btn-mostrar-login-admin":
            esta_visible = estilo_actual and estilo_actual.get("display") != "none"
            nuevo_estilo = {"display": "none"} if esta_visible else {"display": "flex"}
            return nuevo_estilo, no_update

        return no_update, no_update

    # ======================================================
    # 3. MOSTRAR / OCULTAR PANEL ADMIN (SUBIDA DE ARCHIVOS)
    # ======================================================

    @app.callback(
        Output("panel-admin", "style"),
        Input("btn-login-admin", "n_clicks"),
        Input("btn-cerrar-admin", "n_clicks"),
        State("input-clave-admin", "value"),
        prevent_initial_call=True,
    )
    def verificar_admin(n_clicks_login, n_clicks_cerrar, clave):
        trigger = ctx.triggered_id

        if trigger == "btn-cerrar-admin":
            return {"display": "none"}

        if clave and clave == PASSWORD_ADMIN:
            return {"display": "block"}

        return {"display": "none"}

    # ======================================================
    # 3. SUBIR DOCUMENTO (CON TIPO SGC / ESTRATÉGICOS Y NUMERO_IND)
    # ======================================================

    @app.callback(
        Output("mensaje-subida", "children"),
        Input("upload-documento", "contents"),
        State("upload-documento", "filename"),
        State("seccion-actual", "data"),
        State("radio-tipo-documento", "value"),
        State("dropdown-numero-ind-subida", "value"),
        prevent_initial_call=True,
    )
    def procesar_subida(
        contenido,
        nombre,
        categoria,
        tipo_doc,
        numero_ind,
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

        tipo_seleccionado = tipo_doc if tipo_doc in ("SGC", "Estrategicos") else "SGC"
        num_ind_limpio = str(numero_ind).strip() if numero_ind and str(numero_ind).strip() != "" else None

        # ----------------------------------------------
        # Guardar documento en MongoDB GridFS con metadatos
        # ----------------------------------------------

        try:

            subir_documento(
                contenido,
                nombre,
                categoria,
                tipo=tipo_seleccionado,
                numero_ind=num_ind_limpio,
            )

            nombre_categoria = obtener_nombre_categoria(categoria)
            label_tipo = "SGC" if tipo_seleccionado == "SGC" else "Estratégicos"
            ind_info = f" [Indicador: {num_ind_limpio}]" if num_ind_limpio else ""

            return html.Div(
                (
                    f"Archivo '{nombre}' [{label_tipo}]{ind_info} subido "
                    f"exitosamente en la categoría "
                    f"'{nombre_categoria}'."
                ),
                style={"color": "green", "fontWeight": "600"},
            )

        except Exception as e:

            return html.Div(
                f"Error al subir el archivo: {str(e)}",
                style={"color": "red"},
            )

    # ======================================================
    # 4. RENDERIZAR LISTA DE DOCUMENTOS (CON FILTRO DE TIPO Y BADGES)
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
        Input(
            "filtro-tipo-doc-lista",
            "value",
        ),
    )
    def actualizar_lista(
        mensaje,
        clave,
        categoria,
        filtro_tipo,
    ):

        # Validar que exista una categoría seleccionada antes de consultar a Mongo
        if not categoria:
            return html.Div(
                "Cargando sección...",
                style={"color": "#666", "marginTop": "15px"},
            )

        tipo_param = None if (not filtro_tipo or filtro_tipo == "Todos") else filtro_tipo

        try:
            # Ahora le pasas la categoría y el tipo para filtrar en Mongo
            docs = listar_documentos(categoria, tipo=tipo_param)

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

            tipo_doc = doc.get(
                "tipo",
                "SGC",
            )

            num_ind_doc = doc.get(
                "numero_ind",
                None,
            )

            nombre_categoria = obtener_nombre_categoria(cat_doc)

            # Badge de Tipo de Archivo
            if tipo_doc == "Estrategicos":
                badge_tipo = html.Span("Estratégicos", className="badge-tipo badge-tipo-estrategico")
            else:
                badge_tipo = html.Span("SGC", className="badge-tipo badge-tipo-sgc")

            badges_header = [badge_tipo]
            if num_ind_doc:
                badges_header.append(
                    html.Span(
                        num_ind_doc,
                        className="badge-tipo",
                        style={
                            "backgroundColor": "#f1f5f9",
                            "color": "#334155",
                            "border": "1px solid #cbd5e1",
                        },
                    )
                )

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
                        className="gestor-item-contenido",
                        children=[
                            html.Img(
                                src="assets/iconos/pdf_icon.png", 
                                className="icono-documento-item",
                                alt="Icono documento",
                            ),
                            html.Div(
                                className="gestor-item-info",
                                children=[
                                    html.Div([
                                        *badges_header,
                                        html.Span(doc["nombre"], className="gestor-item-titulo"),
                                    ]),
                                    html.Span(
                                        (
                                            f"Categoría: {nombre_categoria} | "
                                            f"Fecha: {doc['fecha'].strftime('%Y-%m-%d')}"
                                        ),
                                        className="gestor-item-meta",
                                    ),
                                ],
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
            tipo_txt = f" de tipo '{filtro_tipo}'" if filtro_tipo and filtro_tipo != "Todos" else ""
            return html.Div(
                f"No hay documentos{tipo_txt} disponibles para la sección '{nombre_seccion_actual}'.",
                style={
                    "color": "var(--text-soft)",
                    "textAlign": "center",
                    "padding": "20px 0",
                    "fontWeight": "600",
                },
            )

        return html.Ul(elementos_lista, className="gestor-lista")

    # ======================================================
    # 5. DESCARGAR / ELIMINAR DOCUMENTO
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
