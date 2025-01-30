import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode

# Установим уровень логирования для отладки
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")  # Берём токен из переменных окружения
ALLOWED_USERS = {954053674, 5743867278}  # ID пользователей, которым бот может отвечать

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

MESSAGE = """📄 **Официальные ресурсы:**  
🔹 **Основной канал:** OTVETS_ORG  
🔹 **Дополнительный канал:** OtvetsOrg  

🤖 **Наш бот:** OtvetsOrgBot  

💎 **VIP-Пакет:** Перейти  

💸 **Дополнительные материалы:**  
📌 **Ответы ОГЭ:** Перейти  
📌 **Устное собеседование:** Перейти  

⭐ **Отзывы пользователей:** Читать  

👨‍💻 **Администратор:** [@ISupportTelegram](https://t.me/ISupportTelegram)  
🌐 **Официальный сайт:** [hedred.online](https://hedred.online)  
"""

@dp.message_handler(commands=["org"])
async def send_message(message: types.Message):
    # Логирование ID пользователя для проверки
    logging.info(f"Received /org command from user: {message.from_user.id}")

    if message.from_user.id in ALLOWED_USERS:
        logging.info(f"User {message.from_user.id} is allowed. Sending message.")
        await message.answer(MESSAGE, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
    else:
        logging.info(f"User {message.from_user.id} is not authorized.")

async def main():
    try:
        await dp.start_polling()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.info("Bot is starting...")
    asyncio.run(main())
