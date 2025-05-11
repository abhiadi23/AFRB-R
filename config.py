import re, os, time
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","")
    PORT = os.environ.get("PORT", "8000")
 
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    START_STICKER   = "CAACAgUAAyEFAASUwGgHAAIYBmgcl2iAiZGVsNreqpw1OFvJnBdWAAIxBAACCCbhVIWB74mXKv-gNgQ"
    FORCE_PIC   = os.environ.get("FORCE_PIC", "")
    ADMINS       = [int(admins) if id_pattern.search(admins) else admins for admins in os.environ.get('ADMINS', '').split()]
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', '').split(', ')
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")
    DUMP_CHANNEL = os.environ.get("DUMP_CHANNEL", "")
    DUMP = True
    BOT_CHANNEL_NAME = os.environ.get("BOT_CHANNEL_NAME", "")
    BOT_CHANNEL_USERNAME = os.environ.get("BOT_CHANNEL_USERNAME", "")
    SUPPORT_CHANNEL_NAME = os.environ.get("SUPPORT_CHANNEL_NAME", "")
    SUPPORT_CHANNEL_USERNAME = os.environ.get("SUPPORT_CHANNEL_USERNAME", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    BOT_NAME = os.environ.get("BOT_NAME", "")
    OWNER_NAME = os.environ.get("OWNER_NAME", "")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
    DEVELOPER_USERNAME = os.environ.get("DEVELOPER_USERNAME", "")
    DEVELOPER_NAME = os.environ.get("DEVELOPER_NAME", "")
    #TOKEN_API = ""
    TOKEN_API = ""
    SHORTENER_URL = "https://droplink.co/api"
    TOKEN_ID_LENGTH = 8
    SHORTENER_TOKEN_GEN = 100
    UPI_ID = ""
    VERSION = "4.1.2"
    LAST_UPDATED = "2025-05-01"
    DB_VERSION = "1.4.2"
    FLOODWAIT_RETRIES = 999
    FLOODWAIT_WAIT = 30
    DEFAULT_TOKEN = 100
    UPDATE_TIME = 7
    LEADERBOARD_DELETE_TIMER = 30
    RENAMED_DELETE_TIMER = 120
    ADMIN_OR_PREMIUM_TASK_LIMIT = 5
    NORMAL_TASK_LIMIT = 3
    ADMIN_USAGE_MODE = True
    GLOBAL_TOKEN_MODE = True
    GLOBAL_TOKEN_EXPIRY = None
    SESSION_NAME = "Renamer"
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))
    WEBHOOK_PORT = os.environ.get("WEBHOOK_PORT", "8000")


