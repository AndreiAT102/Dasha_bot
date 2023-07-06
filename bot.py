import hashlib
from config import TOKEN

from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle, input_message_content
import os




bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




executor.start_polling(dp, skip_updates=True)