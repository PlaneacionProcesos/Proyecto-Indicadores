from dash import Input, Output, html, ctx
from secciones.resumen import layout_resumen
from componentes.db.vistas_crud import layout_documentos
from secciones.aprendizaje_evaluacion import layout_aprendizaje


def registrar_callbacks_navegacion(app):

    # ======================================================================
    # CONTROLADOR DE BOTONES MENÚ (Actualiza 'seccion-actual')
    # ======================================================================
        
    @app.callback(
        Output("seccion-actual", "data"),
        Output("btn-resumen", "className"),
        Output("btn-profesores", "className"),
        Output("btn-aprendizaje-evaluacion", "className"),
        Output("btn-estudiantes", "className"),
        Output("btn-impacto", "className"),
        Output("btn-investigacion", "className"),
        Output("btn-siac", "className"),
        Output("btn-sostenibilidad", "className"),
        Input("btn-resumen", "n_clicks"),
        Input("btn-profesores", "n_clicks"),
        Input("btn-aprendizaje-evaluacion", "n_clicks"),
        Input("btn-estudiantes", "n_clicks"),
        Input("btn-impacto", "n_clicks"),
        Input("btn-investigacion", "n_clicks"),
        Input("btn-siac", "n_clicks"),
        Input("btn-sostenibilidad", "n_clicks"),
    )
    def cambiar_seccion(
        resumen,
        profesores,
        aprendizaje_evaluacion,
        estudiantes,
        impacto,
        investigacion,
        siac,
        sostenibilidad,
    ):

        mapa_secciones = {
            "btn-resumen": "resumen",
            "btn-profesores": "profesores",
            "btn-aprendizaje-evaluacion": "aprendizaje_evaluacion",
            "btn-estudiantes": "estudiantes",
            "btn-impacto": "impacto",
            "btn-investigacion": "investigacion",
            "btn-siac": "siac",
            "btn-sostenibilidad": "sostenibilidad",
        }

        if not ctx.triggered_id:
            seccion = "resumen"
        else:
            seccion = mapa_secciones[ctx.triggered_id]

        clases = []

        for boton, nombre_seccion in mapa_secciones.items():

            if nombre_seccion == seccion:
                clases.append("marcador activo")
            else:
                clases.append("marcador")

        return (
            seccion,
            *clases,
        )


    @app.callback(
        Output("contenido-seccion", "children"),
        Input("seccion-actual", "data"),
    )
    def mostrar_seccion(seccion):
        
        # 1. Manejo por defecto
        if not seccion:
            seccion = "resumen"

        # 2. PRIMERO creamos la lista vacía
        elementos_pantalla = []

        # ======================================================================
        # 3. GESTOR DE DOCUMENTOS (Aparecerá en la parte SUPERIOR de la pantalla)
        # ======================================================================
        if seccion != "resumen":
            elementos_pantalla.append(layout_documentos(categoria=seccion))
            
        # ======================================================================
        # 4. VISTA DE LA SECCIÓN (Aparecerá DEBAJO de los documentos)
        # ======================================================================
        if seccion == "resumen":
            elementos_pantalla.append(layout_resumen())

        elif seccion == "aprendizaje_evaluacion":
            elementos_pantalla.append(layout_aprendizaje())

        # elif seccion == "investigacion":
        #     elementos_pantalla.append(layout_investigacion())
        
        else:
            # Mensaje por si la pantalla no existe aún
            elementos_pantalla.append(
                html.Div(
                    f"La vista para '{seccion}' aún no está construida.",
                    style={"padding": "50px", "textAlign": "center"},
                )
            )

        # 5. Finalmente, devolvemos todo el paquete armado en ese orden
        return elementos_pantalla
