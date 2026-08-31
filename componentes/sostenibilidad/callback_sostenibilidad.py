from componentes.factory import registrar_callback_seccion


def registrar_callback_sostenibilidad(app):
    registrar_callback_seccion(
        app=app,
        seccion_id="sostenibilidad",
        clave_nav="sostenibilidad",
        agrupador="Sostenibilidad",
        categoria_db="sostenibilidad",
    )