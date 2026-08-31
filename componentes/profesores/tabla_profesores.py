from dash import dash_table
from configuraciones.colors import (
    COLOR_TABLA_ENCA,
    COLOR_BLANCO,
    COLOR_PRIMARIO,
)

# ==============================================================================
# CONFIGURACIÓN DE COLORES DE CABECERA POR COLUMNA
# ==============================================================================

VARIACION = "2025-2026"


COLORES_CABECERA = {
    "nombre_indicador": {
        "fondo": "#002060",
        "texto": "#FFFFFF",
    },
    "año-2023": {
        "fondo": "#6ED8D8",
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


def tabla_profesores():

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
        id="tabla-profesores",
        columns=[
            {"name": "Indicador", "id": "nombre_indicador"},
            {
                "name": "2023",
                "id": "año-2023",
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
            {"name": f"Variacion ({VARIACION})", "id": "variacion-ultimos_dos"},
            {"name": "%", "id": "porcentaje_variacion"},
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
            "cursor": "pointer",
            "overflow": "hidden",
            "textOverflow": "ellipsis",
        },
        style_cell_conditional=[
            {
                "if": {"column_id": "nombre_indicador"},
                "width": "45%",
                "minWidth": "240px",
                "textAlign": "left",
                "fontWeight": "600",
            },
            {
                "if": {"column_id": "año-2023"},
                "width": "11%",
                "minWidth": "80px",
                "textAlign": "center",
            },
            {
                "if": {"column_id": "año-2024"},
                "width": "11%",
                "minWidth": "80px",
                "textAlign": "center",
            },
            {
                "if": {"column_id": "año-2025"},
                "width": "11%",
                "minWidth": "80px",
                "textAlign": "center",
            },
            {
                "if": {"column_id": "año-2026"},
                "width": "11%",
                "minWidth": "80px",
                "textAlign": "center",
            },
            {
                "if": {"column_id": "variacion-ultimos_dos"},
                "width": "11%",
                "minWidth": "90px",
                "textAlign": "center",
            },
            {
                "if": {"column_id": "porcentaje_variacion"},
                "width": "11%",
                "minWidth": "80px",
                "textAlign": "center",
            },
        ],
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
        style_data_conditional=[
            {
                "if": {"state": "active"},
                "backgroundColor": "rgba(71, 212, 90, 0.22) !important",
                "border": "1px solid #002e6d !important",
                "fontWeight": "bold",
            },
            {
                "if": {"state": "selected"},
                "backgroundColor": "rgba(71, 212, 90, 0.15) !important",
            },
        ],
    )
