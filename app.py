from dash import Dash, dcc, html

from datos import resultados_completos

from secciones.resumen import layout_resumen
from secciones.aprendizaje_evaluacion import layout_aprendizaje
from componentes.db.vistas_crud import layout_documentos
from componentes.header import layout_header
from componentes.navegacion.navegacion import layout_navegacion
from componentes.filtros import layout_filtros
from componentes.footer import layout_footer
from secciones.profesores import layout_profesores
from secciones.estudiantes import layout_estudiantes
from secciones.impacto import layout_impacto
from secciones.investigacion import layout_investigacion
from secciones.siac import layout_siac
from secciones.sostenibilidad import layout_sostenibilidad

from componentes.db.callbacks_db import registrar_callbacks_db
from componentes.navegacion.callback_navegacion import registrar_callbacks_navegacion
from componentes.resumen.callbacks_resumen import registrar_callbacks_resumen
from callbacks_ocultar_filtros import registrar_callback_ocultar_filtros
from componentes.aprendizaje_y_evaluacion.callback_aprendizaje import registrar_callback_aprendizaje
from componentes.profesores.callback_profesores import registrar_callback_profersores
from componentes.estudiantes.callback_estudiantes import registrar_callback_estudiantes
from componentes.impacto.callback_impacto import registrar_callback_impacto
from componentes.investigacion.callback_investigacion import registrar_callback_investigacion
from componentes.siac.callback_siac import registrar_callback_siac
from componentes.sostenibilidad.callback_sostenibilidad import registrar_callback_sostenibilidad


app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # Instancia WSGI para Vercel / Gunicorn / Waitress


# ========================================================================================
#                                      LAYOUT
# ========================================================================================

app.layout = html.Div(
    className="app",
    children=[

        # ==================================================================================
        # HEADER
        # ==================================================================================

        layout_header(),

        # ==================================================================================
        # NAVEGACIÓN
        # ==================================================================================

        layout_navegacion(),

        # ==================================================================================
        # SECCIÓN ACTUAL
        # ==================================================================================

        dcc.Store(
            id="seccion-actual",
            data="resumen",
        ),

        # ==================================================================================
        # CONTENEDOR PRINCIPAL
        # ==================================================================================

        html.Div(
            className="contenedor",
            children=[

                # --------------------------------------------------------------------------
                # FILTROS
                # --------------------------------------------------------------------------

                layout_filtros(),

                # --------------------------------------------------------------------------
                # CONTENIDO DE SECCIONES (PERSISTENTE)
                # --------------------------------------------------------------------------

                html.Div(
                    id="contenido-seccion",
                    children=[
                        # Vista Resumen
                        html.Div(
                            id="vista-resumen",
                            children=[layout_resumen()],
                            style={"display": "flex", "flexDirection": "column", "flex": "1", "minWidth": "0", "minHeight": "0", "overflow": "hidden"},
                        ),

                        
                        # Vista Aprendizaje y Evaluación
                        html.Div(
                            id="vista-aprendizaje",
                            children=[layout_aprendizaje()],
                            style={"display": "none"},
                        ),

                        html.Div(
                            id="vista-profesores",
                            children=[layout_profesores()],
                            style={"display": "none"},
                        ),

                        html.Div(
                            id="vista-estudiantes",
                            children=[layout_estudiantes()],
                            style={"display": "none"},
                        ),

                        html.Div(
                            id="vista-impacto",
                            children=[layout_impacto()],
                            style={"display": "none"},
                        ),

                        html.Div(
                            id="vista-investigacion",
                            children=[layout_investigacion()],
                            style={"display": "none"},
                        ), 

                        html.Div(
                            id="vista-siac",
                            children=[layout_siac()],
                            style={"display": "none"},
                        ), 

                        html.Div(
                            id="vista-sostenibilidad",
                            children=[layout_sostenibilidad()],
                            style={"display": "none"},
                        ),                                                 

                        
                        # Vista para secciones en construcción
                        html.Div(
                            id="vista-en-construccion",
                            children=[
                                html.Div(
                                    id="texto-en-construccion",
                                    children="La vista para esta sección aún no está construida.",
                                    style={"padding": "50px", "textAlign": "center", "fontSize": "16px", "color": "#666"},
                                )
                            ],
                            style={"display": "none"},
                        ),

                        # Gestor de Documentos (para secciones no-resumen)
                        html.Div(
                            id="vista-gestor-documentos",
                            children=[layout_documentos()],
                            style={"display": "none"},
                        ),

                    ],
                ),
            ],
        ),

        # ==================================================================================
        # FOOTER
        # ==================================================================================

        layout_footer(),
    ],
)


# ========================================================================================
#                                      CALLBACKS
# ========================================================================================

registrar_callbacks_resumen(app)

registrar_callbacks_navegacion(app)

registrar_callbacks_db(app)

registrar_callback_ocultar_filtros(app)

registrar_callback_aprendizaje(app)

registrar_callback_profersores(app)

registrar_callback_estudiantes(app)

registrar_callback_impacto(app)

registrar_callback_investigacion(app)

registrar_callback_siac(app)

registrar_callback_sostenibilidad(app)

# ========================================================================================
#                                      EJECUCIÓN
# ========================================================================================

if __name__ == "__main__":
    app.run(debug=True)