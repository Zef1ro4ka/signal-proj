from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import os
dp = Dispatcher()
chats_id = set()
load_dotenv()
bot = Bot(os.getenv("BOT_TOKEN"))
@dp.message(CommandStart())
async def cmd_start(message: Message):
    chats_id.add(message.chat.id)
    await message.answer("Привіт")



