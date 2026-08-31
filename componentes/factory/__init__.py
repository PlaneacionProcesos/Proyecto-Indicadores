from componentes.factory.config import SECCIONES_CONFIG
from componentes.factory.tabla import crear_tabla_seccion
from componentes.factory.layout import crear_layout_seccion
from componentes.factory.callback import (
    registrar_callback_seccion,
    registrar_callbacks_todas_secciones,
    procesar_datos_tabla_seccion,
    calcular_variacion_absoluta,
    calcular_variacion_porcentual,
)

__all__ = [
    "SECCIONES_CONFIG",
    "crear_tabla_seccion",
    "crear_layout_seccion",
    "registrar_callback_seccion",
    "registrar_callbacks_todas_secciones",
    "procesar_datos_tabla_seccion",
    "calcular_variacion_absoluta",
    "calcular_variacion_porcentual",
]

