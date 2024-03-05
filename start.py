import re
from aiogram import Router
from state.register import RegisterState
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    ReactionTypeEmoji
)
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
from data.database import Database

from keyboards.user_choice import user_choice


db = Database("database.sql")

db.create_table("users", {
    "id": "INTEGER PRIMARY KEY",
    "telegram_id": "INTEGER",
    "username": "TEXT",
    "phone_number": "TEXT"
})


router = Router(name=__name__)

@router.message(CommandStart())
async def start_register(message: Message):
    await message.answer(f"Привіт. Для продовження виберіть як ви хочите зайти?", reply_markup=user_choice)
    
    # if message.answer == user_choice:
        
    #     @router.message(Command("register"))
    #     async def start_register(message: Message, state: FSMContext):
    #         registered_phones = db.select("users", "phone_number")
    #         if any(message.from_user.username == phone[0] for phone in registered_phones):
    #             await message.answer("Ви вже зареєстровані.")
    #             await message.react([ReactionTypeEmoji(emoji="👍")])
    #         else:
    #             await message.answer(f"Для реєстрації, будь ласка, введіть своє ім'я користувача.")
    #             await state.set_state(RegisterState.username)

    #     # Обробник для введення імені
    #     @router.message(RegisterState.username)
    #     async def register_name(message: Message, state: FSMContext):
    #         # Додайте клавіатуру з однією кнопкою для надсилання номера телефону
    #         # keyboard = get_action_kb()
    #         # await message.answer("Надішліть свій номер телефону, натиснувши на кнопку нижче.", reply_markup=keyboard)
    #         await message.answer(f"Дякую! Тепер надішліть свій номер телефону у форматі +380XXXXXXXXX.")
    #         await state.update_data(username=message.text)
    #         await state.set_state(RegisterState.phone_number)

    #     # Обробник для введення номера телефону
    #     @router.message(RegisterState.phone_number)
    #     async def register_phone(message: Message, state: FSMContext):
    #         if re.match(r"^\+?380\d{9}$", message.text):
    #             await state.update_data(phone_number=message.text)
    #             reg_data = await state.get_data()
    #             reg_name = reg_data.get("username")
    #             reg_phone = reg_data.get("phone_number")
                
    #             # Отримайте ID користувача з Телеграму
    #             telegram_id = message.from_user.id
                
    #             # Додайте користувача до бази даних
    #             msg = f"Ім'я: {reg_name}\nНомер телефону: {reg_phone}"
    #             await message.answer(msg)
                
    #             try:
    #                 db.insert("users", {"telegram_id": telegram_id, "username": reg_name, "phone_number": reg_phone})
    #             except Exception as e:
    #                 print(f"Помилка при вставці в базу даних: {e}")
    #             else:
    #                 print("Запис успішно вставлено в базу даних.")
                
    #             await message.react([ReactionTypeEmoji(emoji="👍")])
                
    #             await state.clear()
    #         else:
    #             await message.answer(f"Номер телефону введено некоректно. Будь ласка, введіть номер у форматі +380XXXXXXXXX.")
    # else:
    #     pass
        

