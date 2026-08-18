from dash import Input, Output
from app import app
from datos import df
import plotly.express as px


@app.callback(
    Output("kpi-ventas", "children"),
    Output("kpi-promedios", "children"),
    Output("kpi-registros", "children"),
    Output("kpi-maximos", "children"),
    Input("filtro-producto", "value"),
    Input("filtro-mes", "value"),
)
def actualizar_kpis(producto, mes):

    # Copiamos el DataFrame
    datos_filtrados = df.copy()

    if producto == None and mes == None:
        return (
            "Selecciona un valor",
            "Selecciona un valor",
            "Selecciona un valor",
            "Selecciona un valor",
        )
    elif producto == None:
        return (
            "Selecciona un valor para producto",
            "Selecciona un valor para producto",
            "Selecciona un valor para producto",
            "Selecciona un valor para producto",
        )
    elif mes == None:
        return (
            "Selecciona un valor para mes",
            "Selecciona un valor para mes",
            "Selecciona un valor para mes",
            "Selecciona un valor para mes",
        )

    # Filtro producto
    if producto != "Todos":
        datos_filtrados = datos_filtrados[datos_filtrados["producto"] == producto]

    # Filtro mes
    if mes != "Todos":
        datos_filtrados = datos_filtrados[datos_filtrados["mes"] == mes]

    # -------------------------
    # KPIs
    # -------------------------

    # Ventas totales
    ventas_totales = datos_filtrados["ventas"].sum()

    # Promedio
    ventas_promedio = datos_filtrados["ventas"].mean()

    # Cantidad de registros
    cantidad_registros = len(datos_filtrados)

    # Venta máxima
    venta_maxima = datos_filtrados["ventas"].max()

    # -------------------------
    # Formatear valores
    # -------------------------

    kpi_ventas = f"${ventas_totales:,.0f}"

    kpi_promedios = f"${ventas_promedio:,.2f}"

    kpi_registros = f"{cantidad_registros:,}"

    kpi_maximos = f"${venta_maxima:,.0f}"

    return (
        kpi_ventas,
        kpi_promedios,
        kpi_registros,
        kpi_maximos,
    )


# -------------------------
# Graficas
# -------------------------



@app.callback(
    Output("grafico-pastel", "figure"),
    Output("grafico-barras", "figure"),
    Input("filtro-producto", "value"),
    Input("filtro-mes", "value"),
)
def actualizar_graficas(producto, mes):

    # Copiamos el DataFrame
    datos_filtrados = df.copy()

    # -------------------------
    # FILTRO PRODUCTO
    # -------------------------

    if producto != "Todos":
        datos_filtrados = datos_filtrados[
            datos_filtrados["producto"] == producto
        ]

    # -------------------------
    # FILTRO MES
    # -------------------------

    if mes != "Todos":
        datos_filtrados = datos_filtrados[
            datos_filtrados["mes"] == mes
        ]

    # -------------------------
    # GRÁFICO DE PASTEL
    # -------------------------

    grafico_pastel = px.pie(
        datos_filtrados,
        names="producto",
        values="ventas",
        title="Distribución de ventas por producto",
    )
    
    grafico_pastel.update_layout(
        font=dict(
            family="Arial",
            color="#080b0d"
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30
        ),
    )

    # -------------------------
    # GRÁFICO DE BARRAS
    # -------------------------

    grafico_barras = px.bar(
        datos_filtrados,
        x="producto",
        y="ventas",
        title="Ventas por producto",
    )
    
    grafico_barras.update_layout(
        font=dict(
            family="Arial",
            color="#080b0d"
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30
        )
    )
    
    return grafico_pastel, grafico_barras
