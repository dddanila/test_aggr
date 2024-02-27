from dotenv import load_dotenv
import os

load_dotenv()

MONGOODB_URI =  os.getenv("MONGODB_URI")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")