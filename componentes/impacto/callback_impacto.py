from componentes.factory import registrar_callback_seccion


def registrar_callback_impacto(app):
    registrar_callback_seccion(
        app=app,
        seccion_id="impacto",
        clave_nav="impacto",
        agrupador="Impacto",
        categoria_db="impacto",
    )