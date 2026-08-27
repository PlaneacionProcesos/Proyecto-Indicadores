import os
from pymongo import MongoClient
import gridfs
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = None
db = None
fs = None
coleccion_metadatos = None

if MONGODB_URI:
    try:
        client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
        # Comprobar conexión sin bloquear
        client.admin.command("ping")
        db = client["dashboard_db"]
        fs = gridfs.GridFS(db)
        coleccion_metadatos = db["documentos_meta"]
        print("Conexión a MongoDB Atlas exitosa.")
    except Exception as e:
        print(f"Advertencia: No se pudo conectar a MongoDB Atlas: {e}")
else:
    print("Advertencia: No se encontró MONGODB_URI en las variables de entorno.")
