# TEAM SHAHIL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "29727048"
    API_HASH = "38d104adbd94c66a349714abd7977d80"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://Chatgpt:Chatgpt%40123@chatgpt.56l90.mongodb.net/?retryWrites=true&w=majority&appName=Chatgpt"
    START_PIC = "https://envs.sh/aKf.mp4"
    SUDOERS = filters.user(["8129810243"])
