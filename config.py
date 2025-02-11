# TEAM SHAHIL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "29727048"
    API_HASH = "38d104adbd94c66a349714abd7977d80"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb://factotask:toxictanji@cluster0-shard-00-00.v8qm5.mongodb.net:27017/?authSource=admin"
    START_PIC = "https://graph.org/file/93cf947713f49e9e4f99a.jpg"
    SUDOERS = filters.user(["7029912634"])
