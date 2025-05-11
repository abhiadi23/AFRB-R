from pyrogram import Client, filters 
from helper.database import DARKXSIDE78
from pyrogram.types import Message
import os
from functools import wraps

def check_ban_status(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        user_id = message.from_user.id
        is_banned, ban_reason = await DARKXSIDE78.is_user_banned(user_id)
        if is_banned:
            await message.reply_text(
                f"**Yᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ.**\n\n**Rᴇᴀsᴏɴ:** {ban_reason}"
            )
            return
        return await func(client, message, *args, **kwargs)
    return wrapper

@Client.on_message(filters.private & filters.command("get_thumb"))
@check_ban_status
async def get_file_thumb(client, message: Message):
    if not message.reply_to_message or not (message.reply_to_message.document or message.reply_to_message.video):
        return await message.reply_text("**Pʟᴇᴀsᴇ Rᴇᴘʟʏ ᴛᴏ ᴀ Dᴏᴄᴜᴍᴇɴᴛ ᴏʀ Vɪᴅᴇᴏ ᴛʜᴀᴛ ʜᴀs ᴀ Tʜᴜᴍʙɴᴀɪʟ.**")

    media = message.reply_to_message.document or message.reply_to_message.video

    thumb = (
        media.thumbs[0] if getattr(media, "thumbs", None)
        else media.thumbnail if getattr(media, "thumbnail", None)
        else None
    )

    if not thumb:
        return await message.reply_text("**Nᴏ Tʜᴜᴍʙɴᴀɪʟ Fᴏᴜɴᴅ ɪɴ ᴛʜᴀᴛ ᴍᴇᴅɪᴀ.**")

    status_msg = await message.reply_text("**Fᴇᴛᴄʜɪɴɢ Tʜᴜᴍʙɴᴀɪʟ... Pʟᴇᴀsᴇ Wᴀɪᴛ.**")

    try:
        downloaded_thumb = await client.download_media(thumb)
        await client.send_photo(chat_id=message.chat.id, photo=downloaded_thumb, caption="**Hᴇʀᴇ ɪs ᴛʜᴇ Tʜᴜᴍʙɴᴀɪʟ.**")
        os.remove(downloaded_thumb)
    except Exception as e:
        await message.reply_text(f"**Eʀʀᴏʀ:** `{e}`")
    finally:
        await status_msg.delete()

@Client.on_message(filters.private & filters.command('set_caption'))
@check_ban_status
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Gɪᴠᴇ Cᴀᴘᴛɪᴏɴ\n\nExᴀᴍᴘʟᴇ: `/set_caption Nᴀᴍᴇ ➠ : {filename} \n\nSɪᴢᴇ ➠ : {filesize} \n\nDᴜʀᴀᴛɪᴏɴ ➠ : {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await DARKXSIDE78.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ ʜᴀs ʙᴇᴇɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Sᴇᴛ...**")

@Client.on_message(filters.private & filters.command('del_caption'))
@check_ban_status
async def delete_caption(client, message):
    caption = await madflixbotz.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Cᴀᴘᴛɪᴏɴ.**")
    await DARKXSIDE78.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ ʜᴀs ʙᴇᴇɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ...**")

@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption']))
@check_ban_status
async def see_caption(client, message):
    caption = await DARKXSIDE78.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Cᴜʀʀᴇɴᴛ Cᴀᴘᴛɪᴏɴ:**\n\n`{caption}`")
    else:
       await message.reply_text("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Cᴀᴘᴛɪᴏɴ.**")


@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
@check_ban_status
async def viewthumb(client, message):    
    thumb = await DARKXSIDE78.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Tʜᴜᴍʙɴᴀɪʟ.**") 

@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
@check_ban_status
async def removethumb(client, message):
    await DARKXSIDE78.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**Yᴏᴜʀ Tʜᴜᴍʙɴᴀɪʟ ʜᴀs ʙᴇᴇɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ.**")

@Client.on_message(filters.private & filters.photo)
@check_ban_status
async def addthumbs(client, message):
    mkn = await message.reply_text("Pʟᴇᴀsᴇ Wᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ...")
    await DARKXSIDE78.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("**Tʜᴜᴍʙɴᴀɪʟ ʜᴀs ʙᴇᴇɴ Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ.**")
