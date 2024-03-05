from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_choice = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Реєстрація"
        ),
        KeyboardButton(
            text="Гість"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="for enterice press this button ")