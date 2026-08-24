from dash import dash_table
from configuraciones.colors import *


def tabla_aprendizaje():

    return dash_table.DataTable(
        id="tabla-agrupadores",
        columns=[
            {
                "name": "2024",
                "id": "año-2024",
            },
            {
                "name": "2025",
                "id": "año-2025",
            },
            {
                "name": "2026",
                "id": "año-2026",
            },
        ],
        data=[],
        style_table={
            "width": "100%",
            "overflowX": "auto",
            "border-radius": "15px",
        },
        style_cell={
            "fontFamily": "Arial",
            "fontSize": "13px",
            "padding": "12px",
            "textAlign": "left",
            "whiteSpace": "normal",
            "height": "auto",
        },
        style_header={
            "backgroundColor": COLOR_TABLA_ENCA,
            "color": COLOR_PRIMARIO,
            "fontWeight": "bold",
            "textAlign": "center",
        },
        style_data={
            "backgroundColor": COLOR_BLANCO,
            "color": "#1f2937",
            "textAlign": "center",
        },
    )
