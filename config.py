import os

class Config:
    API_ID = int(os.getenv("API_ID", 23365392))
    API_HASH = os.getenv("API_HASH", 'fffdba007ae9e02207be11b8d8d3f2a8')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '5996900120:AAF3YcDjFBSacTa1SaOKJI2kFJb9epxLjW0')
