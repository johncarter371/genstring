from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝐇𝐞𝐥𝐥𝐨 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐖𝐢𝐜𝐤 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐁𝐨𝐭

Welcome to {}

Welcome to Wick String Session Generator.
I can generate Pyrogram & Telethon String Session for you in easy way

You can use me to generate pyrogram and telethon string session. Use below buttons !

By Wick
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
