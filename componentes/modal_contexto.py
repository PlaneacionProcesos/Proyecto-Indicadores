from dash import html
import pandas as pd


def banner_ayuda_tabla():
    """
    Banner visual que indica claramente al usuario que las filas de la tabla
    son interactivas y abren la Ficha Técnica al hacer clic.
    """
    return html.Div(
        className="banner-ayuda-tabla",
        children=[
            html.Span("💡", className="icono-ayuda-tabla"),
            html.Span(
                [
                    "Haz clic en cualquier ",
                    html.Strong("nombre de indicador", className="texto-ayuda-destacado"),
                    " en la tabla para abrir instantáneamente su Ficha Técnica y Metodología en pantalla.",
                ],
                className="texto-ayuda-tabla",
            ),
        ],
    )


def layout_modal_contexto(seccion_id):
    """
    Estructura del Modal emergente centrado para la sección indicada.
    """
    return html.Div(
        id=f"modal-contexto-{seccion_id}",
        className="modal-contexto-overlay",
        style={"display": "none"},
        children=[
            html.Div(
                className="modal-contexto-card",
                children=[
                    html.Div(
                        className="modal-contexto-header",
                        children=[
                            html.Div(
                                className="modal-contexto-header-texto",
                                children=[
                                    html.Span(
                                        "FICHA TÉCNICA Y METODOLOGÍA",
                                        className="modal-contexto-tag",
                                    ),
                                    html.H3(
                                        id=f"modal-titulo-{seccion_id}",
                                        className="modal-contexto-titulo",
                                    ),
                                ],
                            ),
                            html.Button(
                                "✕",
                                id=f"btn-cerrar-modal-{seccion_id}",
                                className="btn-cerrar-modal-contexto",
                                n_clicks=0,
                            ),
                        ],
                    ),
                    html.Div(
                        id=f"modal-cuerpo-{seccion_id}",
                        className="modal-contexto-cuerpo",
                    ),
                    html.Div(
                        className="modal-contexto-footer",
                        children=[
                            html.Button(
                                "Entendido / Cerrar",
                                id=f"btn-entendido-modal-{seccion_id}",
                                className="btn-entendido-modal",
                                n_clicks=0,
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )


def generar_cuerpo_modal(macroproceso, proceso, formula):
    """
    Construye la UI del cuerpo del modal con diseño limpio.
    """
    macro_str = (
        str(macroproceso).strip()
        if pd.notna(macroproceso) and str(macroproceso).strip() != "" and str(macroproceso).strip().lower() != "nan"
        else "No especificado"
    )
    proceso_str = (
        str(proceso).strip()
        if pd.notna(proceso) and str(proceso).strip() != "" and str(proceso).strip().lower() != "nan"
        else "No especificado"
    )
    formula_str = (
        str(formula).strip()
        if pd.notna(formula) and str(formula).strip() != "" and str(formula).strip().lower() != "nan"
        else "Registro directo / No especificada"
    )

    return html.Div(
        className="modal-cuerpo-grid",
        children=[
            html.Div(
                className="modal-campo-grupo",
                children=[
                    html.Span("Macroproceso", className="modal-campo-label"),
                    html.Span(macro_str, className="modal-campo-valor"),
                ],
            ),
            html.Div(
                className="modal-campo-grupo",
                children=[
                    html.Span("Proceso", className="modal-campo-label"),
                    html.Span(proceso_str, className="modal-campo-valor"),
                ],
            ),
            html.Div(
                className="modal-campo-grupo modal-campo-full",
                children=[
                    html.Span("Fórmula de Cálculo / Metodología", className="modal-campo-label"),
                    html.Div(formula_str, className="modal-campo-formula-box"),
                ],
            ),
        ],
    )


def generar_tarjeta_contexto_abierta(nombre_str, macro_str, proceso_str, formula_str, es_seleccionada=False):
    """
    Genera una tarjeta de contexto abierta por defecto (sin necesidad de desplegar),
    resaltando la tarjeta si es_seleccionada es True.
    """
    clases_tarjeta = "tarjeta-indicador-contexto"
    if es_seleccionada:
        clases_tarjeta += " tarjeta-activa-seleccionada"

    badge_sel = (
        html.Span("Seleccionado en tabla", className="badge-seleccionado-tabla")
        if es_seleccionada
        else None
    )

    return html.Div(
        className=clases_tarjeta,
        children=[
            html.Div(
                className="tarjeta-header-abierta",
                children=[
                    html.H4(nombre_str, className="tarjeta-titulo-indicador"),
                    badge_sel,
                ],
            ),
            html.Div(
                className="tarjeta-cuerpo-detalle",
                children=[
                    html.Div(
                        className="item-detalle-contexto",
                        children=[
                            html.Span("Macroproceso", className="label-detalle-contexto"),
                            html.Span(macro_str, className="valor-detalle-contexto"),
                        ],
                    ),
                    html.Div(
                        className="item-detalle-contexto",
                        children=[
                            html.Span("Proceso", className="label-detalle-contexto"),
                            html.Span(proceso_str, className="valor-detalle-contexto"),
                        ],
                    ),
                    html.Div(
                        className="item-detalle-contexto item-formula",
                        children=[
                            html.Span("Fórmula de Cálculo / Metodología", className="label-detalle-contexto"),
                            html.Div(formula_str, className="valor-detalle-contexto valor-formula"),
                        ],
                    ),
                ],
            ),
        ],
    )


