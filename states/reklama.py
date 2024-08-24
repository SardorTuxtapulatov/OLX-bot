from aiogram.fsm.state import State, StatesGroup

class Adverts(StatesGroup):
    adverts = State()

# class Heshteg(StatesGroup):
#     heshteg = State()

class Users(StatesGroup):
    first_name = State()
    phone_number = State()
    age = State()
    location = State()

class Info(StatesGroup):
    pic = State()
    model = State()
    protsessor = State()
    memory = State()
    videokarta = State()
    operativka = State()
    document = State()
    color = State()
    master = State()
    price = State()
    phone_number = State()
    location = State()