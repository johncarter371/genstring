from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝐇𝐞𝐥𝐥𝐨 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐖𝐢𝐜𝐤 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐁𝐨𝐭

𝐖𝐞𝐥𝐜𝐨𝐦𝐞 {}

𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐖𝐢𝐜𝐤 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫.
𝐈 𝐜𝐚𝐧 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 & 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐟𝐨𝐫 𝐲𝐨𝐮 𝐢𝐧 𝐞𝐚𝐬𝐲 𝐰𝐚𝐲

𝐘𝐨𝐮 𝐜𝐚𝐧 𝐮𝐬𝐞 𝐦𝐞 𝐭𝐨 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐩𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐚𝐧𝐝 𝐭𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧. 𝐔𝐬𝐞 𝐛𝐞𝐥𝐨𝐰 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 ❗

𝐁𝐲 𝐖𝐢𝐜𝐤
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔗 Start Generating Session ", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔗 Start Generating Session ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔗 Start Generating Session ", callback_data="generate")],
        
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by Wick

Source Code : [Click Here](https://github.com/johncarter371/StringSessionBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : Mr.Wick
    """
