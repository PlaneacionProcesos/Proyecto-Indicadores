from componentes.factory import registrar_callback_seccion


def registrar_callback_profesores(app):
    registrar_callback_seccion(
        app=app,
        seccion_id="profesores",
        clave_nav="profesores",
        agrupador="Profesores",
        categoria_db="profesores",
    )