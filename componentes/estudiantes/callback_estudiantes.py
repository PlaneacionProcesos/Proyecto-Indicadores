from componentes.factory import registrar_callback_seccion


def registrar_callback_estudiantes(app):
    registrar_callback_seccion(
        app=app,
        seccion_id="estudiantes",
        clave_nav="estudiantes",
        agrupador="Estudiantes",
        categoria_db="estudiantes",
    )