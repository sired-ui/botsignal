from unittest.mock import call

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils import callback_data

from keyboards.default import mainmenu
from keyboards.inline.choice_buttons import get_symbols_menu
from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message, state:FSMContext):
        await message.answer(f"Неверная команда",reply_markup=mainmenu)


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
