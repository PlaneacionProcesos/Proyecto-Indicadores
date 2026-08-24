import base64

from bson import ObjectId
from bson.errors import InvalidId

from componentes.db.conexion import fs
from componentes.db.categorias import CATEGORIAS_DOCUMENTOS


# ==========================================================
# CATEGORÍAS VÁLIDAS
# ==========================================================

CATEGORIAS_VALIDAS = {
    categoria["value"]
    for categoria in CATEGORIAS_DOCUMENTOS
}


# ==========================================================
# SUBIR DOCUMENTO
# ==========================================================

def subir_documento(
    contenido_base64,
    nombre_archivo,
    categoria,
):
    """
    Decodifica el archivo enviado por Dash y lo guarda
    en GridFS junto con su categoría.
    """

    if not contenido_base64:
        raise ValueError(
            "No se recibió contenido del archivo."
        )

    if not nombre_archivo:
        raise ValueError(
            "El archivo no tiene nombre."
        )

    if not categoria:
        raise ValueError(
            "El documento debe tener una categoría."
        )

    # ------------------------------------------------------
    # Validar categoría
    # ------------------------------------------------------

    if categoria not in CATEGORIAS_VALIDAS:
        raise ValueError(
            f"La categoría '{categoria}' no es válida."
        )

    # ------------------------------------------------------
    # Decodificar contenido enviado por Dash
    # ------------------------------------------------------

    # Ejemplo:
    # data:application/pdf;base64,JVBERi0x...

    if "," in contenido_base64:
        _, string_base64 = contenido_base64.split(
            ",",
            1,
        )
    else:
        string_base64 = contenido_base64

    try:

        decoded = base64.b64decode(
            string_base64,
            validate=True,
        )

    except Exception as e:

        raise ValueError(
            f"No se pudo decodificar el archivo: {e}"
        )

    if not decoded:
        raise ValueError(
            "El archivo está vacío."
        )

    # ------------------------------------------------------
    # Guardar en GridFS
    # ------------------------------------------------------

    file_id = fs.put(
        decoded,
        filename=nombre_archivo,
        metadata={
            "categoria": categoria,
        },
    )

    return str(file_id)


# ==========================================================
# LISTAR DOCUMENTOS
# ==========================================================

def listar_documentos(categoria=None):
    """
    Obtiene documentos de GridFS.

    Si se proporciona una categoría, solamente devuelve
    documentos pertenecientes a esa categoría.
    """

    # ------------------------------------------------------
    # Validar categoría si fue proporcionada
    # ------------------------------------------------------

    if categoria is not None:

        if categoria not in CATEGORIAS_VALIDAS:
            raise ValueError(
                f"La categoría '{categoria}' no es válida."
            )

    # ------------------------------------------------------
    # Construir filtro
    # ------------------------------------------------------

    if categoria:

        filtro = {
            "metadata.categoria": categoria
        }

        archivos = fs.find(
            filtro
        ).sort(
            "uploadDate",
            -1,
        )

    else:

        archivos = fs.find().sort(
            "uploadDate",
            -1,
        )

    # ------------------------------------------------------
    # Construir resultado
    # ------------------------------------------------------

    documentos = []

    for archivo in archivos:

        metadata = archivo.metadata or {}

        documentos.append(
            {
                "id": str(
                    archivo._id
                ),
                "nombre": archivo.filename,
                "fecha": archivo.uploadDate,
                "categoria": metadata.get(
                    "categoria",
                    "sin_categoria",
                ),
            }
        )

    return documentos


# ==========================================================
# OBTENER DOCUMENTO
# ==========================================================

def obtener_documento(file_id):
    """
    Obtiene un archivo de GridFS por su ID.

    Retorna:
        (contenido_bytes, nombre_archivo)
    """

    try:

        object_id = ObjectId(
            file_id
        )

    except (
        InvalidId,
        TypeError,
    ):

        raise ValueError(
            "El ID del documento no es válido."
        )

    try:

        archivo = fs.get(
            object_id
        )

    except Exception:

        raise FileNotFoundError(
            "El documento no existe en la base de datos."
        )

    return (
        archivo.read(),
        archivo.filename,
    )


# ==========================================================
# ELIMINAR DOCUMENTO
# ==========================================================

def eliminar_documento(file_id):
    """
    Elimina un archivo de GridFS por su ID.
    """

    try:

        object_id = ObjectId(
            file_id
        )

    except (
        InvalidId,
        TypeError,
    ):

        raise ValueError(
            "El ID del documento no es válido."
        )

    try:

        fs.get(
            object_id
        )

    except Exception:

        raise FileNotFoundError(
            "El documento no existe."
        )

    fs.delete(
        object_id
    )

    return True