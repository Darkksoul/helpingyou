
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
# from pyrogram.types import CallbackQuery
import random
import os
from info import SP
from Script import script
import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import BR_IMDB_TEMPLATE, PROTECT_CONTENT, AUTH_CHANNEL, BATCH_LINK, ADMINS, LOG_CHANNEL
from utils import extract_user, get_file_id, get_poster, last_online
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.ia_filterdb import Media, get_file_details, get_search_results, get_bad_files
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
from info import IMDB









Muhammed = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

ALL_PIC = [
 "https://te.legra.ph/file/b700bbbf7329b04f3673a.jpg",
 "https://telegra.ph/file/1a2b6e76af675065491a7.jpg"
 ]



START_MESSAGE = """
𝐇𝐞𝐥𝐥𝐨 <a href='tg://settings'>𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮⚡️</a>

# @Client.on_callback_query()
# async def callback(bot: Client, query: CallbackQuery):
#     if query.data== "r":
#         await query.message.edit(
#             text=f"ok da"
#         )





@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    imdb = await get_poster(content) if IMDB else None
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtags
#    if user_id in ADMINS: return # ignore admins
    
    
    try:
            buttons = [[
                InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'https://t.me/Devilservers'),
                InlineKeyboardButton("𝐒𝐮𝐫𝐩𝐫𝐢𝐬𝐞", url=f"https://telegram.me/{temp.U_NAME}?start"),
                InlineKeyboardButton('𝐋𝐞𝐭𝐞𝐬𝐭 𝐓𝐫𝐲', url=(BATCH_LINK))      
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await message.reply_photo(photo=imdb.get('poster'), caption=f"𝐇𝐞𝐲 {content} 𝐌𝐨𝐯𝐢𝐞 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩...\n\n🏷𝐓𝐢𝐭𝐥𝐞 :  {imdb.get('title')}\n\n🎭 Genres: {imdb.get('genres')}\n\n🌟 𝐑𝐚𝐭𝐢𝐧𝐠 : {imdb.get('rating')}\n\n☀️ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬 : {imdb.get('languages')}\n\n📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞 : {imdb.get('runtime')}\n\n📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨 : {imdb.get('year')}\n\n🎛 𝐂𝐨𝐮𝐧𝐭𝐫𝐢𝐞𝐬 : {imdb.get('countries')}\n\n{imdb.get('title')}",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
            )
                                      
    except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            buttons = [[
                InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'https://t.me/Devilservers'),
                InlineKeyboardButton("𝐒𝐮𝐫𝐩𝐫𝐢𝐬𝐞", url=f"https://telegram.me/{temp.U_NAME}?start"),
                InlineKeyboardButton('𝐋𝐞𝐭𝐞𝐬𝐭 𝐓𝐫𝐲', url=(BATCH_LINK))           
            ]]
            hmm = await message.reply_photo(photo=poster, caption=f"𝐇𝐞𝐲 {content} 𝐌𝐨𝐯𝐢𝐞 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩...\n\n🏷𝐓𝐢𝐭𝐥𝐞 :  {imdb.get('title')}\n\n🎭 Genres: {imdb.get('genres')}\n\n🌟 𝐑𝐚𝐭𝐢𝐧𝐠 : {imdb.get('rating')}\n\n☀️ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬 : {imdb.get('languages')}\n\n📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞 : {imdb.get('runtime')}\n\n📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨 : {imdb.get('year')}\n\n🎛 𝐂𝐨𝐮𝐧𝐭𝐫𝐢𝐞𝐬 : {imdb.get('countries')}\n\n{imdb.get('title')}",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
            )
    except Exception as e:
        logger.exception(e)




