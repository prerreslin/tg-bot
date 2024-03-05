import asyncio
import logging
import sys
import time
import random
from os import getenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from data.database import Database
from state.tracking_habit import HabitState
from dotenv import load_dotenv
#from keyboards.markups import kb_menu

from handlers.users import router as main_router

load_dotenv()
TOKEN = getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

#All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

dp.include_routers(main_router)


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Дом. справи🧹'),
            KeyboardButton(text='Спорт 🏈'),
        ],
        [
            KeyboardButton(text='Школа'),
        ],
        [
            KeyboardButton(text='Прогулянка 🚶'),
            KeyboardButton(text='Інше'),
        ]
    ],
    resize_keyboard=True
)




advice_options = {
        'Дом. справи🧹': ['Почніть з найважливішого завдання.', 'Розплануйте час для кожної справи.'],
        'Спорт 🏈': ['Запишіться на тренування.', 'Вправляйтесь регулярно.'],
        'Школа': ['Відведіть час на повторення матеріалу.', 'Поставте перед собою малі цілі.'],
        'Прогулянка 🚶': ['Вийдіть на свіжий повітря.', 'Погуляйте в парку або лісі.'],
        'Інше': ['Визначте свої пріоритети.', 'Пам\'ятайте про важливість відпочинку.']
    }



# async def process_advice_callback(callback_query: CallbackQuery):
#     await send_advice(callback_query.message, kb_menu)
        

# async def send_advice(message: Message):
#     button_text = message.text
#     print("Received button text:", button_text)

#     if button_text in advice_options:
#         advice = random.choice(advice_options[button_text])
#         await message.answer(advice, reply_markup=kb_menu)
#     else:
#         await message.answer("Немає поради для цієї кнопки", reply_markup=kb_menu)
        
        
        
# @dp.callback_query(lambda message: message.data in advice_options.keys())
# async def process_advice_callback(callback_query: CallbackQuery):
#     await send_advice(callback_query.message, kb_menu)
    
# @dp.message(F(equals=['Дом. справи🧹', 'Спорт 🏈', 'Школа', 'Прогулянка 🚶', 'Інше']))
# async def process_advice_callback(message: Message):
#     await send_advice(message)


# @dp.message(Command("menu"))
# async def command_menu_handler(message: Message):
#     await message.answer("Виберіть тему для поради:", reply_markup=kb_menu)



async def process_advice_callback(callback_query: CallbackQuery):
    await send_advice(callback_query.message, kb_menu)
         
async def send_advice(message: Message, kb_menu: ReplyKeyboardMarkup):
    button_text = message.text
    print("Received button text:", button_text)

    if button_text in advice_options:
        advice = random.choice(advice_options[button_text])
        await message.answer(advice, reply_markup=kb_menu)
    else:
        await message.answer("Немає поради для цієї кнопки", reply_markup=kb_menu)

@dp.callback_query(lambda message: message.data in advice_options.keys())
async def process_advice_callback(callback_query: CallbackQuery):
    await send_advice(callback_query.message, kb_menu)

@dp.message(Command("menu"))
async def command_menu_handler(message: Message):
    await message.answer("Виберіть тему для поради:", reply_markup=kb_menu)




async def command_error(message: Message):
    await message.answer(f"Команди {message.text} немає!!!")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
