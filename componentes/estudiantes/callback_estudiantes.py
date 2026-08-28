import dash
from dash import Input, Output, State, ctx, html, no_update
from datos import resultados_completos
import pandas as pd


def generar_tarjetas_contexto_estudiantes(datos_seccion, indicador_seleccionado=None):
    """
    Genera tarjetas interactivas de contexto para cada indicador del agrupador Estudiantes.
    Si un indicador fue clickeado en la tabla (indicador_seleccionado),
    su tarjeta se colorea/resalta y se abre automáticamente.
    """
    if datos_seccion.empty:
        return html.Div(
            "No se encontraron indicadores disponibles con los filtros seleccionados.",
            className="sin-indicadores-contexto",
        )

    pares_indicadores = datos_seccion[["numero_ind", "nombre indicador"]].drop_duplicates()
    tarjetas = []

    for _, par in pares_indicadores.iterrows():
        cod_ind = par["numero_ind"]
        nombre = par["nombre indicador"]

        df_ind = datos_seccion[datos_seccion["numero_ind"] == cod_ind]
        if df_ind.empty:
            continue
        fila = df_ind.iloc[0]

        # 1. Nombre Indicador
        nombre_str = (
            str(nombre).strip()
            if pd.notna(nombre) and str(nombre).strip() != "" and str(nombre).strip().lower() != "nan"
            else str(cod_ind)
        )

        # 2. Proceso
        proceso = fila.get("proceso")
        proceso_str = (
            str(proceso).strip()
            if pd.notna(proceso) and str(proceso).strip() != "" and str(proceso).strip().lower() != "nan"
            else "No especificado"
        )

        # 3. Macroproceso
        macroproceso = fila.get("macroproceso")
        macro_str = (
            str(macroproceso).strip()
            if pd.notna(macroproceso) and str(macroproceso).strip() != "" and str(macroproceso).strip().lower() != "nan"
            else "No especificado"
        )

        # 4. Formula de Calculo
        formula = fila.get("formula de calculo")
        formula_str = (
            str(formula).strip()
            if pd.notna(formula) and str(formula).strip() != "" and str(formula).strip().lower() != "nan"
            else "Registro directo / No especificada"
        )

        # Determinar si esta tarjeta es la seleccionada desde la tabla (por nombre o por código)
        es_seleccionada = (
            indicador_seleccionado is not None
            and (
                str(nombre_str).strip().lower() == str(indicador_seleccionado).strip().lower()
                or str(cod_ind).strip().lower() == str(indicador_seleccionado).strip().lower()
            )
        )

        clases_tarjeta = "tarjeta-indicador-contexto"
        if es_seleccionada:
            clases_tarjeta += " tarjeta-activa-seleccionada"

        if es_seleccionada:
            texto_btn = "Seleccionado en tabla"
            flecha_btn = " ▴"
        else:
            texto_btn = "Ver detalles"
            flecha_btn = " ▾"

        cod_ind_str = (
            str(cod_ind).strip()
            if pd.notna(cod_ind) and str(cod_ind).strip() != "" and str(cod_ind).strip().lower() != "nan"
            else "No especificado"
        )

        tarjeta = html.Details(
            className=clases_tarjeta,
            open=es_seleccionada,
            children=[
                html.Summary(
                    className="tarjeta-summary",
                    children=[
                        html.Div(
                            className="tarjeta-summary-izq",
                            children=[
                                html.Span(cod_ind_str, className="badge-codigo-indicador"),
                                html.Span(nombre_str, className="nombre-resumen-indicador"),
                            ],
                        ),
                        html.Span(
                            className="btn-ver-detalle-tag",
                            children=[
                                html.Span(texto_btn, className="texto-btn-detalle"),
                                html.Span(flecha_btn, className="flecha-btn-detalle"),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="tarjeta-cuerpo-detalle",
                    children=[
                        html.Div(
                            className="item-detalle-contexto",
                            children=[
                                html.Span("Código Indicador", className="label-detalle-contexto"),
                                html.Span(cod_ind_str, className="valor-detalle-contexto valor-nombre"),
                            ],
                        ),
                        html.Div(
                            className="item-detalle-contexto",
                            children=[
                                html.Span("Proceso", className="label-detalle-contexto"),
                                html.Span(proceso_str, className="valor-detalle-contexto"),
                            ],
                        ),
                        html.Div(
                            className="item-detalle-contexto",
                            children=[
                                html.Span("Macroproceso", className="label-detalle-contexto"),
                                html.Span(macro_str, className="valor-detalle-contexto"),
                            ],
                        ),
                        html.Div(
                            className="item-detalle-contexto item-formula",
                            children=[
                                html.Span("Fórmula de Cálculo", className="label-detalle-contexto"),
                                html.Div(formula_str, className="valor-detalle-contexto valor-formula"),
                            ],
                        ),
                    ],
                ),
            ],
        )
        tarjetas.append(tarjeta)

    return tarjetas


def registrar_callback_estudiantes(app):

    # ==========================================================================
    # Callback Unificado de Alto Rendimiento (Tabla + Tarjetas de Estudiantes)
    # ==========================================================================
    @app.callback(
        Output("tabla-estudiantes", "data"),
        Output("tarjetas-contexto-estudiantes", "children"),
        Input("filtro-año", "value"),
        Input("filtro-centro", "value"),
        Input("filtro-periodo", "value"),
        Input("filtro-nivel", "value"),
        Input("filtro-modalidad", "value"),
        Input("filtro-tipo", "value"),
        Input("filtro-tiempo-reporte", "value"),
        Input("tabla-estudiantes", "active_cell"),
        Input("seccion-actual", "data"),
        dash.State("tabla-estudiantes", "data"),
    )
    def datos_y_tarjetas_estudiantes(
        año, centro, periodo, nivel, modalidad, tipo, tiempo_reporte,
        active_cell, seccion_actual, data_tabla_actual
    ):
        # 1. Guard de Sección
        if seccion_actual is not None and seccion_actual != "estudiantes":
            return dash.no_update, dash.no_update

        # 2. Filtrar DataFrame del agrupador
        datos_ae = resultados_completos[
            resultados_completos["agrupador"] == "Estudiantes"
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

        # 3. Optimización de clic en celda activa
        disparador = dash.ctx.triggered_id
        if disparador == "tabla-estudiantes" and data_tabla_actual:
            indicador_sel = None
            if active_cell is not None:
                row_idx = active_cell.get("row")
                if row_idx is not None and 0 <= row_idx < len(data_tabla_actual):
                    indicador_sel = data_tabla_actual[row_idx].get("nombre_indicador")
            return dash.no_update, generar_tarjetas_contexto_estudiantes(datos_ae, indicador_seleccionado=indicador_sel)

        # 4. Procesar datos para la tabla
        if datos_ae.empty:
            df_resultado = pd.DataFrame(
                columns=[
                    "nombre_indicador",
                    "año-2024",
                    "año-2025",
                    "año-2026",
                    "variacion-ultimos_dos",
                    "porcentaje_variacion",
                ]
            )
            return df_resultado.to_dict("records"), generar_tarjetas_contexto_estudiantes(datos_ae)

        indicadores = datos_ae["nombre indicador"].drop_duplicates()
        df_resultado = pd.DataFrame({"nombre_indicador": indicadores})

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

        val_2024 = df_resultado["nombre_indicador"].map(serie_2024)
        val_2025 = df_resultado["nombre_indicador"].map(serie_2025)
        val_2026 = df_resultado["nombre_indicador"].map(serie_2026)

        df_resultado["año-2024"] = val_2024.apply(
            lambda x: round(x, 2) if pd.notna(x) else "Sin datos"
        )
        df_resultado["año-2025"] = val_2025.apply(
            lambda x: round(x, 2) if pd.notna(x) else "Sin datos"
        )
        df_resultado["año-2026"] = val_2026.apply(
            lambda x: round(x, 2) if pd.notna(x) else "Sin datos"
        )

        def calcular_variacion_absoluta(v_actual, v_anterior):
            if pd.notna(v_actual) and pd.notna(v_anterior):
                diff = v_actual - v_anterior
                return round(diff, 2)
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

        records = df_resultado.to_dict("records")

        indicador_seleccionado = None
        if active_cell is not None:
            row_idx = active_cell.get("row")
            if row_idx is not None and 0 <= row_idx < len(records):
                indicador_seleccionado = records[row_idx].get("nombre_indicador")

        tarjetas_ui = generar_tarjetas_contexto_estudiantes(datos_ae, indicador_seleccionado=indicador_seleccionado)

        return records, tarjetas_ui