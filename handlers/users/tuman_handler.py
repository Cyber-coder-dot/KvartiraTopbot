from aiogram import types
from loader import dp
from keyboards.inline.tuman import tumanlar_jizzax
from keyboards.inline.tuman import tumanlar_buxoro
from keyboards.inline.tuman import tumanlar_navoiy
from keyboards.inline.tuman import tumanlar_xorazm
from keyboards.inline.tuman import tumanlar_samarqand
from keyboards.inline.tuman import tumanlar_sirdaryo
from keyboards.inline.tuman import tumanlar_surxondaryo
from keyboards.inline.tuman import tumanlar_andijon
from keyboards.inline.tuman import tumanlar_fargona
from keyboards.inline.tuman import tumanlar_namangan
from keyboards.inline.tuman import tumanlar_qashqadaryo
from keyboards.inline.tuman import tumanlar_qoraqalpogiston
from keyboards.inline.tuman import tumanlar_toshkent

from keyboards.inline.region import manzil
@dp.callback_query_handler(text="sam")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_samarqand)
@dp.callback_query_handler(text="tosh")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_toshkent)
@dp.callback_query_handler(text="jiz")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_jizzax)
@dp.callback_query_handler(text="sir")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_sirdaryo)
@dp.callback_query_handler(text="qash")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_qashqadaryo)
@dp.callback_query_handler(text="nam")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_namangan)
@dp.callback_query_handler(text="and")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_andijon)
@dp.callback_query_handler(text="sur")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_surxondaryo)
@dp.callback_query_handler(text="qr")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_qoraqalpogiston)
@dp.callback_query_handler(text="far")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_fargona)
@dp.callback_query_handler(text="xor")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_xorazm)
@dp.callback_query_handler(text="nav")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_navoiy)
@dp.callback_query_handler(text="bux")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Tuman tanlang",reply_markup=tumanlar_buxoro)
@dp.callback_query_handler(text="backr")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Manzilni  tanlang",reply_markup=manzil)
