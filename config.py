# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25274255"))
API_HASH = getenv("API_HASH", "02b2832c0e2cc02d8cf178c8a95a5d59")
BOT_TOKEN = getenv("BOT_TOKEN", "7428148949:AAEaukWQDRL1jsJsqQr642eTuGLxVaxYHWo")
OWNER_ID = int(getenv("OWNER_ID", "7103902728"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://mh:qFECbQkAflJ4Teqd@cluster0.c64io4v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1001993672460"))
FORCESUB = getenv("FORCESUB", "Dragon_zone_backup")
