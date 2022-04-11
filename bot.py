from helper_funcs.bot_utils import *
from config import Config
import pyrogram
import shutil, psutil
from pyrogram import Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper_funcs.fsub import handle_force_sub
import os
from config import Config
import pyrogram
import wget
import pyromod.listen

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', 'f168ed7a4e5846c66a58eb6b93c8e4da2318c2b1')

bot = Client('droplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm a specialised bot for shortening Droplink.co links which can help you earn money by just sharing links. Made by <a href=\"https://github.com/dakshy\">ToonsHub</a>.")


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
    
    
  
  bot.run()

