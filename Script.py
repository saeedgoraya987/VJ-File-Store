
class script(object):
    START_TXT = """<b><blockquote>Hᴇʟʟᴏ {}, Mʏ Nᴀᴍᴇ <a href='https://t.me/FileStreamerBot'>File Streamer Bot 🖥️</a></blockquote>

I Aᴍ Aᴅᴠᴀɴᴄᴇ Aɴᴅ Pᴏᴡᴇʀғᴜʟʟ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ Wɪᴛʜ Aᴍᴀᴢɪɴɢ Fᴇᴀᴛᴜʀᴇs Jᴜsᴛ Sʜᴀʀᴇ Aɴʏ Vɪᴅᴇᴏ Oʀ Fɪʟᴇ Tʜᴇɴ Sᴇᴇ Mʏ Pᴏᴡᴇʀ 💘</b>"""

    
    CAPTION = """<b>📂 FɪʟᴇNᴀᴍᴇ: {file_name}

⚙️ Sɪᴢᴇ: {file_size}

✨ @FileStreamerBot</b>""" 

    SHORTENER_API_MESSAGE = """<b>💭 Tᴏ Aᴅᴅ Oʀ Uᴘᴅᴀᴛᴇ Yᴏᴜʀ Sʜᴏʀᴛɴᴇʀ Wᴇʙsɪᴛᴇ Aᴘɪ
            
📍 Eɢ: `/api 𝟼LZǫ𝟾𝟻𝟷sXᴏғғғPHᴜɢɪKQǫ`

⚓ Cᴜʀʀᴇɴᴛ Wᴇʙsɪᴛᴇ: `{base_site}`

⚓ Cᴜʀʀᴇɴᴛ Sʜᴏʀᴛᴇɴᴇʀ Aᴘɪ: `{shortener_api}`

🙃 Iғ Yᴏᴜ Wᴀɴᴛ Tᴏ Rᴇᴍᴏᴠᴇ Aᴘɪ Tʜᴇɴ Cᴏᴘʏ Tʜɪs Aɴᴅ Sᴇɴᴅ Tᴏ Bᴏᴛ - </b>`/api None`"""

    CLONE_START_TXT = """<b>Hᴇʟʟᴏ {},ᴍʏ ɴᴀᴍᴇ {},【ɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ】ᴀɴᴅ ᴘᴏᴡᴇʀꜰᴜʟ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ +├ᴄᴜꜱᴛᴏᴍ ᴜʀʟ ꜱʜᴏʀᴛɴᴇʀ ꜱᴜᴘᴘᴏʀᴛ┤+  ᢵᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ sᴜᴘᴘᴏʀᴛ ᢴ ᢾᴀɴᴅ ʙᴇꜱᴛ ᴜɪ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇᢿ

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ᴛʜᴇɴ ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ᴄʟᴏɴᴇ ʙᴏᴛ ғʀᴏᴍ ᴍʏ <a href=https://t.me/vj_botz>ᴘᴀʀᴇɴᴛ</a></b>"""

    ABOUT_TXT = """<b><blockquote>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>

‣ Mʏ Nᴀᴍᴇ: {}
‣ Dᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/BackupRedirect'>Oᴡɴᴇʀ</a> 
‣ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
‣ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ3</a> 
‣ Dᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/'>Mᴏɴɢᴏ Dʙ</a> 
‣ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://app.koyeb.com/'>Kᴏʏᴇʙ</a> 
‣ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: ᴠ2.7.1 [Sᴛᴀʙʟᴇ]></b>
"""

    CABOUT_TXT = """<b>ʜɪ ɪ ᴀᴍ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ + ᴄᴜsᴛᴏᴍ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ɪᴛ ᴍᴇᴀɴs ᴀɴʏ ᴜsᴇʀ ᴄᴀɴ sᴇᴛ ʜɪs ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀɴᴅ + ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ.

🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=tg://user?id={}>ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></b>
"""

    CLONE_TXT = """<b>ʜᴇʟʟᴏ {} 👋

First Send /clone command then follow below steps.
    
1) sᴇɴᴅ <code>/newbot</code> ᴛᴏ @BotFather
2) ɢɪᴠᴇ ᴀ ɴᴀᴍᴇ ꜰᴏʀ ʏᴏᴜʀ ʙᴏᴛ.
3) ɢɪᴠᴇ ᴀ ᴜɴɪǫᴜᴇ ᴜsᴇʀɴᴀᴍᴇ.
4) ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ.
5) ꜰᴏʀᴡᴀʀᴅ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.

ᴛʜᴇɴ ɪ ᴀᴍ ᴛʀʏ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴄᴏᴘʏ ʙᴏᴛ ᴏғ ᴍᴇ ғᴏʀ ʏᴏᴜ ᴏɴʟʏ 😌</b>"""


    HELP_TXT = """<b><blockquote>⍟───[ Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs ]───⍟</blockquote>

✯ /link - Rᴇᴘʟʏ Tᴏ A Vɪᴅᴇᴏ Oʀ Fɪʟᴇ Tᴏ Gᴇᴛ Sʜᴀʀᴇᴀʙʟᴇ Lɪɴᴋ.
✯ /batch - Sᴇɴᴅ Fɪʀsᴛ & Lᴀsᴛ Pᴏsᴛ Lɪɴᴋ & Mᴀᴋᴇ Sᴜʀᴇ Bᴏᴛ Is Aᴅᴍɪɴ Iɴ Cʜᴀɴɴᴇʟ
Eɢ - /batch https://t.me/Op_HackZ/3 https://t.me/Op_HackZ/4
✯ /base_site - Sᴇᴛ Yᴏᴜʀ Cᴜsᴛᴏᴍ Uʀʟ Sʜᴏʀᴛɴᴇʀ Dᴏᴍᴀɪɴ
✯ /api - Sᴇᴛ Yᴏᴜʀ Uʀʟ Sʜᴏʀᴛɴᴇʀ Aᴘɪ
✯ /broadcast - Rᴇᴘʟʏ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Mᴇssᴀɢᴇ Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ (Oᴡɴᴇʀ Oɴʟʏ)</b>"""




    CHELP_TXT = """<b><blockquote>Hᴇʏ {}
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.</blockquote>

🔻 /link - ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ

🔻 /base_site - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ʟɪɴᴋ ᴅᴏᴍᴀɪɴ
ᴇx - /base_site ʏᴏᴜʀᴅᴏᴍᴀɪɴ.ᴄᴏᴍ

🔻 /api - sᴇᴛ ʏᴏᴜʀ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴀᴘɪ
ᴇx - /api ʙᴀᴏᴡɢᴡᴋʟᴀᴀʙᴀᴋʟ

🔻 /broadcast - ʀᴇᴘʟʏ ᴛᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</b>"""

    LOG_TEXT = """<b>#NewUser | @FileStreamerBot
    
🆔 User ID: <code>{}</code>
👤 Username: {}</b>
"""
    RESTART_TXT = """
<b>Bot Restarted!

📅 Date: <code>{}</code>
⏰ Time: <code>{}</code>
🌐 Timezone: <code>Asia/Kolkata</code>
🛠️ Build Status: <code>v2.7.1 [ Stable ]</code></b>"""
