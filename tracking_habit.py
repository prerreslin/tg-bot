from aiogram.fsm.state import StatesGroup, State

class HabitState(StatesGroup):
    HabitName = State()
    HabitFrequency = State()