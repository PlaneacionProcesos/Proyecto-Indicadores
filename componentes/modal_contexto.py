from dash import html, dcc
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
                    html.Strong("nombre de indicador 👁️", className="texto-ayuda-destacado"),
                    " en la tabla para abrir instantáneamente su Ficha Técnica y Metodología en pantalla.",
                ],
                className="texto-ayuda-tabla",
            ),
        ],
    )


def layout_modal_contexto(seccion_id):
    """
    Estructura del Modal emergente centrado para la sección indicada,
    incluyendo botones para descargar documentos SGC y Estratégicos.
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
                    # Footer con los 2 botones SGC y Estratégico + botón Cerrar
                    html.Div(
                        className="modal-contexto-footer",
                        children=[
                            html.Div(
                                className="modal-descargas-contenedor",
                                children=[
                                    html.Span("Documentos asociados:", className="modal-descargas-titulo"),
                                    html.Div(
                                        className="modal-botones-doc-grupo",
                                        children=[
                                            html.Button(
                                                [
                                                    html.Span("📄", style={"marginRight": "5px"}),
                                                    "SGC",
                                                ],
                                                id=f"btn-descargar-sgc-{seccion_id}",
                                                className="btn-modal-doc btn-modal-sgc",
                                                n_clicks=0,
                                                title="Descargar documento SGC de este indicador",
                                            ),
                                            html.Button(
                                                [
                                                    html.Span("📊", style={"marginRight": "5px"}),
                                                    "Estratégico",
                                                ],
                                                id=f"btn-descargar-estrategico-{seccion_id}",
                                                className="btn-modal-doc btn-modal-estrategico",
                                                n_clicks=0,
                                                title="Descargar documento Estratégico de este indicador",
                                            ),
                                        ],
                                    ),
                                    html.Div(id=f"alerta-doc-modal-{seccion_id}", className="modal-alerta-doc"),
                                ],
                            ),
                            html.Button(
                                "Entendido / Cerrar",
                                id=f"btn-entendido-modal-{seccion_id}",
                                className="btn-entendido-modal",
                                n_clicks=0,
                            ),
                            dcc.Download(id=f"download-modal-{seccion_id}"),
                            dcc.Store(id=f"store-numero-ind-modal-{seccion_id}"),
                        ],
                    ),
                ],
            ),
        ],
    )



def generar_cuerpo_modal(
    campo1_val=None,
    campo2_val=None,
    formula=None,
    label1="Responsable",
    label2="Tiempo de Reporte",
    numero_ind=None,
):
    """
    Construye la UI del cuerpo del modal con diseño limpio.
    Permite personalizar las etiquetas (por ejemplo, 'Responsable' y 'Tiempo de Reporte')
    e incluir el número/código de indicador (numero_ind).
    """
    lbl1 = label1 if label1 else "Responsable"
    lbl2 = label2 if label2 else "Tiempo de Reporte"
    val1_str = (
        str(campo1_val).strip()
        if pd.notna(campo1_val) and str(campo1_val).strip() != "" and str(campo1_val).strip().lower() != "nan"
        else "No especificado"
    )
    val2_str = (
        str(campo2_val).strip()
        if pd.notna(campo2_val) and str(campo2_val).strip() != "" and str(campo2_val).strip().lower() != "nan"
        else "No especificado"
    )
    formula_str = (
        str(formula).strip()
        if pd.notna(formula) and str(formula).strip() != "" and str(formula).strip().lower() != "nan"
        else "Registro directo / No especificada"
    )
    num_ind_str = (
        str(numero_ind).strip()
        if pd.notna(numero_ind) and str(numero_ind).strip() != "" and str(numero_ind).strip().lower() != "nan"
        else None
    )

    campos = []

    if num_ind_str:
        campos.append(
            html.Div(
                className="modal-campo-grupo",
                children=[
                    html.Span("N° / Código Indicador", className="modal-campo-label"),
                    html.Span(num_ind_str, className="modal-campo-valor", style={"fontWeight": "700", "color": "var(--primary)"}),
                ],
            )
        )

    campos.extend([
        html.Div(
            className="modal-campo-grupo",
            children=[
                html.Span(lbl1, className="modal-campo-label"),
                html.Span(val1_str, className="modal-campo-valor"),
            ],
        ),
        html.Div(
            className="modal-campo-grupo",
            children=[
                html.Span(lbl2, className="modal-campo-label"),
                html.Span(val2_str, className="modal-campo-valor"),
            ],
        ),
        html.Div(
            className="modal-campo-grupo modal-campo-full",
            children=[
                html.Span("Fórmula de Cálculo / Metodología", className="modal-campo-label"),
                html.Div(formula_str, className="modal-campo-formula-box"),
            ],
        ),
    ])

    return html.Div(
        className="modal-cuerpo-grid",
        children=campos,
    )


