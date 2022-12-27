import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27639102")

API_HASH = os.environ.get("API_HASH", "35142c1407be6264e68fb6bec5dcabd9")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5906887802:AAFxiHDzneMSKc70V9JNgUufx2_GpCE08Dw") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001787446188") 

DB_NAME = os.environ.get("DB_NAME","renamerbot")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Fileshare123:Fileshare123@cluster0.nqjle5f.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/14929fa56470f5bd74b88.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")
