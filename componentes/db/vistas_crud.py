from dash import html, dcc

# Agregamos 'categoria=None' para que acepte el argumento de tu callback de navegación
def layout_documentos(categoria=None):
    return html.Div(
        className="gestor-contenedor",
        children=[
            # Título estilo tabla-agrupadores
            html.H3("Documentos de la Sección", className="gestor-titulo"),
            
            html.Div(
                className="gestor-cuerpo",
                children=[
                    # Zona de Autenticación
                    html.Div(
                        className="gestor-login",
                        children=[
                            html.Label("Acceso Admin:"),
                            dcc.Input(
                                id="input-clave-admin", 
                                type="password", 
                                placeholder="Clave...",
                                className="gestor-input"
                            ),
                            html.Button(
                                "Ingresar", 
                                id="btn-login-admin", 
                                n_clicks=0,
                                className="btn-admin"
                            ),
                        ]
                    ),

                    # Panel de subida (Oculto por defecto)
                    html.Div(
                        id="panel-admin", 
                        style={"display": "none"}, 
                        children=[
                            dcc.Upload(
                                id='upload-documento',
                                className="gestor-upload-area",
                                children=html.Div(['Arrastra y suelta o ', html.A('Selecciona un Archivo')]),
                                multiple=False
                            ),
                            html.Div(id="mensaje-subida", style={"marginTop": "10px"})
                        ]
                    ),

                    # Lista de documentos
                    html.Div(id="lista-documentos-ui"),
                    dcc.Download(id="descargar-documento")
                ]
            )
        ]
    )