from dash import Input, Output, html, ctx


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
            seccion = mapa_secciones.get(ctx.triggered_id, "resumen")

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


    # ======================================================================
    # CONTROLADOR DE VISIBILIDAD DE SECCIONES
    # ======================================================================
    @app.callback(
        Output("vista-resumen", "style"),
        Output("vista-gestor-documentos", "style"),
        Output("vista-aprendizaje", "style"),
        Output("vista-en-construccion", "style"),
        Output("texto-en-construccion", "children"),
        Input("seccion-actual", "data"),
    )
    def mostrar_seccion(seccion):
        
        # 1. Manejo por defecto
        if not seccion:
            seccion = "resumen"

        style_oculto = {"display": "none"}
        style_resumen = {"display": "flex", "flexDirection": "column", "flex": "1", "minWidth": "0", "minHeight": "0", "overflow": "hidden"}
        style_gestor = {"display": "block", "padding": "0 20px"}
        style_aprendizaje = {"display": "block", "padding": "0 20px 20px"}
        style_construccion = {"display": "block", "padding": "0 20px 20px"}

        if seccion == "resumen":
            return (
                style_resumen,   # vista-resumen
                style_oculto,    # vista-gestor-documentos
                style_oculto,    # vista-aprendizaje
                style_oculto,    # vista-en-construccion
                "",
            )

        elif seccion == "aprendizaje_evaluacion":
            return (
                style_oculto,       # vista-resumen
                style_gestor,       # vista-gestor-documentos
                style_aprendizaje,  # vista-aprendizaje
                style_oculto,       # vista-en-construccion
                "",
            )

        else:
            nombres = {
                "profesores": "Profesores",
                "estudiantes": "Estudiantes",
                "impacto": "Impacto",
                "investigacion": "Investigación",
                "siac": "SIAC",
                "sostenibilidad": "Sostenibilidad",
            }
            nombre = nombres.get(seccion, seccion)
            return (
                style_oculto,        # vista-resumen
                style_gestor,        # vista-gestor-documentos
                style_oculto,        # vista-aprendizaje
                style_construccion,  # vista-en-construccion
                f"La vista para '{nombre}' aún no está construida.",
            )
