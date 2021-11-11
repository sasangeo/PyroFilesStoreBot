# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("7849221"))
	API_HASH = os.environ.get("ef483846c6ad56e52008e9e569c4a3b8")
	BOT_TOKEN = os.environ.get("2144767257:AAFanu6g6W7auKllC5Zzvx369No3PmKAA-4")
	BOT_USERNAME = os.environ.get("linkFileShare1_bot")
	DB_CHANNEL = int(os.environ.get("-1001424477540"))
	BOT_OWNER = int(os.environ.get("1747137573"))
	DATABASE_URL = os.environ.get("mongodb+srv://bulanbintang69:bulanbintang69@cluster0.hqhq7.mongodb.net/cluster0?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("-1001569616638")
	LOG_CHANNEL = os.environ.get("1001424477540", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("True", True))
	BROADCAST_AS_COPY = bool(os.environ.get("False", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @AbirHasan2005

👥 **Support Group:** [Linux Repositories](https://t.me/DevsZone)

📢 **Updates Channel:** [Discovery Projects](https://t.me/Discovery_Updates)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @AbirHasan2005

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/AbirHasan2005) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
