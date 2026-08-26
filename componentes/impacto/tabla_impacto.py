from dash import dash_table
from configuraciones.colors import (
    COLOR_TABLA_ENCA,
    COLOR_BLANCO,
    COLOR_PRIMARIO,
)

def tabla_impacto():

    return dash_table.DataTable(
        id="tabla-impacto",
        columns=[
            {
                "name": "Indicador",
                "id": "nombre_indicador"
            },
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
            {
                "name": "Variación",
                "id": "variacion-ultimos_dos"
            },
            {
                "name": "%",
                "id": "porcentaje_variacion"
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
