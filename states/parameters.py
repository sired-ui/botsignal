from aiogram.dispatcher.filters.state import StatesGroup, State


class Parameters(StatesGroup):
    typeSignal = State()
    stock = State()
    symbol = State()
    timeframe = State()

class ParforOff(StatesGroup):
    typeSignal = State()
    stock = State()
    symbol = State()
    timeframe = State()