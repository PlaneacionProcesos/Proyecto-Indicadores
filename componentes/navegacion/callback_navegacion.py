from dash import Input, Output, html, ctx
from componentes.navegacion.navegacion import ICONOS_NAVEGACION


def registrar_callbacks_navegacion(app):

    # ======================================================================
    # CONTROLADOR DE BOTONES MENÚ (Actualiza 'seccion-actual', clases e iconos)
    # ======================================================================
        
    @app.callback(
        Output("seccion-actual", "data"),
        # Clases de botones
        Output("btn-resumen", "className"),
        Output("btn-profesores", "className"),
        Output("btn-aprendizaje-evaluacion", "className"),
        Output("btn-estudiantes", "className"),
        Output("btn-impacto", "className"),
        Output("btn-investigacion", "className"),
        Output("btn-siac", "className"),
        Output("btn-sostenibilidad", "className"),
        # Iconos de botones (src)
        Output("icono-resumen", "src"),
        Output("icono-profesores", "src"),
        Output("icono-aprendizaje", "src"),
        Output("icono-estudiantes", "src"),
        Output("icono-impacto", "src"),
        Output("icono-investigacion", "src"),
        Output("icono-siac", "src"),
        Output("icono-sostenibilidad", "src"),
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
        iconos = []

        for boton, nombre_seccion in mapa_secciones.items():

            if nombre_seccion == seccion:
                clases.append("marcador activo")
                iconos.append(ICONOS_NAVEGACION[nombre_seccion]["activo"])
            else:
                clases.append("marcador")
                iconos.append(ICONOS_NAVEGACION[nombre_seccion]["normal"])

        return (
            seccion,
            *clases,
            *iconos,
        )


    # ======================================================================
    # CONTROLADOR DE VISIBILIDAD DE SECCIONES
    # ======================================================================
    @app.callback(
        Output("vista-resumen", "style"),
        Output("vista-aprendizaje", "style"),
        Output("vista-profesores", "style"),
        Output("vista-estudiantes", "style"),
        Output("vista-impacto", "style"),
        Output("vista-investigacion", "style"),      
        Output("vista-siac", "style"),
        Output("vista-sostenibilidad", "style"),
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
        style_aprendizaje = {"display": "block", "padding": "0 20px 20px"}
        style_profesores = {"display": "block", "padding": "0 20px 20px"}
        style_estudiantes= {"display": "block", "padding": "0 20px 20px"}
        style_impacto= {"display": "block", "padding": "0 20px 20px"}
        style_investigacion= {"display": "block", "padding": "0 20px 20px"}
        style_siac= {"display": "block", "padding": "0 20px 20px"}
        style_sostenibilidad= {"display": "block", "padding": "0 20px 20px"}
        style_construccion = {"display": "block", "padding": "0 20px 20px"}

        if seccion == "resumen":
            return (
                style_resumen,       # vista-resumen
                style_oculto,        # vista-aprendizaje
                style_oculto,        # vista-profesores
                style_oculto,        # vista-en-estudiantes
                style_oculto,        # vista-en-impacto   
                style_oculto,        # vista-en-investigacion    
                style_oculto,        # vista-en-siac 
                style_oculto,        # vista-en-sostenibilidad
                style_oculto,        # vista-en-construccion
                "",
            )

        elif seccion == "aprendizaje_evaluacion":
            return (
                style_oculto,        # vista-resumen
                style_aprendizaje,   # vista-aprendizaje
                style_oculto,        # vista-profesores
                style_oculto,        # vista-en-estudiantes
                style_oculto,        # vista-en-impacto    
                style_oculto,        # vista-en-investigacion  
                style_oculto,        # vista-en-siac     
                style_oculto,        # vista-en-sostenibilidad
                style_oculto,        # vista-en-construccion
                "",
            )

        elif seccion == "profesores":
            return (
                style_oculto,        # vista-resumen
                style_oculto,        # vista-aprendizaje
                style_profesores,    # vista-profesores
                style_oculto,        # vista-en-estudiantes
                style_oculto,        # vista-en-impacto     
                style_oculto,        # vista-en-investigacion 
                style_oculto,        # vista-en-siac   
                style_oculto,        # vista-en-sostenibilidad
                style_oculto,        # vista-en-construccion                
                "",
            )

        elif seccion == "estudiantes":
            return (
                style_oculto,        # vista-resumen
                style_oculto,        # vista-aprendizaje
                style_oculto,        # vista-profesores
                style_estudiantes,   # vista-en-estudiantes
                style_oculto,        # vista-en-impacto   
                style_oculto,        # vista-en-investigacion   
                style_oculto,        # vista-en-siac  
                style_oculto,        # vista-en-sostenibilidad
                style_oculto,        # vista-en-construccion
                "",
            )

        elif seccion == "impacto":
            return (
                style_oculto,        # vista-resumen
                style_oculto,        # vista-aprendizaje
                style_oculto,        # vista-profesores
                style_oculto,        # vista-en-estudiantes
                style_impacto,       # vista-en-impacto  
                style_oculto,        # vista-en-investigacion  
                style_oculto,        # vista-en-siac      
                style_oculto,        # vista-en-sostenibilidad
                style_oculto,        # vista-en-construccion
                "",
            )

        elif seccion == "investigacion":
            return (
                style_oculto,        # vista-resumen
                style_oculto,        # vista-aprendizaje
                style_oculto,        # vista-profesores
                style_oculto,        # vista-en-estudiantes
                style_oculto,        # vista-en-impacto  
                style_investigacion, # vista-en-investigacion 
                style_oculto,        # vista-en-siac    
                style_oculto,        # vista-en-sostenibilidad                            
                style_oculto,        # vista-en-construccion
                "",
            )

        elif seccion == "siac":
            return (
                style_oculto,        # vista-resumen
                style_oculto,        # vista-aprendizaje
                style_oculto,        # vista-profesores
                style_oculto,        # vista-en-estudiantes
                style_oculto,        # vista-en-impacto  
                style_oculto,        # vista-en-investigacion 
                style_siac,          # vista-en-siac  
                style_oculto,        # vista-en-sostenibilidad
                style_oculto,        # vista-en-construccion
                "",
            )

        elif seccion == "sostenibilidad":
            return (
                style_oculto,        # vista-resumen
                style_oculto,        # vista-aprendizaje
                style_oculto,        # vista-profesores
                style_oculto,        # vista-en-estudiantes
                style_oculto,        # vista-en-impacto  
                style_oculto,        # vista-en-investigacion 
                style_oculto,          # vista-en-siac  
                style_sostenibilidad,        # vista-en-sostenibilidad
                style_oculto,        # vista-en-construccion
                "",
            )

        else:
            nombres = {
                "sin-datos": "Sin-Datos",
            }
            nombre = nombres.get(seccion, seccion)
            return (
                style_oculto,        # vista-resumen
                style_oculto,        # vista-aprendizaje
                style_oculto,        # vista-profesores
                style_oculto,        # vista-estudiantes
                style_oculto,        # vista-impacto    
                style_oculto,        # vista-en-investigacion  
                style_oculto,        # vista-en-siac    
                style_oculto,        # vista-en-sostenibilidad                            
                style_construccion,  # vista-en-construccion
                f"La vista para '{nombre}' aún no está construida.",
            )
