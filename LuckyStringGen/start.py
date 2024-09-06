from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID

# Renaming the filter function to avoid conflict with built-in names
def command_filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(command_filter("start"))
async def start(bot: Client, msg: Message):
    me = (await bot.get_me()).mention  # Changed variable name to avoid shadowing built-in function name 'me'
    await msg.reply_text(
        text=f"""ʜᴇʏ {msg.from_user.mention},

ᴛʜɪs ɪs {me},
ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀʟʟ ᴛʏᴘᴇ ᴏғ sᴇssɪᴏɴs..
ᴄʟɪᴄᴋ ᴏɴ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ!

ᴍᴀᴅᴇ ʙʏ: [𝐋𝚄𝙲𝙺𝚈 𝐑𝙰𝙹𝙰](https://t.me/The_LuckyX) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝙶𝙴𝙽𝚁𝙰𝚃𝙴 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝐒𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/LuckyXSupport"),
                    InlineKeyboardButton("𝐔𝙿𝙳𝙰𝚃𝙴", url="https://t.me/LuckyXUpdate")
                 ],
                 [
                    InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴", url="https://github.com/The-LuckyX/LuckyStringGen")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
