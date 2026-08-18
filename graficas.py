from datos import ventas_mes, ventas_productos
import plotly.express as px


def barras_mes():
    datos = ventas_mes()

    fig = px.bar(
        datos,
        x="mes",
        y="ventas",
        title="Ventas por mes"
    )

    return fig


def barras_producto():
    datos = ventas_productos()

    fig = px.bar(
        datos,
        x="producto",
        y="ventas",
        title="Ventas por producto"
    )

    return fig