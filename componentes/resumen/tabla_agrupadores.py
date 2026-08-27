from dash import dash_table
from configuraciones.colors import COLOR_BLANCO


COLORES_CABECERA = {
    "agrupador": {
        "fondo": "#002060",
        "texto": "#FFFFFF",
    },
    "descripcion": {
        "fondo": "#002060",
        "texto": "#FFFFFF",
    },
    "total_indicadores": {
        "fondo": "#002060",
        "texto": "#FFFFFF",
    },
}


def tabla_agrupadores():

    style_header_conditional = [
        {
            "if": {"column_id": col_id},
            "backgroundColor": config["fondo"],
            "color": config["texto"],
        }
        for col_id, config in COLORES_CABECERA.items()
    ]

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
            "fontWeight": "bold",
            "fontSize": "13px",
            "textAlign": "center",
            "padding": "12px 10px",
        },
        style_header_conditional=style_header_conditional,
        style_data={
            "backgroundColor": COLOR_BLANCO,
            "color": "#1f2937",
            "textAlign": "center",
        },
    )