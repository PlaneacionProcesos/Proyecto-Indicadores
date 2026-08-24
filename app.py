from dash import Dash, dcc, html

from datos import resultados_completos

from secciones.resumen import layout_resumen
from componentes.header import layout_header
from componentes.navegacion.navegacion import layout_navegacion
from componentes.filtros import layout_filtros
from componentes.footer import layout_footer

from componentes.db.callbacks_db import registrar_callbacks_db
from componentes.navegacion.callback_navegacion import registrar_callbacks_navegacion
from componentes.resumen.callbacks_resumen import registrar_callbacks_resumen
from callbacks_ocultar_filtros import registrar_callback_ocultar_filtros
from componentes.aprendizaje_y_evaluacion.callback_aprendizaje import registrar_callback_aprendizaje


app = Dash(__name__, suppress_callback_exceptions=True)


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
                # CONTENIDO DINÁMICO
                # --------------------------------------------------------------------------

                html.Div(
                    id="contenido-seccion",
                    # children=layout_resumen(),
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

# ========================================================================================
#                                      EJECUCIÓN
# ========================================================================================

if __name__ == "__main__":
    app.run(debug=True)