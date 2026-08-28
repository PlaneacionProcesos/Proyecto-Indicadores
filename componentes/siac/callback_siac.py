from dash import Input, Output, html
from datos import resultados_completos
import pandas as pd


def registrar_callback_siac(app):

    @app.callback(
        Output("tabla-siac", "data"),
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
            resultados_completos["agrupador"] == "SIAC - Rendicion de Cuentas"
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
            return df_resultado.to_dict("records")

        # Indicadores únicos del agrupador
        indicadores = datos_ae["numero_ind"].drop_duplicates()

        # Crear una fila por indicador
        df_resultado = pd.DataFrame({
            "nombre_indicador": indicadores
        })

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
            calcular_variacion_absoluta(a, b)
            for a, b in zip(val_2026, val_2025)
        ]

        df_resultado["porcentaje_variacion"] = [
            calcular_variacion_porcentual(a, b)
            for a, b in zip(val_2026, val_2025)
        ]

        return df_resultado.to_dict("records")