class Txt(object):
        
    START_TXT = """<b>ʜᴇʏ! {}  

» ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ! ᴡʜɪᴄʜ ᴄᴀɴ ᴀᴜᴛᴏʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴀʟsᴏ sᴇǫᴜᴇɴᴄᴇ ᴛʜᴇᴍ ᴘᴇʀғᴇᴄᴛʟʏ</b>"""
    
    FILE_NAME_TXT = f"""<b>» <u>sᴇᴛᴜᴘ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ғᴏʀᴍᴀᴛ</u></b>

<b>ᴠᴀʀɪᴀʙʟᴇꜱ :</b>
➲ ᴇᴘɪꜱᴏᴅᴇ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴇᴘɪꜱᴏᴅᴇ ɴᴜᴍʙᴇʀ  
➲ ǫᴜᴀʟɪᴛʏ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ǫᴜᴀʟɪᴛʏ  
➲ sᴇᴀsᴏɴ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ sᴇᴀsᴏɴ  
➲ ᴀᴜᴅɪᴏ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴀᴜᴅɪᴏ
➲ ᴄʜᴀᴘᴛᴇʀ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴄʜᴀᴘᴛᴇʀ

<b>‣ ᴇxᴀᴍᴘʟᴇ :</b>  
<code>/autorename [Sseason-episode] One Piece [quality] [audio] @GenAnimeOfc</code>

<b>‣ /autorename:</b>  
ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ꜰɪʟᴇꜱ ʙʏ ᴜꜱɪɴɢ 'ᴇᴘɪꜱᴏᴅᴇ', 'sᴇᴀsᴏɴ', 'ᴀᴜᴅɪᴏ', 'ʀᴇsᴏʟᴜᴛɪᴏɴ' ᴀɴᴅ 'ǫᴜᴀʟɪᴛʏ' ᴠᴀʀɪᴀʙʟᴇꜱ ɪɴ ʏᴏᴜʀ ꜰᴏʀᴍᴀᴛ ᴛᴇxᴛ.  
ᴛʜᴇʏ ᴡɪʟʟ ʙᴇ ᴇxᴛʀᴀᴄᴛᴇᴅ ꜰʀᴏᴍ ᴛʜᴇ ᴏʀɪɢɪɴᴀʟ ꜰɪʟᴇɴᴀᴍᴇ ᴀɴᴅ ᴜꜱᴇᴅ ɪɴ ʀᴇɴᴀᴍɪɴɢ.
"""

    ABOUT_TXT = f"""<b>❍ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/{Config.BOT_USERNAME}">{Config.BOT_NAME}</a>
❍ ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href="https://t.me/{Config.DEVELOPER_USERNAME}">{Config.DEVELOPER_NAME}</a>
❍ ᴏᴡɴᴇʀ : <a href="https://t.me/{Config.OWNER_USERNAME}">{Config.OWNER_NAME}</a>
❍ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>
❍ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
❍ ʜᴏꜱᴛᴇᴅ ᴏɴ : <a href="https://t.me/{Config.DEVELOPER_USERNAME}">ᴠᴘs</a>
❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/{Config.BOT_CHANNEL_USERNAME}">{Config.BOT_CHANNEL_NAME}</a>
❍ ʜᴇʟᴘ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/{Config.SUPPORT_CHANNEL_USERNAME}">{Config.SUPPORT_CHANNEL_NAME}</a>

➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍᴇ.</b>"""

    
    THUMBNAIL_TXT = """<b><u>» ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>
    
➲ /start: ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /del_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /view_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /get_thumb: ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴇxᴛʀᴀᴄᴛ ᴛʜᴜᴍʙɴᴀɪʟ ғʀᴏᴍ ᴏᴛʜᴇʀ ᴠɪᴅᴇᴏs ᴏʀ ᴅᴏᴄ.

ɴᴏᴛᴇ: ɪꜰ ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ɪɴ ʙᴏᴛ ᴛʜᴇɴ, ɪᴛ ᴡɪʟʟ ᴜꜱᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ᴛʜᴇ ᴏʀɪɢɪɴɪᴀʟ ꜰɪʟᴇ ᴛᴏ ꜱᴇᴛ ɪɴ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ"""

    CAPTION_TXT = """<b><u>» ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ</u></b>
    
<b>ᴠᴀʀɪᴀʙʟᴇꜱ :</b>         
ꜱɪᴢᴇ: {filesize}
ᴅᴜʀᴀᴛɪᴏɴ: {duration}
ꜰɪʟᴇɴᴀᴍᴇ: {filename}

➲ /set_caption: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
➲ /see_caption: ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
➲ /del_caption: ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.

» ꜰᴏʀ ᴇx:- /set_caption ꜰɪʟᴇ ɴᴀᴍᴇ: {filesize}"""

    PROGRESS_BAR = """\n
<b>» Sɪᴢᴇ</b> : {1} | {2}
<b>» Dᴏɴᴇ</b> : {0}%
<b>» Sᴘᴇᴇᴅ</b> : {3}/s
<b>» ETA</b> : {4} """
    
    
    DONATE_TXT = f"""<blockquote> ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ</blockquote>

<b><i>💞  ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴏᴜʀ ʙᴏᴛ ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴅᴏɴᴀᴛᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ₹𝟷𝟶, ₹𝟸𝟶, ₹𝟻𝟶, ₹𝟷𝟶𝟶, ᴇᴛᴄ.</i></b>

ᴅᴏɴᴀᴛɪᴏɴs ᴀʀᴇ ʀᴇᴀʟʟʏ ᴀᴘᴘʀᴇᴄɪᴀᴛᴇᴅ ɪᴛ ʜᴇʟᴘs ɪɴ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ

 <u>ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴅᴏɴᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴜᴘɪ</u>

 ᴜᴘɪ ɪᴅ : <code>{Config.UPI_ID}</code>

ɪғ ʏᴏᴜ ᴡɪsʜ ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴜs ss
ᴏɴ - @{Config.OWNER_USERNAME}"""

    PREMIUM_TXT = """<b>ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ ᴀɴᴅ ᴇɴJᴏʏ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs:
○ ᴜɴʟɪᴍɪᴛᴇᴅ Rᴇɴᴀᴍɪɴɢ.
○ ɴᴏ ᴀᴅꜱ.
○ ᴇᴀʀʟʏ Aᴄᴄᴇss.
○ ᴍᴏʀᴇ ᴘʀɪᴏʀɪᴛʏ

• ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.

➲ ғɪʀsᴛ sᴛᴇᴘ : ᴘᴀʏ ᴛʜᴇ ᴀᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴘʟᴀɴ ᴛᴏ ᴛʜᴇ ᴜᴘɪ ɪᴅ ᴏʀ Qʀ.
➲ secoɴᴅ sᴛᴇᴘ : ᴛᴀᴋᴇ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ sʜᴀʀᴇ ɪᴛ ᴅɪʀᴇᴄᴛʟʏ ʜᴇʀᴇ: @darkxside78, @Jas_Mehra ᴏʀ @Blakite_Ravii
➲ ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇ sᴛᴇᴘ : ᴏʀ ᴜᴘʟᴏᴀᴅ ᴛʜᴇ sᴄʀᴇᴇɴsʜᴏᴛ ʜᴇʀᴇ ᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ /bought ᴄᴏᴍᴍᴀɴᴅ. [ᴍᴀʏ ɴᴏᴛ ᴡᴏʀᴋ ᴘʀᴏᴘᴇʀʟʏ]

Yᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ᴡɪʟʟ ʙᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴀғᴛᴇʀ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ</b>"""

    PREPLANS_TXT = """<b>👋 ʜᴇʟʟᴏ ʙʀᴏ,
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u> :

Pʀɪᴄɪɴɢ:
➜ ᴅᴀɪʟʏ ᴘʀᴇᴍɪᴜᴍ: ₹10/ᴅᴀʏ
➜ ᴍᴏɴᴛʜʟʏ ᴘʀᴇᴍɪᴜᴍ: ₹80/ᴍᴏɴᴛʜ
➜ ʟɪꜰᴇᴛɪᴍᴇ ᴘʀᴇᴍɪᴜᴍ: ₹459
➜ ғᴏʀ ʙᴏᴛ ʜᴏsᴛɪɴɢ: [ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ](https://t.me/{Config.DEVELOPER_USERNAME})

➲ ᴜᴘɪ ɪᴅ - <code>{Config.UPI_ID}</code>

‼️ᴜᴘʟᴏᴀᴅ ᴛʜᴇ ᴘᴀʏᴍᴇɴᴛ sᴄʀᴇᴇɴsʜᴏᴛ ʜᴇʀᴇ ᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ /bought ᴄᴏᴍᴍᴀɴᴅ.</b>"""
    
    HELP_TXT = """<b>ʜᴇʀᴇ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ ɪᴍᴘᴏʀᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:

ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs🫧

ʀᴇɴᴀᴍᴇ ʙᴏᴛ ɪꜱ ᴀ ʜᴀɴᴅʏ ᴛᴏᴏʟ ᴛʜᴀᴛ ʜᴇʟᴘꜱ ʏᴏᴜ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ.

➲ /autorename: ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ.
➲ /ssequence: ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ.
➲ /ssequence: ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ.
➲ /metadata: ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ.
➲ /help: ɢᴇᴛ ǫᴜɪᴄᴋ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ.</b>"""

    SEND_METADATA = """
<b>--Mᴇᴛᴀᴅᴀᴛᴀ Sᴇᴛᴛɪɴɢs:--</b>

➜ /metadata: Tᴜʀɴ ᴏɴ ᴏʀ ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ.

<b>Description</b> : Mᴇᴛᴀᴅᴀᴛᴀ ᴡɪʟʟ ᴄʜᴀɴɢᴇ MKV ᴠɪᴅᴇᴏ ғɪʟᴇs ɪɴᴄʟᴜᴅɪɴɢ ᴀʟʟ ᴀᴜᴅɪᴏ, sᴛʀᴇᴀᴍs, ᴀɴᴅ sᴜʙᴛɪᴛʟᴇ ᴛɪᴛʟᴇs."""


    SOURCE_TXT = f"""
<b>ʜᴇʏ,
ᴛʜɪs ɪs ᴀɴ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʙᴏᴛ,
ᴄʀᴇᴀᴛᴇᴅ ʙʏ [{Config.BOT_CHANNEL_NAME}](https://t.me/{Config.BOT_CHANNEL_USERNAME}).</b>

<b>ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ :
[ᴩʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram)
[ᴩʏᴛʜᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-ʙᴏᴛ](https://github.com/python-telegram-bot/python-telegram-bot)
ᴀɴᴅ ᴜsɪɴɢ [ᴍᴏɴɢᴏ](https://cloud.mongodb.com) ᴀs ᴅᴀᴛᴀʙᴀsᴇ.</b>"""

    META_TXT = """
**ᴍᴀɴᴀɢɪɴɢ ᴍᴇᴛᴀᴅᴀᴛᴀ ғᴏʀ ʏᴏᴜʀ ᴠɪᴅᴇᴏs ᴀɴᴅ ғɪʟᴇs**

**ᴠᴀʀɪᴏᴜꜱ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

- **ᴛɪᴛʟᴇ**: Descriptive title of the media.
- **ᴀᴜᴛʜᴏʀ**: The creator or owner of the media.
- **ᴀʀᴛɪꜱᴛ**: The artist associated with the media.
- **ᴀᴜᴅɪᴏ**: Title or description of audio content.
- **ꜱᴜʙᴛɪᴛʟᴇ**: Title of subtitle content.
- **ᴠɪᴅᴇᴏ**: Title or description of video content.
- **ᴇɴᴄᴏᴅᴇ ʙʏ**: The person who encoded the video.
- **ᴄᴜꜱᴛᴏᴍ ᴛᴀɢ**: Any Title.
- **ᴄᴏᴍᴍᴇɴᴛ**: Any Title.
 

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ:**
➜ /metadata: Turn on or off metadata.

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ꜱᴇᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

➜ /settitle: Set a custom title of media.
➜ /setauthor: Set the author.
➜ /setartist: Set the artist.
➜ /setaudio: Set audio title.
➜ /setsubtitle: Set subtitle title.
➜ /setvideo: Set video title.
➜ /setencoded_by: Set encoded by title.
➜ /setcustom_tag: Set custom tag title.
➜ /setcomment: Set comment title.

**ᴇxᴀᴍᴘʟᴇ:** /settitle Your Title Here

**ᴜꜱᴇ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴇɴʀɪᴄʜ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴡɪᴛʜ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ᴍᴇᴛᴀᴅᴀᴛᴀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ!**
"""
