from helper.database import DARKXSIDE78 as db
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import *
from functools import wraps

def check_ban_status(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        user_id = message.from_user.id
        is_banned, ban_reason = await db.is_user_banned(user_id)
        if is_banned:
            await message.reply_text(
                f"**Yᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ.**\n\n**Rᴇᴀsᴏɴ:** {ban_reason}"
            )
            return
        return await func(client, message, *args, **kwargs)
    return wrapper

@Client.on_message(filters.command("metadata"))
@check_ban_status
async def metadata(client, message):
    user_id = message.from_user.id

    current = await db.get_metadata(user_id)
    title = await db.get_title(user_id)
    author = await db.get_author(user_id)
    artist = await db.get_artist(user_id)
    video = await db.get_video(user_id)
    audio = await db.get_audio(user_id)
    subtitle = await db.get_subtitle(user_id)
    encoded_by = await db.get_encoded_by(user_id)
    custom_tag = await db.get_custom_tag(user_id)
    commentz = await db.get_commentz(user_id)

    text = f"""
**㊋ Yᴏᴜʀ Mᴇᴛᴀᴅᴀᴛᴀ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ: {current}**

**◈ Tɪᴛʟᴇ ▹** `{title if title else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Aᴜᴛʜᴏʀ ▹** `{author if author else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Aʀᴛɪꜱᴛ ▹** `{artist if artist else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Aᴜᴅɪᴏ ▹** `{audio if audio else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Sᴜʙᴛɪᴛʟᴇ ▹** `{subtitle if subtitle else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Vɪᴅᴇᴏ ▹** `{video if video else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Eɴᴄᴏᴅᴇᴅ Bʏ ▹** `{encoded_by if encoded_by else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Cᴜsᴛᴏᴍ Tᴀɢ ▹** `{custom_tag if custom_tag else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Cᴏᴍᴍᴇɴᴛ ▹** `{commentz if commentz else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
    """

    buttons = [
        [
            InlineKeyboardButton(f"Oɴ{' 🗸' if current == 'on' else ''}", callback_data='on_metadata'),
            InlineKeyboardButton(f"Oғғ{' 🗸' if current == 'Off' else ''}", callback_data='off_metadata')
        ],
        [
            InlineKeyboardButton("Mᴇᴛᴀᴅᴀᴛᴀ Hᴇʟᴘ", callback_data="metainfo")
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await message.reply_text(text=text, reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex(r"on_metadata|off_metadata|metainfo"))
async def metadata_callback(client, query: CallbackQuery):
    user_id = query.from_user.id
    data = query.data

    if data == "on_metadata":
        await db.set_metadata(user_id, "On")
    elif data == "off_metadata":
        await db.set_metadata(user_id, "Off")
    elif data == "metainfo":
        await query.message.edit_text(
            text=Txt.META_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
                    InlineKeyboardButton("Bᴀᴄᴋ", callback_data="commands")
                ]
            ])
        )
        return

    current = await db.get_metadata(user_id)
    title = await db.get_title(user_id)
    author = await db.get_author(user_id)
    artist = await db.get_artist(user_id)
    video = await db.get_video(user_id)
    audio = await db.get_audio(user_id)
    subtitle = await db.get_subtitle(user_id)
    encoded_by = await db.get_encoded_by(user_id)
    custom_tag = await db.get_custom_tag(user_id)
    commentz = await db.get_commentz(user_id)

    text = f"""
**㊋ Yᴏᴜʀ Mᴇᴛᴀᴅᴀᴛᴀ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ: {current}**

**◈ Tɪᴛʟᴇ ▹** `{title if title else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Aᴜᴛʜᴏʀ ▹** `{author if author else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Aʀᴛɪꜱᴛ ▹** `{artist if artist else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Aᴜᴅɪᴏ ▹** `{audio if audio else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Sᴜʙᴛɪᴛʟᴇ ▹** `{subtitle if subtitle else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Vɪᴅᴇᴏ ▹** `{video if video else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`  
**◈ Eɴᴄᴏᴅᴇᴅ Bʏ ▹** `{encoded_by if encoded_by else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Cᴜsᴛᴏᴍ Tᴀɢ ▹** `{custom_tag if custom_tag else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Cᴏᴍᴍᴇɴᴛ ▹** `{commentz if commentz else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
    """

    buttons = [
        [
            InlineKeyboardButton(f"Oɴ{' 🗸' if current == 'On' else ''}", callback_data='on_metadata'),
            InlineKeyboardButton(f"Oғғ{' 🗸' if current == 'Off' else ''}", callback_data='off_metadata')
        ],
        [
            InlineKeyboardButton("Mᴇᴛᴀᴅᴀᴛᴀ Hᴇʟᴘ", callback_data="metainfo")
        ]
    ]
    await query.message.edit_text(text=text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)


