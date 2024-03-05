# from aiogram import Router
# from aiogram.types import Message, CallbackQuery
# from aiogram.fsm.context import FSMContext
# from state.tracking_habit import HabitState
# from data.pandas import save_habit_to_csv
# #from data.database import Database
# from aiogram.filters import Command

# from keyboards._tracking_habit_keyboard import get_tracking_habit_keyboard

# import pandas as pd
# import json
# import os
# from aiogram.filters import Command
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram import Router
# from aiogram.types import Message, CallbackQuery
# from aiogram.fsm.context import FSMContext
# from state.tracking_habit import HabitState

# router = Router(name=__name__)

# # Змінена функція збереження звички у форматі JSON
# def save_habit_to_csv(user_id, habit_name, habit_frequency):
#     data = {
#         "user_id": [user_id],
#         "habit_name": [habit_name],
#         "habit_frequency": [habit_frequency]
#     }
#     df = pd.DataFrame(data)
#     df.to_csv('habits.csv', mode='a', index=False, header=not os.path.exists('habits.csv'))
#     print("Запис успішно вставлено в базу даних.")

# def get_user_habits(user_id):
#     if not os.path.exists('habits.csv'):
#         return []
#     df = pd.read_csv('habits.csv')
#     user_habits = df[df['user_id'] == user_id]
#     return user_habits.to_dict(orient='records')

# # Оголошуємо функції для роботи з клавіатурою
# def get_tracking_habit_keyboard(user_id):
#     row = [
#         InlineKeyboardButton(text="Подивитися всі мої звички", callback_data=f"view_all_habits_{user_id}"),
#         InlineKeyboardButton(text="Додати нову звичку", callback_data="add_new_habit")
#     ]
#     rows = [row]
#     markup = InlineKeyboardMarkup(inline_keyboard=rows)
#     return markup

# # Оголошуємо функції для обробки натискання кнопок
# @router.callback_query(lambda query: query.data.startswith('view_all_habits'))
# async def view_all_habits(query: CallbackQuery):
#     user_id = query.from_user.id
#     user_habits = get_user_habits(user_id)
#     if user_habits:
#         habits_text = "\n".join([f"{habit['habit_name']}: {habit['habit_frequency']}" for habit in user_habits])
#         await query.message.answer(f"Ваші звички:\n{habits_text}")
#     else:
#         await query.message.answer("Ви ще не маєте жодних звичок.")
# # Оголошуємо функції для обробки введення даних
# @router.message(HabitState.HabitName)
# async def process_habit_name(message: Message, state: FSMContext):
#     habit_name = message.text
#     await state.update_data(habit_name=habit_name)
#     await message.answer("Введіть частоту цієї звички:")
#     await state.get_state(HabitState.HabitFrequency)

# @router.message(HabitState.HabitFrequency)
# async def process_habit_frequency(message: Message, state: FSMContext):
#     habit_frequency = int(message.text)
#     data = await state.get_data()
#     habit_name = data.get('habit_name')
#     user_id = message.from_user.id
#     save_habit_to_csv(user_id, habit_name, habit_frequency)
#     await message.answer(f"Звичка '{habit_name}' успішно збережена з частотою {habit_frequency}.")
#     await state.clear()

# @router.message(Command('tracking_habit'))
# async def start_tracking_habit(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     keyboard = get_tracking_habit_keyboard(user_id)
#     await message.answer("Виберіть опцію:", reply_markup=keyboard)
#     await state.get_state(HabitState.HabitName)



# db = Database("database.sql")
# db.create_table("habits", {
#     "user_id": "INTEGER",
#     "habit_name": "TEXT",
#     "habit_frequency": "INTEGER"
# })



# @router.message(Command('tracking_habit'))
# async def start_tracking_habit(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     keyboard = get_tracking_habit_keyboard(user_id)
#     await message.answer("Виберіть опцію:", reply_markup=keyboard)
#     await state.set_state(HabitState.HabitName)



# @router.message(HabitState.HabitName)
# async def process_habit_name(message: Message, state: FSMContext):
#     habit_name = message.text
#     await state.update_data(habit_name=habit_name)
#     await message.answer("Введіть частоту звички (наприклад, кількість разів на день або на тиждень):")
#     await state.set_state(HabitState.HabitFrequency)



# @router.message(HabitState.HabitFrequency)
# async def process_habit_frequency(message: Message, state: FSMContext):
#     habit_frequency = int(message.text)
#     data = await state.get_data()
#     habit_name = data.get('habit_name')
#     user_id = message.from_user.id
#     try:
#         db.insert("habits", {"user_id": user_id, "habit_name": habit_name, "habit_frequency": habit_frequency})
#     except Exception as e:
#         print(f"Помилка при вставці в базу даних: {e}")
#     else:
#         print("Запис успішно вставлено в базу даних.")
    
#     await message.answer(f"Звичка '{habit_name}' успішно збережена з частотою {habit_frequency}.")
#     await state.clear()


# @router.callback_query(lambda callback_query: callback_query.data.startswith("view_all_habits"))
# async def process_callback_button(callback_query: CallbackQuery, state: FSMContext):
#     user_id = callback_query.from_user.id
    
#     user_id = callback_query.data.split("_")[-1]
    
#     if str(user_id) == str(callback_query.from_user.id):
#         habits = db.select("habits", "*")
        
#         if habits:
#             habits_text = "\n".join([f"- {habit[1]} (Частота: {habit[2]})" for habit in habits])
#             response_text = f"Ваші звички:\n{habits_text}"
#         else:
#             response_text = "У вас ще немає звичок."
        
#         await callback_query.message.answer(response_text)
#     else:
#         await callback_query.message.answer("У вас немає доступу до цієї інформації.")

# @router.callback_query(lambda callback_query: callback_query.data == "add_new_habit")
# async def process_callback_button(callback_query: CallbackQuery, state: FSMContext):
#     await callback_query.message.answer("Введіть назву нової звички:")
#     await state.set_state(HabitState.HabitName)


