from aiogram import types
from keyboards.inline.region import manzil
from keyboards.inline.xaridor import maqsad
from loader import dp
@dp.callback_query_handler(text="ijara")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Siz ijaraga kvartira topmoqchi bolgan manzilni tanlang",reply_markup=manzil)
@dp.callback_query_handler(text="xarid")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("siz xonadon xarid qilmoqchi bolgan joyni tanlang",reply_markup=manzil)
@dp.callback_query_handler(text="yotoq")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(" Siz yotoqxona topmoqchi bolgan manzilni tanlang",reply_markup=manzil)
@dp.callback_query_handler(text="back")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("",reply_markup=maqsad)





