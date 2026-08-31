from dash import html, dcc

def layout_documentos(categoria=None):
    return html.Div(
        id="modal-gestor-documentos",
        className="modal-contexto-overlay",
        style={"display": "none"},
        children=[
            html.Div(
                className="modal-contexto-card",
                style={"maxWidth": "780px", "width": "92%"},
                children=[
                    # Header del Modal de Documentos
                    html.Div(
                        className="modal-contexto-header",
                        children=[
                            html.Div(
                                className="modal-contexto-header-texto",
                                children=[
                                    html.Span("GESTOR DE EVIDENCIAS Y DOCUMENTOS", className="modal-contexto-tag"),
                                    html.H3(
                                        "Documentos de la Sección",
                                        id="titulo-gestor-modal",
                                        className="modal-contexto-titulo",
                                    ),
                                ],
                            ),
                            html.Button(
                                "✕",
                                id="btn-cerrar-gestor-modal",
                                className="btn-cerrar-modal-contexto",
                                n_clicks=0,
                            ),
                        ],
                    ),
                    # Cuerpo del Modal
                    html.Div(
                        className="modal-contexto-cuerpo",
                        style={"gap": "14px"},
                        children=[
                            # Botón / Barra de acceso Admin
                            html.Div(
                                id="zona-login-admin",
                                className="gestor-login",
                                style={"display": "none"},
                                children=[
                                    html.Label("Clave Admin:"),
                                    dcc.Input(
                                        id="input-clave-admin", 
                                        type="password", 
                                        placeholder="Clave admin...",
                                        className="gestor-input"
                                    ),
                                    html.Button(
                                        "Desbloquear Carga", 
                                        id="btn-login-admin", 
                                        n_clicks=0,
                                        className="btn-admin"
                                    ),
                                    html.Button(
                                        "✕", 
                                        id="btn-cerrar-admin", 
                                        n_clicks=0,
                                        className="btn-cerrar-admin",
                                        title="Ocultar acceso admin"
                                    ),
                                ]
                            ),

                            # Botón para mostrar zona login si no está visible
                            html.Div(
                                id="contenedor-btn-activar-admin",
                                style={"display": "flex", "justifyContent": "flex-end"},
                                children=[
                                    html.Button(
                                        "🔒 Cargar nuevo archivo (Admin)",
                                        id="btn-mostrar-login-admin",
                                        className="btn-descargar",
                                        n_clicks=0,
                                        style={"fontSize": "12px", "padding": "5px 12px"}
                                    )
                                ]
                            ),

                            # Panel de subida (Oculto por defecto hasta ingresar clave admin)
                            html.Div(
                                id="panel-admin", 
                                style={"display": "none"}, 
                                children=[
                                    # Selector de tipo de archivo (SGC vs Estratégicos)
                                    html.Div(
                                        className="gestor-tipo-selector",
                                        children=[
                                            html.Label("Tipo de Archivo:"),
                                            dcc.RadioItems(
                                                id="radio-tipo-documento",
                                                options=[
                                                    {"label": " SGC", "value": "SGC"},
                                                    {"label": " Estratégicos", "value": "Estrategicos"},
                                                ],
                                                value="SGC",
                                                inline=True,
                                                className="gestor-radio-tipos",
                                                inputStyle={"marginRight": "5px", "marginLeft": "8px"},
                                            ),
                                        ]
                                    ),
                                    # Selector de Indicador de la sección (Dropdown desplegable)
                                    html.Div(
                                        className="gestor-tipo-selector",
                                        style={"display": "flex", "flexDirection": "column", "alignItems": "flex-start", "gap": "6px"},
                                        children=[
                                            html.Label("Asociar a Indicador (Opcional):", style={"fontWeight": "700", "fontSize": "13px"}),
                                            dcc.Dropdown(
                                                id="dropdown-numero-ind-subida",
                                                placeholder="Selecciona un indicador de esta sección...",
                                                className="gestor-dropdown-indicador",
                                                clearable=True,
                                                style={"width": "100%", "fontSize": "13px"},
                                            ),
                                        ]
                                    ),
                                    dcc.Upload(
                                        id='upload-documento',
                                        className="gestor-upload-area",
                                        children=html.Div(['Arrastra y suelta o ', html.A('Selecciona un Archivo')]),
                                        multiple=False
                                    ),
                                    html.Div(id="mensaje-subida", style={"marginTop": "10px"})
                                ]
                            ),

                            # Barra de filtro por tipo de documento
                            html.Div(
                                className="gestor-filtro-contenedor",
                                children=[
                                    html.Span("Mostrar tipo:", className="gestor-filtro-label"),
                                    dcc.RadioItems(
                                        id="filtro-tipo-doc-lista",
                                        options=[
                                            {"label": " Todos", "value": "Todos"},
                                            {"label": " SGC", "value": "SGC"},
                                            {"label": " Estratégicos", "value": "Estrategicos"},
                                        ],
                                        value="Todos",
                                        inline=True,
                                        className="gestor-filtro-tipo-lista",
                                        inputStyle={"marginRight": "4px", "marginLeft": "10px"},
                                    ),
                                ]
                            ),

                            # Lista de documentos
                            html.Div(id="lista-documentos-ui"),
                            dcc.Download(id="descargar-documento")
                        ]
                    ),
                    # Footer del Modal
                    html.Div(
                        className="modal-contexto-footer",
                        children=[
                            html.Button(
                                "Cerrar",
                                id="btn-entendido-gestor-modal",
                                className="btn-entendido-modal",
                                n_clicks=0,
                            ),
                        ],
                    ),
                ]
            )
        ]
    )
