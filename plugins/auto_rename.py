from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import DARKXSIDE78
from pyrogram.types import CallbackQuery
import pytz
import logging
from math import ceil
from functools import wraps
from config import Config
from datetime import datetime

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

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@Client.on_message((filters.private | filters.group) & filters.command("rename_history"))
@check_ban_status
async def rename_history(client, message):
    args = message.text.split(maxsplit=1)
    user_id = message.from_user.id

    # Check if the user is an admin or premium
    is_admin = user_id in Config.ADMINS
    is_premium = await DARKXSIDE78.is_premium(user_id)

    # Determine whose history to fetch
    if len(args) > 1 and (is_admin or is_premium):
        try:
            target_user_id = int(args[1])
        except ValueError:
            return await message.reply_text("**Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ ID.**")
    else:
        target_user_id = user_id

    # Fetch rename history
    history = await DARKXSIDE78.get_rename_history(target_user_id)
    if not history:
        return await message.reply_text("**Nᴏ ʀᴇɴᴀᴍᴇ ʜɪsᴛᴏʀʏ ғᴏᴜɴᴅ.**")

    # Pagination variables
    items_per_page = 25
    total_pages = ceil(len(history) / items_per_page)
    current_page = 1

    # Generate the first page
    await send_history_page(client, message, history, current_page, total_pages, items_per_page, target_user_id)


async def send_history_page(client, message, history, current_page, total_pages, items_per_page, target_user_id):
    """Send a specific page of rename history with navigation buttons."""
    start_index = (current_page - 1) * items_per_page
    end_index = start_index + items_per_page
    page_items = history[start_index:end_index]

    # Format the history for the current page
    history_text = "\n".join([
        f"**Oʀɪɢɪɴᴀʟ:** `{item.get('original_name', 'Unknown')}` ➨ **Rᴇɴᴀᴍᴇᴅ:** `{item.get('renamed_name', 'Unknown')}`"
        for item in page_items
    ])
    text = (
        f"**Rᴇɴᴀᴍᴇ Hɪsᴛᴏʀʏ ғᴏʀ Usᴇʀ {target_user_id} (Pᴀɢᴇ {current_page}/{total_pages}):**\n\n"
        f"{history_text}"
    )

    # Create navigation buttons
    buttons = []
    if current_page > 1:
        buttons.append(InlineKeyboardButton("« Pʀᴇᴠɪᴏᴜs", callback_data=f"history_page_{current_page - 1}_{target_user_id}"))
    if current_page < total_pages:
        buttons.append(InlineKeyboardButton("Nᴇxᴛ »", callback_data=f"history_page_{current_page + 1}_{target_user_id}"))

    reply_markup = InlineKeyboardMarkup([buttons]) if buttons else None

    # Send or edit the message
    if message.reply_to_message:
        await message.reply_to_message.edit_text(text, reply_markup=reply_markup)
    else:
        await message.reply_text(text, reply_markup=reply_markup)


@Client.on_callback_query(filters.regex(r"^history_page_\d+_\d+$"))
async def handle_history_pagination(client, callback_query: CallbackQuery):
    """Handle pagination for rename history."""
    data = callback_query.data.split("_")
    current_page = int(data[2])
    target_user_id = int(data[3])

    # Fetch rename history
    history = await DARKXSIDE78.get_rename_history(target_user_id)
    if not history:
        return await callback_query.answer("Nᴏ ʀᴇɴᴀᴍᴇ ʜɪsᴛᴏʀʏ ғᴏᴜɴᴅ.", show_alert=True)

    # Pagination variables
    items_per_page = 25
    total_pages = ceil(len(history) / items_per_page)

    # Send the requested page
    await send_history_page(client, callback_query.message, history, current_page, total_pages, items_per_page, target_user_id)
    await callback_query.answer()

