from componentes.factory import registrar_callback_seccion


def registrar_callback_investigacion(app):
    registrar_callback_seccion(
        app=app,
        seccion_id="investigacion",
        clave_nav="investigacion",
        agrupador="Investigacion",
        categoria_db="investigacion",
    )