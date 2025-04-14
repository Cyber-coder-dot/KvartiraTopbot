from aiogram import types
from keyboards.inline.sign_up import buttons
from keyboards.inline.xaridor import maqsad
from loader import dp



@dp.callback_query_handler(text="client")
async def xaridor_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Bu botdan nima maqsadda foydalanyapsiz?",reply_markup=maqsad)

