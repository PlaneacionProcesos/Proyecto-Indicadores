from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div(
    [
        # HEADER
        html.Div(className="header", children=[html.H1("Indicadores")]),
        # CONTENEDOR PRINCIPAL
        html.Div(
            className="contenedor",
            children=[
                # SEGMENTADORES
                html.Div(
                    className="segmentadores",
                    children=[
                        html.H3("Filtros"),
                        html.Label("Producto"),
                        dcc.Dropdown(
                            id="filtro-producto",
                            options=[
                                {"label": "Todos", "value": "Todos"},
                                {"label": "Producto A", "value": "A"},
                                {"label": "Producto B", "value": "B"},
                            ],
                            value="Todos",
                        ),
                        html.Br(),
                        html.Label("Mes"),
                        dcc.Dropdown(
                            id="filtro-mes",
                            options=[
                                {"label": "Todos", "value": "Todos"},
                                {"label": "Enero", "value": "Enero"},
                                {"label": "Febrero", "value": "Febrero"},
                            ],
                            value="Todos",
                        ),
                    ],
                ),
                # GRÁFICAS
                html.Div(
                    className="graficas",
                    children=[
                        # TARJETAS
                        html.Div(
                            className="tarjetas",
                            children=[
                                html.Div(
                                    className="tarjeta",
                                    id="tarjeta1",
                                    children=[
                                        html.P("Inicadores de ventas"),
                                        html.H2(id="kpi-ventas"),
                                    ],
                                ),
                                html.Div(
                                    className="tarjeta",
                                    id="tarjeta2",
                                    children=[
                                        html.P("Promedio de ventas"),
                                        html.H2(id="kpi-promedios"),
                                    ],
                                ),
                                html.Div(
                                    className="tarjeta",
                                    id="tarjeta3",
                                    children=[
                                        html.P("Cantidad de registros"),
                                        html.H2(id="kpi-registros"),
                                    ],
                                ),
                                html.Div(
                                    className="tarjeta",
                                    id="tarjeta4",
                                    children=[
                                        html.P("Venta maximas"),
                                        html.H2(id="kpi-maximos"),
                                    ],
                                ),
                            ],
                        ),
                        # VISUALIZACIONES
                        html.Div(
                            className="visualizaciones",
                            children=[
                                html.Div(
                                    className="pastel",
                                    children=[dcc.Graph(id="grafico-pastel")],
                                ),
                                html.Div(
                                    className="barras",
                                    children=[dcc.Graph(id="grafico-barras")],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ]
)

from callbacks import *

if __name__ == "__main__":
    app.run(debug=True)
