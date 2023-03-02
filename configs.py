# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 27260514))
    API_HASH = os.getenv("API_HASH", "a3bda807c596c557f7ce24ae6e481566")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6133702981:AAFn4AlZL6uR8iQs7nVYasRsGShUMW6zhp4")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "Mdisklink_online_bot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "BQGf9mIAlf9GGdNTfGghiXrCdBkI7tO2Ir_p1NNzB0TybVHLcA_OqhhfChwf5Z6ro9tTqsptcrhIQFnVF5MWyt1CypjNZYUTmztQ9cSJpbYG0_dwz2xqHXkU4kkzobhh1QDmZUm6pC6TJvNgv5oOSAPNA_YuNWFNNv5xLNniodzmG9mdW4LhRPm8j2CrT2-OFPrOda8TFQNqqH296lFSzJlE5PVDZxEOw8sTMODzqh3GFvoGfMGOCNS6lgiXfZeBFIlCIvipcPrDzu_xV3-9oSoGQiNE8FgzfkbY681SmmtzCZuus2piiurYLPBUjTlZ57-3W_B3jIYgpgdP49bImiLNdDCSfwAAAAFtmOFFAQ")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1001871919249))
    BOT_USERNAME = os.getenv("Mdisklink_online_bot")
    BOT_OWNER = int(os.getenv("5393990613"))
#    OWNER_USERNAME = os.getenv("jblink90")
    BACKUP_CHANNEL = os.getenv("mdisklinkonline")
#    GROUP_USERNAME = os.getenv("Netflixmoviesindiaa")
    START_MSG = os.getenv("START_MSG", '''Hᴇʏ! {} 😅,

Mᴇ! Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Bᴏᴛ.🤖

I Cᴀɴ Sᴇᴀʀᴄʜ Mᴏᴠɪᴇꜱ Fᴏʀ Yᴏᴜ.🔍

Mᴀᴅᴇ Wɪᴛʜ ❤ Bʏ

@jayu2980

''')
    START_PHOTO = os.getenv("START_PHOTO", "")
    HOME_TEXT = os.getenv("HOME_TEXT", '''ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ,
ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅''')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", None)
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://jayu99:<password>@cluster0.80ialce.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "5393990613"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 1800))
    MDISK_API = os.getenv("MDISK_API", "hvlk6Uq3knBo2TbFE7d6")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "30"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", '''I ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, i ᴅᴏ ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇxᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.✅

ᴅᴍ ꜰᴏʀ ᴀɴʏ Qᴜᴇʀʏ @jayu2980''')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", '''How to get movies & series from Bot
♻️ 𝖳ɪᴘ ᴛᴏ ᴜ𝗌ᴇ ʙᴏᴛ : ᴅᴏɴ'ᴛ ɪɴᴄʟᴜᴅᴇ ᴀɴʏᴛʜɪɴɢ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ. 

𝖤ɢ: 𝖫ᴜᴄɪғᴇʀ 𝖲𝟶𝟷𝖤𝟶𝟻 ✅

𝖫ᴜᴄɪғᴇʀ 𝖲ᴇᴀ𝗌ᴏɴ 𝟷 𝖤ᴘɪ𝗌ᴏᴅᴇ 𝟻 ❌

𝖡ʟᴀᴄᴋ 𝖶ɪᴅᴏᴡ 𝟸𝟶𝟸𝟷 ✅

𝖡ʟᴀᴄᴋ ᴡɪᴅᴏᴡ 𝟸𝟶𝟸𝟷 𝖧ɪɴᴅɪ ❌

𝖡ʟᴀᴄᴋ𝖶ɪᴅᴏᴡ 𝟸𝟶𝟸𝟷 ❌

○ 𝖨ғ 𝖬ᴏᴠɪᴇ / 𝖲ᴇʀɪᴇ𝗌 𝖭ᴏᴛ 𝖥ᴏᴜɴᴅ 𝖳ʜᴇɴ 𝖱ᴇǫᴜᴇ𝗌ᴛ 𝖨ɴ 𝖦ɪᴠᴇɴ 𝖥ᴏʀᴍᴀᴛ 𝖮ɴʟʏ

👉🏼 𝖭ᴀᴍᴇ | 𝖸ᴇᴀʀ | 𝖱ᴇ𝗌ᴏʟᴜᴛɪᴏɴ | 𝖫ᴀɴɢᴜᴀɢᴇ''')
