from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from info import DATABASE_URI as MONGO_URL
from pymongo import MongoClient

mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["cloned_vjbotz"]



@Client.on_message(filters.command('customize'))
async def settings(client, message):
   await message.reply_text(
     "<b>📝 Eᴅɪᴛ Δɴᴅ ᴄʜᴀɴɢᴇ ꜱΞᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.......\n<blockquote>ᴩʀᴏ ✨</blockquote></b>",
     reply_markup=main_buttons()
     )

@Client.on_callback_query(filters.regex(r'^customize'))
async def settings_query(bot, query):
  user_id = query.from_user.id
  i, type = query.data.split("#")
  buttons = [[InlineKeyboardButton('«« ʙΔᴄᴋ', callback_data="customize#main")]]
  if type=="main":
     await query.message.edit_text(
       "<b>📝 Eᴅɪᴛ Δɴᴅ ᴄʜᴀɴɢᴇ ꜱΞᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.......\n<blockquote>ᴩʀᴏ ✨</blockquote></b>",
       reply_markup=main_buttons())

  elif type=="forc":  
     await query.message.delete()
     forc_ids = await bot.ask(chat_id=query.message.chat.id, text="<b>❪ SET TARGET CHAT ❫\n\nForward a message from Your target chat\n/cancel - cancel this process</b>")
     if forc_ids.text=="/cancel":
        return await forc_ids.reply_text(
                  "<b>Pʀᴏᴄᴇꜱꜱ ᴄᴀɴᴄᴇʟᴇᴅ 😮‍💨 !</b>",
                  reply_markup=InlineKeyboardMarkup(buttons))
     elif not forc_ids.forward_date:
        return await chat_ids.reply("**This is not a forward message**")
     else:
        chat_id = forc_ids.forward_from_chat.id
        title = forc_ids.forward_from_chat.title
        username = forc_ids.forward_from_chat.username
        username = "@" + username if username else "private"
     foor = await db.add_channel(user_id, chat_id, title, username)
     await query.message.reply_text(
        "<b>Successfully updated</b>",
        reply_markup=InlineKeyboardMarkup(buttons))

def main_buttons():
  buttons = [[
       InlineKeyboardButton('🤖 Бᴏᴛꜱ 🤖',
                    callback_data='customize'),
       InlineKeyboardButton('👣 CʜᴀИИᴇʟꜱ 👣',
                    callback_data=f'customize#forc')
       ],[
       InlineKeyboardButton('✎ Cᴀᴘᴛɪᴏɴ ✎',
                    callback_data='forc'),
       InlineKeyboardButton('𠂤 Dᴀᴛᴀ-Бᴀꜱᴇ 𠂤',
                    callback_data='customize')
       ],[
       InlineKeyboardButton('🖤 Fɪʟᴛᴇʀꜱ 🖤',
                    callback_data='customize'),
       InlineKeyboardButton('🖱 ʙꪊᴛᴛᴏɴ 🖱',
                    callback_data='customize')
       ],[
       InlineKeyboardButton('⌂ H0ᴍᴇ ⌂', callback_data='start')
       ]]
  return InlineKeyboardMarkup(buttons)
