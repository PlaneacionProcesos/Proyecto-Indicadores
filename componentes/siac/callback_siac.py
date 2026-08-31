from componentes.factory import registrar_callback_seccion


def registrar_callback_siac(app):
    registrar_callback_seccion(
        app=app,
        seccion_id="siac",
        clave_nav="siac",
        agrupador="SIAC - Rendicion de Cuentas",
        categoria_db="siac",
    )