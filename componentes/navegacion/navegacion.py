from dash import dcc, html

def layout_navegacion():
    return html.Div(
        className="navegacion",
        children=[
            html.Button(
                children=[
                    html.Img(src="assets/iconos/resumen_icon.png", className="icono-marcador"),  # <- Cambia la ruta aquí
                    html.Span("Resumen"),
                ],
                id="btn-resumen",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(src="assets/iconos/profesores.png", className="icono-marcador"),  # <- Cambia la ruta aquí
                    html.Span("Profesores"),
                ],
                id="btn-profesores",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(src="assets/iconos/aprendizaje.png", className="icono-marcador"),  # <- Cambia la ruta aquí
                    html.Span("Aprendizaje y Evaluación"),
                ],
                id="btn-aprendizaje-evaluacion",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(src="assets/iconos/estudiantes.png", className="icono-marcador"),  # <- Cambia la ruta aquí
                    html.Span("Estudiantes"),
                ],
                id="btn-estudiantes",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(src="assets/iconos/impacto.png", className="icono-marcador"),  # <- Cambia la ruta aquí
                    html.Span("Impacto"),
                ],
                id="btn-impacto",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(src="assets/iconos/investigacion.png", className="icono-marcador"),  # <- Cambia la ruta aquí
                    html.Span("Investigación"),
                ],
                id="btn-investigacion",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(src="assets/iconos/SIAC.png", className="icono-marcador"),  # <- Cambia la ruta aquí
                    html.Span("SIAC"),
                ],
                id="btn-siac",
                className="marcador",
                n_clicks=0,
            ),
            html.Button(
                children=[
                    html.Img(src="assets/iconos/sostenibilidad.png", className="icono-marcador"),  # <- Cambia la ruta aquí
                    html.Span("Sostenibilidad"),
                ],
                id="btn-sostenibilidad",
                className="marcador",
                n_clicks=0,
            ),
        ],
    )
