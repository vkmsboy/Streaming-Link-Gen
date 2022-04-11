# (c) Jigarvarma2005

from helper_funcs.bot_utils import *
from config import Config
import time
from bot import botStartTime
import pyrogram
import shutil, psutil
from pyrogram import Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper_funcs.fsub import handle_force_sub

@app.on_message(pyrogram.filters.private & pyrogram.filters.command(["play"]))
async def direct_player_(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    msg = "Now send me Direct Video URL"
    uri = await input_str(bot, update,msg)
    if uri == 404:
        return
    uri = f"https://{Config.VIDEO_PLAYER_URL}/play?id=" + uri
    await update.reply_text(text=f"Use the below url to stream in website {uri}")
