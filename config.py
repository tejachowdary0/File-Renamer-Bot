import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27604683")

API_HASH = os.environ.get("API_HASH", "ed52a1d0803b2ed84c5cca7f20535aac")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6636903897:AAH4jTAphNyRH9jHXQfi-FQd3WO-3LSRcxU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001942937148") 

DB_NAME = os.environ.get("DB_NAME","jonny002")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://jonnywaker002:WlPnEIcbNTY2jc47@jonny002.fgsyjqw.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/14929fa56470f5bd74b88.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1264280791').split()]

PORT = os.environ.get("PORT", "8080")
