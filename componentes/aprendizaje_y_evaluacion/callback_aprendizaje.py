from componentes.factory import registrar_callback_seccion


def registrar_callback_aprendizaje(app):
    registrar_callback_seccion(
        app=app,
        seccion_id="aprendizaje",
        clave_nav="aprendizaje_evaluacion",
        agrupador="Aprendizaje y Evaluacion",
        categoria_db="aprendizaje_evaluacion",
    )
