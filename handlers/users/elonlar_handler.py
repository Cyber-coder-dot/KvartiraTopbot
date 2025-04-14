from aiogram import types
from loader import dp
# Jizzax tumanlari
@dp.callback_query_handler(text="arn")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Arnasoy tumanida e'lonlar topilmadi")
@dp.callback_query_handler(text="bax")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Baxmal tumanida  e'lonlar topilmadi")
@dp.callback_query_handler(text="do's")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Do'stlik tumanida  e'lonlar topilmadi")
@dp.callback_query_handler(text="for")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Forish tumanida e'lonlar topilmadi")
@dp.callback_query_handler(text="g'all")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("G'allaorol tumanida  e'lonlar topilmadi")
@dp.callback_query_handler(text="shr")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Sharof Rashidov tumanida e'lonlar topilmadi")
@dp.callback_query_handler(text="mir")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Mirzacho'l tumanida e'lonlar topilmadi")
@dp.callback_query_handler(text="paxt")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Paxtakor tumanida  e'lonlar topilmadi")
@dp.callback_query_handler(text="yangob")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Yangiobod tumanida e'lonlar topilmadi")
@dp.callback_query_handler(text="zom")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Zomin tumanida e'lonlar topilmadi")
@dp.callback_query_handler(text="zaf")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Zafarobod tumanida  e'lonlar topilmadi")
@dp.callback_query_handler(text="zarb")
async def region_handler(callback:types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Zarbdor tumanida e'lonlar topilmadi")