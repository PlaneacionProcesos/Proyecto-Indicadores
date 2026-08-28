from dash import Input, Output, html
from datos import resultados_completos
import pandas as pd


def generar_tarjetas_contexto_aprendizaje(datos_seccion):
    """
    Genera tarjetas interactivas de contexto para cada indicador del agrupador.
    Muestra:
      - Nombre indicador
      - Proceso
      - Macroproceso
      - Formula de calculo
    """
    if datos_seccion.empty:
        return html.Div(
            "No se encontraron indicadores disponibles con los filtros seleccionados.",
            className="sin-indicadores-contexto",
        )

    indicadores_unicos = datos_seccion["numero_ind"].drop_duplicates()
    tarjetas = []

    for cod_ind in indicadores_unicos:
        df_ind = datos_seccion[datos_seccion["numero_ind"] == cod_ind]
        if df_ind.empty:
            continue
        fila = df_ind.iloc[0]

        # 1. Nombre Indicador
        nombre = fila.get("nombre indicador")
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

        tarjeta = html.Details(
            className="tarjeta-indicador-contexto",
            children=[
                html.Summary(
                    className="tarjeta-summary",
                    children=[
                        html.Div(
                            className="tarjeta-summary-izq",
                            children=[
                                html.Span(str(cod_ind), className="badge-codigo-indicador"),
                                html.Span(nombre_str, className="nombre-resumen-indicador"),
                            ],
                        ),
                        html.Span(
                            className="btn-ver-detalle-tag",
                            children=[
                                html.Span("Ver detalles", className="texto-btn-detalle"),
                                html.Span(" ▾", className="flecha-btn-detalle"),
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
                                html.Span("Nombre Indicador", className="label-detalle-contexto"),
                                html.Span(nombre_str, className="valor-detalle-contexto valor-nombre"),
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


def registrar_callback_aprendizaje(app):

    @app.callback(
        Output("tabla-aprendizaje", "data"),
        Output("tarjetas-contexto-aprendizaje", "children"),
        Input("filtro-año", "value"),
        Input("filtro-centro", "value"),
        Input("filtro-periodo", "value"),
        Input("filtro-nivel", "value"),
        Input("filtro-modalidad", "value"),
        Input("filtro-tipo", "value"),
        Input("filtro-tiempo-reporte", "value"),
    )
    def datos_tabla(año, centro, periodo, nivel, modalidad, tipo, tiempo_reporte):

        # --------------------------------------------------------------------------
        # 1. Filtrar primero por el agrupador de la sección
        # --------------------------------------------------------------------------
        datos_ae = resultados_completos[
            resultados_completos["agrupador"] == "Aprendizaje y Evaluacion"
        ].copy()

        # --------------------------------------------------------------------------
        # 2. Aplicar Filtros sobre el agrupador
        # --------------------------------------------------------------------------
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

        # --------------------------------------------------------------------------
        # 3. Procesar datos para la tabla
        # --------------------------------------------------------------------------
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
            return df_resultado.to_dict("records"),generar_tarjetas_contexto_aprendizaje(datos_ae)

        # Indicadores únicos del agrupador
        indicadores = datos_ae["numero_ind"].drop_duplicates()

        # Crear una fila por indicador
        df_resultado = pd.DataFrame({"nombre_indicador": indicadores})

        # =========================
        # DATOS NUMÉRICOS POR AÑO
        # =========================
        serie_2024 = (
            datos_ae[datos_ae["ano"] == 2024]
            .dropna(subset=["resultado"])
            .groupby("numero_ind")["resultado"]
            .mean()
        )

        serie_2025 = (
            datos_ae[datos_ae["ano"] == 2025]
            .dropna(subset=["resultado"])
            .groupby("numero_ind")["resultado"]
            .mean()
        )

        serie_2026 = (
            datos_ae[datos_ae["ano"] == 2026]
            .dropna(subset=["resultado"])
            .groupby("numero_ind")["resultado"]
            .mean()
        )

        # Mapear valores numéricos
        val_2024 = df_resultado["nombre_indicador"].map(serie_2024)
        val_2025 = df_resultado["nombre_indicador"].map(serie_2025)
        val_2026 = df_resultado["nombre_indicador"].map(serie_2026)

        # =========================
        # COLUMNAS POR AÑO
        # =========================
        df_resultado["año-2024"] = val_2024.apply(
            lambda x: round(x, 2) if pd.notna(x) else "Sin datos"
        )
        df_resultado["año-2025"] = val_2025.apply(
            lambda x: round(x, 2) if pd.notna(x) else "Sin datos"
        )
        df_resultado["año-2026"] = val_2026.apply(
            lambda x: round(x, 2) if pd.notna(x) else "Sin datos"
        )

        # =========================
        # VARIACIÓN ABSOLUTA Y PORCENTUAL (2026 vs 2025)
        # =========================
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
            calcular_variacion_absoluta(a, b) for a, b in zip(val_2026, val_2025)
        ]

        df_resultado["porcentaje_variacion"] = [
            calcular_variacion_porcentual(a, b) for a, b in zip(val_2026, val_2025)
        ]

        tarjetas_ui = generar_tarjetas_contexto_aprendizaje(datos_ae)

        return df_resultado.to_dict("records"), tarjetas_ui
