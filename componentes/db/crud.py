import base64
import re

from bson import ObjectId
from bson.errors import InvalidId

from componentes.db.conexion import fs
from componentes.db.categorias import CATEGORIAS_DOCUMENTOS, TIPOS_VALIDOS


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
    tipo="SGC",
    numero_ind=None,
):
    """
    Decodifica el archivo enviado por Dash y lo guarda
    en GridFS junto con su categoría, tipo (SGC / Estratégicos)
    y opcionalmente el código de indicador (numero_ind).
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
    # Validar categoría y tipo
    # ------------------------------------------------------

    if categoria not in CATEGORIAS_VALIDAS:
        raise ValueError(
            f"La categoría '{categoria}' no es válida."
        )

    if tipo not in TIPOS_VALIDOS:
        tipo = "SGC"

    # ------------------------------------------------------
    # Decodificar contenido enviado por Dash
    # ------------------------------------------------------

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

    metadata = {
        "categoria": categoria,
        "tipo": tipo,
    }

    if numero_ind:
        metadata["numero_ind"] = str(numero_ind).strip()

    file_id = fs.put(
        decoded,
        filename=nombre_archivo,
        metadata=metadata,
    )

    return str(file_id)


# ==========================================================
# LISTAR DOCUMENTOS
# ==========================================================

def listar_documentos(categoria=None, tipo=None, numero_ind=None):
    """
    Obtiene documentos de GridFS.

    Si se proporciona una categoría, solamente devuelve
    documentos pertenecientes a esa categoría.
    Si se proporciona un tipo ('SGC' o 'Estrategicos'), filtra por tipo.
    Si se proporciona un numero_ind, filtra por código de indicador.
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

    filtro = {}

    if categoria:
        filtro["metadata.categoria"] = categoria

    if tipo and tipo in TIPOS_VALIDOS:
        filtro["metadata.tipo"] = tipo

    if numero_ind:
        filtro["metadata.numero_ind"] = str(numero_ind).strip()

    archivos = fs.find(filtro).sort(
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
                "tipo": metadata.get(
                    "tipo",
                    "SGC",
                ),
                "numero_ind": metadata.get(
                    "numero_ind",
                    None,
                ),
            }
        )

    return documentos


# ==========================================================
# OBTENER DOCUMENTO POR INDICADOR Y TIPO (MODAL)
# ==========================================================

def obtener_documento_por_indicador(numero_ind, tipo="SGC", categoria=None):
    """
    Busca y descarga un documento asociado a un número de indicador y tipo (SGC / Estratégicos).
    
    1. Búsqueda exacta en metadata.numero_ind y metadata.tipo (filtrando por categoría si existe).
    2. Búsqueda secundaria en metadata.numero_ind sin filtro de categoría.
    3. Búsqueda terciaria por coincidencia del código en el nombre del archivo (filename).
    
    Retorna:
        (contenido_bytes, nombre_archivo) o (None, None) si no se encuentra.
    """
    if not numero_ind or not tipo:
        return None, None

    num_limpio = str(numero_ind).strip()
    tipo_normalizado = "Estrategicos" if ("estrateg" in tipo.lower() or tipo == "Estrategicos") else "SGC"

    # 1. Búsqueda primaria por metadata con categoría
    filtro_primario = {
        "metadata.numero_ind": num_limpio,
        "metadata.tipo": tipo_normalizado,
    }
    if categoria:
        filtro_primario["metadata.categoria"] = categoria

    archivo = fs.find_one(filtro_primario)

    # 2. Búsqueda secundaria sin categoría
    if not archivo and categoria:
        archivo = fs.find_one({
            "metadata.numero_ind": num_limpio,
            "metadata.tipo": tipo_normalizado,
        })

    # 3. Búsqueda por regex en filename
    if not archivo:
        patron = re.escape(num_limpio)
        filtro_regex = {
            "filename": {"$regex": patron, "$options": "i"},
            "metadata.tipo": tipo_normalizado,
        }
        if categoria:
            filtro_regex["metadata.categoria"] = categoria

        archivo = fs.find_one(filtro_regex)

        if not archivo:
            # Reintentar regex sin categoría
            archivo = fs.find_one({
                "filename": {"$regex": patron, "$options": "i"},
                "metadata.tipo": tipo_normalizado,
            })

    if not archivo:
        return None, None

    return archivo.read(), archivo.filename


# ==========================================================
# OBTENER DOCUMENTO POR ID
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