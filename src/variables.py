import os
from dotenv import load_dotenv
from telegram import Bot


load_dotenv(".env")
TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(TOKEN)
