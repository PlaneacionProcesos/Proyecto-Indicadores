import os
from pymongo import MongoClient
import gridfs
from dotenv import load_dotenv

load_dotenv()

print("Archivo .env cargado.")

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError(
        "No se encontró MONGODB_URI. "
        "Configúrala en el archivo .env o como variable de entorno."
    )

try:
    client = MongoClient(MONGODB_URI)

    # Comprobar conexión
    client.admin.command("ping")

    db = client["dashboard_db"]
    fs = gridfs.GridFS(db)
    coleccion_metadatos = db["documentos_meta"]

    print("Conexión a MongoDB Atlas exitosa.")

except Exception as e:
    print(f"Error al conectar a MongoDB: {e}")
