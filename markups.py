from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Дом. справи'),
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