@Client.on_message(filters.private & filters.command("autorename"))
@check_ban_status
async def auto_rename_command(client, message):
    try:
        user_id = message.from_user.id
        
        command_parts = message.text.split(maxsplit=1)
        if len(message.command) < 2 or not command_parts[1].strip():
            await message.reply_text(
                "**Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇɴᴀᴍᴇ ᴛᴇᴍᴘʟᴀᴛᴇ**\n\n"
                "**Fᴏʀᴍᴀᴛ:** `/autorename [Season-Episode] Show Name [Quality] [Audio] @ChannelName`\n"
                "**Exᴀᴍᴘʟᴇ:** `/autorename [Sseason-episode] World Trigger [quality] [audio] @GenAnimeOfc`\n\n"
                "**Tʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴜsᴇ ᴛʜɪs ᴛᴇᴍᴘʟᴀᴛᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ.**"
            )
            return

        format_template = command_parts[1].strip()

        await DARKXSIDE78.set_format_template(user_id, format_template)
        
        await message.reply_text(
                "**Aᴜᴛᴏ-ʀᴇɴᴀᴍᴇ ᴛᴇᴍᴘʟᴀᴛᴇ sᴇᴛ sᴜᴄᴄᴇssғᴜʟʟʏ!**\n\n"
                f"**Yᴏᴜʀ ᴛᴇᴍᴘʟᴀᴛᴇ:** `{format_template}`\n\n"
                "**Nᴏᴡ ᴡʜᴇɴ ʏᴏᴜ sᴇɴᴅ ғɪʟᴇs, ᴛʜᴇʏ'ʟʟ ʙᴇ ʀᴇɴᴀᴍᴇᴅ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴜsɪɴɢ ᴛʜɪs ғᴏʀᴍᴀᴛ.**"
        )
    except Exception as e:
        logger.error(f"Error in auto_rename_command: {e}", exc_info=True)
        await message.reply_text("**Aɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sᴇᴛᴛɪɴɢ ᴛʜᴇ ᴀᴜᴛᴏ-ʀᴇɴᴀᴍᴇ ᴛᴇᴍᴘʟᴀᴛᴇ.**")

@Client.on_message(filters.private & filters.command("setmedia"))
@check_ban_status
async def set_media_command(client, message):
    """Initiate media type selection with a sleek inline keyboard."""
    keyboard = InlineKeyboardMarkup([
        [
                InlineKeyboardButton("Dᴏᴄᴜᴍᴇɴᴛ", callback_data="setmedia_document"),
                InlineKeyboardButton("Vɪᴅᴇᴏ", callback_data="setmedia_video"),
        ],
        [
                InlineKeyboardButton("Aᴜᴅɪᴏ", callback_data="setmedia_audio"),
        ]
    ])

    await message.reply_text(
            "**Sᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘʀᴇғᴇʀʀᴇᴅ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ:**\n"
            "**Tʜɪs ᴡɪʟʟ ᴅᴇᴛᴇʀᴍɪɴᴇ ʜᴏᴡ ʏᴏᴜʀ ғɪʟᴇs ᴀʀᴇ ʜᴀɴᴅʟᴇᴅ ʙʏ ᴛʜᴇ ʙᴏᴛ.**",
            reply_markup=keyboard,
            quote=True
    )

@Client.on_callback_query(filters.regex(r"^setmedia_"))
async def handle_media_selection(client, callback_query: CallbackQuery):
    try:
        user_id = callback_query.from_user.id
        media_type = callback_query.data.split("_", 1)[1].capitalize()

        try:
            await DARKXSIDE78.set_media_preference(user_id, media_type.lower())
        
            await callback_query.answer(f"Mᴇᴅɪᴀ ᴘʀᴇғᴇʀᴇɴᴄᴇ sᴇᴛ ᴛᴏ {media_type.capitalize()}")
            await callback_query.message.edit_text(
                f"**Mᴇᴅɪᴀ ᴘʀᴇғᴇʀᴇɴᴄᴇ ᴜᴘᴅᴀᴛᴇᴅ!**\n"
                f"**Yᴏᴜʀ ғɪʟᴇs ᴡɪʟʟ ɴᴏᴡ ʙᴇ ʜᴀɴᴅʟᴇᴅ ᴀs {media_type.capitalize()} ᴛʏᴘᴇ.**"
            )
        except Exception as e:
            logger.error(f"Error in handle_media_selection: {e}", exc_info=True)
            await callback_query.answer("Aɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ!")
            await callback_query.message.edit_text(
            "**Eʀʀᴏʀ Sᴇᴛᴛɪɴɢ Pʀᴇғᴇʀᴇɴᴄᴇ**\n"
            "**Cᴏᴜʟᴅɴ'ᴛ sᴇᴛ ᴍᴇᴅɪᴀ ᴘʀᴇғᴇʀᴇɴᴄᴇ ʀɪɢʜᴛ ɴᴏᴡ. Tʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ!**"
            )
    except Exception as e:
        logger.error(f"Error in handle_media_selection outer block: {e}", exc_info=True)
        await callback_query.answer("Aɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ!")