from dash import dash_table
from configuraciones.colors import (
    COLOR_TABLA_ENCA,
    COLOR_BLANCO,
    COLOR_PRIMARIO,
)

# ==============================================================================
# CONFIGURACIÓN DE COLORES DE CABECERA POR COLUMNA
# ==============================================================================
# Define aquí el color de fondo y de texto específico para cada columna:
COLORES_CABECERA = {
    "nombre_indicador": {
        "fondo": "#002060",  
        "texto": "#FFFFFF",  
    },
    "año-2024": {
        "fondo": "#D86ECC",  
        "texto": "#FFFFFF",
    },
    "año-2025": {
        "fondo": "#FFC000",  
        "texto": "#FFFFFF",
    },
    "año-2026": {
        "fondo": "#47D45A",  
        "texto": "#FFFFFF",
    },
    "variacion-ultimos_dos": {
        "fondo": "#002060", 
        "texto": "#FFFFFF",
    },
    "porcentaje_variacion": {
        "fondo": "#002060",  
        "texto": "#FFFFFF",
    },
}


def tabla_siac():

    # Genera la configuración condicional para aplicar los colores específicos
    style_header_conditional = [
        {
            "if": {"column_id": col_id},
            "backgroundColor": config["fondo"],
            "color": config["texto"],
        }
        for col_id, config in COLORES_CABECERA.items()
    ]

    return dash_table.DataTable(
        id="tabla-siac",
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