@Client.on_message(filters.private & filters.command('settitle'))
async def title(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            f"**Gɪᴠᴇ Tʜᴇ Tɪᴛʟᴇ\n\nExᴀᴍᴩʟᴇ:- /settitle Encoded By {Config.SHOW_CHANNEL}**")
    title = message.text.split(" ", 1)[1]
    await db.set_title(message.from_user.id, title=title)
    await message.reply_text("**✅ Tɪᴛʟᴇ Sᴀᴠᴇᴅ**")

@Client.on_message(filters.private & filters.command('setauthor'))
async def author(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            f"**Gɪᴠᴇ Tʜᴇ Aᴜᴛʜᴏʀ\n\nExᴀᴍᴩʟᴇ:- /setauthor {Config.SHOW_CHANNEL}**")
    author = message.text.split(" ", 1)[1]
    await db.set_author(message.from_user.id, author=author)
    await message.reply_text("**✅ Aᴜᴛʜᴏʀ Sᴀᴠᴇᴅ**")

@Client.on_message(filters.private & filters.command('setartist'))
async def artist(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            f"**Gɪᴠᴇ Tʜᴇ Aʀᴛɪꜱᴛ\n\nExᴀᴍᴩʟᴇ:- /setartist {Config.SHOW_CHANNEL}**")
    artist = message.text.split(" ", 1)[1]
    await db.set_artist(message.from_user.id, artist=artist)
    await message.reply_text("**✅ Aʀᴛɪꜱᴛ Sᴀᴠᴇᴅ**")

@Client.on_message(filters.private & filters.command('setaudio'))
async def audio(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            f"**Gɪᴠᴇ Tʜᴇ Aᴜᴅɪᴏ Tɪᴛʟᴇ\n\nExᴀᴍᴩʟᴇ:- /setaudio {Config.SHOW_CHANNEL}**")
    audio = message.text.split(" ", 1)[1]
    await db.set_audio(message.from_user.id, audio=audio)
    await message.reply_text("**✅ Aᴜᴅɪᴏ Sᴀᴠᴇᴅ**")

@Client.on_message(filters.private & filters.command('setsubtitle'))
async def subtitle(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            f"**Gɪᴠᴇ Tʜᴇ Sᴜʙᴛɪᴛʟᴇ Tɪᴛʟᴇ\n\nExᴀᴍᴩʟᴇ:- /setsubtitle {Config.SHOW_CHANNEL}**")
    subtitle = message.text.split(" ", 1)[1]
    await db.set_subtitle(message.from_user.id, subtitle=subtitle)
    await message.reply_text("**✅ Sᴜʙᴛɪᴛʟᴇ Sᴀᴠᴇᴅ**")

@Client.on_message(filters.private & filters.command('setvideo'))
async def video(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            f"**Gɪᴠᴇ Tʜᴇ Vɪᴅᴇᴏ Tɪᴛʟᴇ\n\nExᴀᴍᴩʟᴇ:- /setvideo Encoded by {Config.SHOW_CHANNEL}**")
    video = message.text.split(" ", 1)[1]
    await db.set_video(message.from_user.id, video=video)
    await message.reply_text("**✅ Vɪᴅᴇᴏ Sᴀᴠᴇᴅ**")

@Client.on_message(filters.private & filters.command('setencoded_by'))
async def encoded_by(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            f"**Gɪᴠᴇ Tʜᴇ Eɴᴄᴏᴅᴇᴅ Bʏ Tɪᴛʟᴇ\n\nExᴀᴍᴩʟᴇ:- /setencoded_by {Config.SHOW_CHANNEL}**")
    encoded_by = message.text.split(" ", 1)[1]
    await db.set_encoded_by(message.from_user.id, encoded_by=encoded_by)
    await message.reply_text("**✅ Eɴᴄᴏᴅᴇᴅ Bʏ Sᴀᴠᴇᴅ**")
    
@Client.on_message(filters.private & filters.command('setcustom_tag'))
async def custom_tag(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            f"**Gɪᴠᴇ Tʜᴇ Cᴜsᴛᴏᴍ Tᴀɢ Tɪᴛʟᴇ\n\nExᴀᴍᴩʟᴇ:- /setcustom_tag {Config.SHOW_CHANNEL}**")
    custom_tag = message.text.split(" ", 1)[1]
    await db.set_custom_tag(message.from_user.id, custom_tag=custom_tag)
    await message.reply_text("**✅ Eɴᴄᴏᴅᴇᴅ Bʏ Sᴀᴠᴇᴅ**")

@Client.on_message(filters.private & filters.command('setcomment'))
async def custom_tag(client, message):
    if len(message.command) == 1:
        return await message.reply_text(
            f"**Gɪᴠᴇ Tʜᴇ Cᴏᴍᴍᴇɴᴛ Tɪᴛʟᴇ\n\nExᴀᴍᴩʟᴇ:- /setcomment {Config.SHOW_CHANNEL}**")
    custom_tag = message.text.split(" ", 1)[1]
    await db.set_custom_tag(message.from_user.id, custom_tag=custom_tag)
    await message.reply_text("**✅ Cᴏᴍᴍᴇɴᴛ Sᴀᴠᴇᴅ**")

