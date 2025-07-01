import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

async def get_chat_id():
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    updates = await bot.get_updates()
    for update in updates:
        if update.message:
            print("Chat ID:", update.message.chat.id)

if __name__ == "__main__":
    asyncio.run(get_chat_id())
