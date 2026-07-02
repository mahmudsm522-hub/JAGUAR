from aiogram.fsm.state import State, StatesGroup


class WithdrawState(StatesGroup):
    waiting_wallet_type = State()
    waiting_wallet_address = State()
    waiting_amount = State()
    waiting_confirmation = State()
