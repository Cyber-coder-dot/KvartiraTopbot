from aiogram.dispatcher.filters.state import State, StatesGroup

class Data(StatesGroup):
    name=State()
    adress=State()
    floor=State()
    rooms=State()
    area=State()
    price=State()
    contact=State()
