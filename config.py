from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","23272158"))
API_HASH = getenv("API_HASH","9c6b7311bf4b00c649674db048c52cbf")

BOT_TOKEN = getenv("BOT_TOKEN","7122702201:AAEH-RPL5Huem69X_c_fOgpXlg3YT7Ukr08")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kingbrukh:kingkhan@kingbruh.ra3pjgm.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 7583810003))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/konnusanlar")
