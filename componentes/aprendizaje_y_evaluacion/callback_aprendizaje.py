import dash
from dash import Input, Output, State, ctx, html, dcc, no_update
from datos import resultados_completos
import pandas as pd
from componentes.modal_contexto import generar_cuerpo_modal
from componentes.db.crud import obtener_documento_por_indicador


def registrar_callback_aprendizaje(app):

    # ==========================================================================
    # Callback de Alto Rendimiento (Tabla de Aprendizaje)
    # ==========================================================================
    @app.callback(
        Output("tabla-aprendizaje", "data"),
        Input("filtro-año", "value"),
        Input("filtro-centro", "value"),
        Input("filtro-periodo", "value"),
        Input("filtro-nivel", "value"),
        Input("filtro-modalidad", "value"),
        Input("filtro-tipo", "value"),
        Input("filtro-tiempo-reporte", "value"),
        Input("seccion-actual", "data"),
    )
    def datos_tabla_aprendizaje(
        año, centro, periodo, nivel, modalidad, tipo, tiempo_reporte,
        seccion_actual
    ):
        # 1. Guard de Sección
        if seccion_actual is not None and seccion_actual != "aprendizaje_evaluacion":
            return dash.no_update

        # 2. Filtrar DataFrame del agrupador
        datos_ae = resultados_completos[
            resultados_completos["agrupador"] == "Aprendizaje y Evaluacion"
        ].copy()

        if año is not None and año != "Historico":
            try:
                if int(año) in datos_ae["ano"].values:
                    datos_ae = datos_ae[datos_ae["ano"] == int(año)]
            except (ValueError, TypeError):
                pass

        if centro is not None and centro != "Todos":
            if centro in datos_ae["centro_universitario"].values:
                datos_ae = datos_ae[datos_ae["centro_universitario"] == centro]

        if periodo is not None and periodo != "Todos":
            if periodo in datos_ae["periodo academico"].values:
                datos_ae = datos_ae[datos_ae["periodo academico"] == periodo]

        if nivel is not None and nivel != "Todos":
            if nivel in datos_ae["nivel academico"].values:
                datos_ae = datos_ae[datos_ae["nivel academico"] == nivel]

        if modalidad is not None and modalidad != "Todos":
            if modalidad in datos_ae["modalidad"].values:
                datos_ae = datos_ae[datos_ae["modalidad"] == modalidad]

        if tipo is not None and tipo != "Todos":
            if tipo in datos_ae["tipo de indicador"].values:
                datos_ae = datos_ae[datos_ae["tipo de indicador"] == tipo]

        if tiempo_reporte is not None and tiempo_reporte != "Todos":
            if str(tiempo_reporte) in datos_ae["tiempo de reporte"].astype(str).values:
                datos_ae = datos_ae[
                    datos_ae["tiempo de reporte"].astype(str) == str(tiempo_reporte)
                ]

        # 3. Procesar datos para la tabla
        if datos_ae.empty:
            df_resultado = pd.DataFrame(
                columns=[
                    "nombre_indicador",
                    "año-2023",
                    "año-2024",
                    "año-2025",
                    "año-2026",
                    "variacion-ultimos_dos",
                    "porcentaje_variacion",
                ]
            )
            return df_resultado.to_dict("records")

        indicadores = datos_ae["nombre indicador"].drop_duplicates()
        df_resultado = pd.DataFrame({"nombre_indicador": indicadores})

        serie_2023 = (
            datos_ae[datos_ae["ano"] == 2023]
            .dropna(subset=["resultado"])
            .groupby("nombre indicador")["resultado"]
            .mean()
        )
        serie_2024 = (
            datos_ae[datos_ae["ano"] == 2024]
            .dropna(subset=["resultado"])
            .groupby("nombre indicador")["resultado"]
            .mean()
        )
        serie_2025 = (
            datos_ae[datos_ae["ano"] == 2025]
            .dropna(subset=["resultado"])
            .groupby("nombre indicador")["resultado"]
            .mean()
        )
        serie_2026 = (
            datos_ae[datos_ae["ano"] == 2026]
            .dropna(subset=["resultado"])
            .groupby("nombre indicador")["resultado"]
            .mean()
        )

        val_2023 = df_resultado["nombre_indicador"].map(serie_2023)
        val_2024 = df_resultado["nombre_indicador"].map(serie_2024)
        val_2025 = df_resultado["nombre_indicador"].map(serie_2025)
        val_2026 = df_resultado["nombre_indicador"].map(serie_2026)

        df_resultado["año-2023"] = val_2023.apply(
            lambda x: f"{round(x, 2):.0%}" if pd.notna(x) else "Sin datos"
        )
        df_resultado["año-2024"] = val_2024.apply(
            lambda x: f"{round(x, 2):.0%}" if pd.notna(x) else "Sin datos"
        )
        df_resultado["año-2025"] = val_2025.apply(
            lambda x: f"{round(x, 2):.0%}" if pd.notna(x) else "Sin datos"
        )
        df_resultado["año-2026"] = val_2026.apply(
            lambda x: f"{round(x, 2):.0%}" if pd.notna(x) else "Sin datos"
        )

        def calcular_variacion_absoluta(v_actual, v_anterior):
            if pd.notna(v_actual) and pd.notna(v_anterior):
                diff = v_actual - v_anterior
                return f"{round(diff, 2):.0%}"

            return "Sin datos"

        def calcular_variacion_porcentual(v_actual, v_anterior):
            if pd.notna(v_actual) and pd.notna(v_anterior):
                if v_anterior != 0:
                    pct = ((v_actual - v_anterior) / abs(v_anterior)) * 100
                    return f"{pct:+.2f}%"
                return "0.00%"
            return "Sin datos"

        df_resultado["variacion-ultimos_dos"] = [
            calcular_variacion_absoluta(a, b)
            for a, b in zip(val_2026, val_2025)
        ]
        df_resultado["porcentaje_variacion"] = [
            calcular_variacion_porcentual(a, b)
            for a, b in zip(val_2026, val_2025)
        ]

        df_resultado["nombre_indicador"] = df_resultado["nombre_indicador"].apply(lambda x: f"👁️  {x}")

        return df_resultado.to_dict("records")

    # ==========================================================================
    # Callback para Controlar Apertura y Cierre del Modal de Aprendizaje
    # ==========================================================================
    @app.callback(
        Output("modal-contexto-aprendizaje", "style"),
        Output("modal-titulo-aprendizaje", "children"),
        Output("modal-cuerpo-aprendizaje", "children"),
        Output("tabla-aprendizaje", "active_cell"),
        Output("store-numero-ind-modal-aprendizaje", "data"),
        Output("alerta-doc-modal-aprendizaje", "children"),
        Input("tabla-aprendizaje", "active_cell"),
        Input("btn-cerrar-modal-aprendizaje", "n_clicks"),
        Input("btn-entendido-modal-aprendizaje", "n_clicks"),
        Input("seccion-actual", "data"),
        State("tabla-aprendizaje", "data"),
        prevent_initial_call=True,
    )
    def controlar_modal_aprendizaje(active_cell, n_close_x, n_close_btn, seccion_actual, data_tabla):
        if seccion_actual is not None and seccion_actual != "aprendizaje_evaluacion":
            return {"display": "none"}, "", "", None, None, ""

        ctx_id = dash.ctx.triggered_id

        # Si se hace clic en alguno de los botones de cerrar
        if ctx_id in ("btn-cerrar-modal-aprendizaje", "btn-entendido-modal-aprendizaje"):
            return {"display": "none"}, "", "", None, None, ""

        # Si el disparador fue la tabla y hay una celda seleccionada
        if ctx_id == "tabla-aprendizaje" and active_cell is not None and data_tabla:
            row_idx = active_cell.get("row")
            if row_idx is not None and 0 <= row_idx < len(data_tabla):
                nombre_indicador_raw = data_tabla[row_idx].get("nombre_indicador")
                if nombre_indicador_raw:
                    nombre_indicador = str(nombre_indicador_raw).replace("👁️", "").replace("👁", "").strip()
                    df_ind = resultados_completos[
                        (resultados_completos["agrupador"] == "Aprendizaje y Evaluacion") &
                        (resultados_completos["nombre indicador"] == nombre_indicador)
                    ]
                    if not df_ind.empty:
                        fila = df_ind.iloc[0]
                        responsable = fila.get("responsable")
                        tiempo_reporte = fila.get("tiempo de reporte")
                        formula = fila.get("formula de calculo")
                        numero_ind = fila.get("numero_ind")
                    else:
                        responsable = None
                        tiempo_reporte = None
                        formula = None
                        numero_ind = None

                    cuerpo = generar_cuerpo_modal(
                        campo1_val=responsable,
                        campo2_val=tiempo_reporte,
                        formula=formula,
                        label1="Responsable",
                        label2="Tiempo de Reporte",
                        numero_ind=numero_ind,
                    )
                    return {"display": "flex"}, nombre_indicador, cuerpo, no_update, numero_ind, ""

        # Si se disparó pero active_cell es None (tras haber sido limpiado), no hacer nada
        if active_cell is None:
            return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

        return {"display": "none"}, "", "", None, None, ""

    # ==========================================================================
    # Callback para Descargar Documentos SGC o Estratégico desde el Modal
    # ==========================================================================
    @app.callback(
        Output("download-modal-aprendizaje", "data"),
        Output("alerta-doc-modal-aprendizaje", "children", allow_duplicate=True),
        Input("btn-descargar-sgc-aprendizaje", "n_clicks"),
        Input("btn-descargar-estrategico-aprendizaje", "n_clicks"),
        State("store-numero-ind-modal-aprendizaje", "data"),
        prevent_initial_call=True,
    )
    def descargar_documento_modal_aprendizaje(n_sgc, n_estrategico, numero_ind):
        trigger = ctx.triggered_id

        if not trigger:
            return no_update, no_update

        if not numero_ind:
            return (
                no_update,
                html.Span(
                    "⚠️ Este indicador no tiene un código de indicador asignado.",
                    style={"color": "#d97706", "fontSize": "12px", "fontWeight": "600"},
                ),
            )

        tipo = "SGC" if trigger == "btn-descargar-sgc-aprendizaje" else "Estrategicos"
        label_tipo = "SGC" if tipo == "SGC" else "Estratégico"

        try:
            contenido_bytes, nombre_archivo = obtener_documento_por_indicador(
                numero_ind=numero_ind,
                tipo=tipo,
                categoria="aprendizaje_evaluacion",
            )

            if not contenido_bytes:
                return (
                    no_update,
                    html.Span(
                        f"⚠️ No se encontró documento de tipo '{label_tipo}' para el indicador {numero_ind}.",
                        style={"color": "#d97706", "fontSize": "12px", "fontWeight": "600"},
                    ),
                )

            return (
                dcc.send_bytes(lambda buffer: buffer.write(contenido_bytes), nombre_archivo),
                html.Span(
                    f"✓ Descargando '{nombre_archivo}'...",
                    style={"color": "#16a34a", "fontSize": "12px", "fontWeight": "600"},
                ),
            )

        except Exception as e:
            return (
                no_update,
                html.Span(
                    f"❌ Error al descargar documento: {str(e)}",
                    style={"color": "#dc2626", "fontSize": "12px", "fontWeight": "600"},
                ),
            )
