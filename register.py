from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    username = State()
    phone_number = State()
    