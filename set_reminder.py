import time
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from state.tracking_habit import HabitState  # Якщо використовуєте власні стани, то додайте їх імпорт
from data.database import Database
from keyboards._tracking_habit_keyboard import get_tracking_habit_keyboard

router = Router(name=__name__)

# # Ініціалізуємо базу даних
db = Database("database.sql")

db.create_table("habits", {
    "user_id": "INTEGER PRIMARY KEY",
    "habit_name": "TEXT",
    "habit_frequency": "TEXT"
})


# @router.message(Command('set_reminders'))
# async def set_reminders(message: Message, state: FSMContext):
#     user_id = message.from_user.id
    
#     # Отримання звичок користувача з бази даних за його ID
#     habits = db.select("habits", "*", where="user_id=?", values=(user_id,))
    
#     # Перевірка, чи є звички у користувача
#     if habits:
#         # Формуємо текст звичок для відображення у повідомленні
#         habits_text = "\n".join([f"{index + 1}. {habit[1]}" for index, habit in enumerate(habits)])
        
#         await message.answer("Оберіть звичку, для якої ви хочете встановити нагадування:\n" + habits_text)
        
#         # Очікування вибору звички від користувача
#         await state.set_state(HabitState.HabitName.name)  # Встановлюємо ім'я стану
#     else:
#         await message.answer("У вас немає жодної звички. Спочатку додайте звички за допомогою команди /tracking_habit.")
        

# @router.message(HabitState.HabitName.name)  # Використовуємо ім'я стану
# async def process_habit_name(message: Message, state: FSMContext):
#     # Отримуємо назву звички від користувача
#     habit_name = message.text
#     await state.update_data(habit_name=habit_name)
#     await message.answer("Введіть час та день для нагадування звички (наприклад, 14:00 понеділок):")
#     await HabitState.HabitFrequency.name  # Переходимо до наступного стану


# @router.message(HabitState.HabitFrequency.name)  # Використовуємо ім'я стану
# async def process_habit_frequency(message: Message, state: FSMContext):
#     habit_frequency = message.text
    
#     # Введіть валідацію часу і дня
#     valid_time_day = False
#     while not valid_time_day:
#         try:
#             # Перевірка часу і дня на вірність формату
#             habit_time, habit_day = habit_frequency.split()
#             time.strptime(habit_time, '%H:%M')
#             time.strptime(habit_day, '%A')
#             valid_time_day = True
#         except ValueError:
#             await message.answer("Введіть час та день у валідному форматі (наприклад, 14:00 понеділок):")
#             return
    
#     data = await state.get_data()
#     habit_name = data.get('habit_name')
    
#     try:
#         # Додаємо запис про звичку до бази даних
#         db.insert("habits", {"user_id": message.from_user.id, "habit_name": habit_name, "habit_frequency": habit_frequency})
#     except Exception as e:
#         print(f"Помилка при вставці в базу даних: {e}")
#     else:
#         print("Запис успішно вставлено в базу даних.")
    
#     await message.answer(f"Звичка '{habit_name}' успішно збережена з частотою {habit_frequency}.")
#     await state.clear()

# from datetime import datetime


# @router.message(Command('set_reminder'))
# async def set_reminders(message: Message, state: FSMContext):
#     user_id = message.from_user.id
    
#     # Отримання всіх звичок користувача з бази даних за його id
#     habits = db.select("habits", "*", condition=f"user_id={user_id}")
    
#     if not habits:
#         await message.answer("У вас ще немає звичок для встановлення нагадувань.")
#         return
    
#     # Формування списку звичок для вибору
#     habit_choices = [f"{habit[0]}. {habit[1]}" for habit in habits]
#     habit_choices_text = "\n".join(habit_choices)
    
#     await message.answer("Оберіть звичку для встановлення нагадування:\n" + habit_choices_text)
#     await state.set_state(HabitState.SetReminder)

# @router.message(HabitState.SetReminder)
# async def process_set_reminder(message: Message, state: FSMContext):
#     try:
#         habit_id = int(message.text.split('.')[0])  
#     except ValueError:
#         await message.answer("Будь ласка, введіть правильний номер звички.")
#         return
    
#     try:
#         reminder_datetime = datetime.strptime(message.text, "%d.%m.%Y %H:%M")
#     except ValueError:
#         await message.answer("Будь ласка, введіть дату та годину у форматі 'дд.мм.рррр гг:хх'.")
#         return
    
#     # Збереження нагадування у базу даних
#     try:
#         db.insert("reminders", {
#             "user_id": message.from_user.id,
#             "habit_id": habit_id,
#             "reminder_datetime": reminder_datetime.strftime("%Y-%m-%d %H:%M:%S")
#         })
#     except Exception as e:
#         print(f"Помилка при вставці нагадування в базу даних: {e}")
#         await message.answer("Виникла помилка при збереженні нагадування.")
#         return
    
#     await message.answer(f"Нагадування для звички {habit_id} встановлено на {reminder_datetime}.")
#     await state.clear()