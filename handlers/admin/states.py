from aiogram.fsm.state import State, StatesGroup


class AddTask(StatesGroup):
    waiting_for_title = State()
    waiting_for_type = State()
    waiting_for_link = State()
    waiting_for_reward = State()
class BroadcastState(StatesGroup):
    waiting_message = State()
