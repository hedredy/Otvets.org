import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode

TOKEN = os.getenv("BOT_TOKEN")  # Берём токен из переменных окружения
ALLOWED_USERS = {954053674, 5743867278}  # ID пользователей, которым бот может отвечать

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

MESSAGE = """🔥 **Добро пожаловать!** 🔥

📢 **Основные каналы:**  
🔹 [OTVETS_ORG](https://t.me/OTVETS_ORG)  
🔹 [OtvetsOrg](https://t.me/OtvetsOrg)  

🤖 **Наш бот:** [OtvetsOrgBot](https://t.me/OtvetsOrgBot)  

💎 **VIP-Пакет:** [Нажмите сюда](https://t.me/+lF57etMQz945NGUy)  

📚 **Полезные материалы:**  
📌 **ОГЭ:** [Перейти](https://t.me/+QvhdA5gBQgU4ZDQy)  
📌 **УС:** [Перейти](https://t.me/+h1HZhKR6Q0I4OTRi)  

⭐ **Отзывы:** [Читать](https://t.me/+VeyLP50u5YRlYzUy)  
"""

@dp.message_handler(commands=["start"])
async def send_message(message: types.Message):
    if message.from_user.id in ALLOWED_USERS:
        sent_message = await message.answer(MESSAGE, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        await sent_message.pin()

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
