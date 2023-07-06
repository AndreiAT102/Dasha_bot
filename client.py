from aiogram import types, Dispatcher
#from create_bot import dp, bot
#from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=kb_client)
        await message.delete() # удалятор
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Pizza_Dronbot')

#@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

# Регистрация хендлеров для бота и передача хендлеров в основной файл
def register_handlers_client(dp : Dispatcher):
    # регестрирует хендлеры для бота
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
