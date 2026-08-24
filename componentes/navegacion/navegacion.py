from dash import dcc, html

def layout_navegacion():
    return(
        html.Div(
            className="navegacion",
            children=[

                html.Button(
                    "Resumen",
                    id="btn-resumen",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Profesores",
                    id="btn-profesores",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Aprendizaje y Evaluación",
                    id="btn-aprendizaje-evaluacion",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Estudiantes",
                    id="btn-estudiantes",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Impacto",
                    id="btn-impacto",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Investigación",
                    id="btn-investigacion",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "SIAC",
                    id="btn-siac",
                    className="marcador",
                    n_clicks=0
                ),

                html.Button(
                    "Sostenibilidad",
                    id="btn-sostenibilidad",
                    className="marcador",
                    n_clicks=0
                ),

            ],
        )
    )