from aiogram import  types
from keyboards.inline.sotuvchi import xizmatlar
from loader import dp
@dp.callback_query_handler(text="owner")
async def xaridor_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Nima sotmoqchi/ijaraga bermoqchisiz",reply_markup=xizmatlar)