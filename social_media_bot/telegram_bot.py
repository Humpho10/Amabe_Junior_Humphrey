import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv
from content_generator import generate_message

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

async def send_motivational_message():
    bot = Bot(token=bot_token)
    message = generate_message()
    await bot.send_message(chat_id=chat_id, text=message)
    print("✅ Message sent:", message)

if __name__ == "__main__":
    asyncio.run(send_motivational_message())
