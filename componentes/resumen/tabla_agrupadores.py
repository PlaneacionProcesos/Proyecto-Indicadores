from dash import dash_table

from configuraciones.colors import (
    COLOR_TABLA_ENCA,
    COLOR_BLANCO,
    COLOR_PRIMARIO,
)


def tabla_agrupadores():

    return dash_table.DataTable(

        id="tabla-agrupadores",

        columns=[
            {
                "name": "Agrupador",
                "id": "agrupador",
            },
            {
                "name": "Descripción",
                "id": "descripcion",
            },
            {
                "name": "Total de indicadores",
                "id": "total_indicadores",
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