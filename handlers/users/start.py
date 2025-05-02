import asyncpg.exceptions
from aiogram import types

from data.config import ADMINS
from keyboards.default.royhatdan_otish import sign_up
from keyboards.inline.sign_up import buttons
from loader import dp,db,bot


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    telegram_id=message.from_user.id
    username=message.from_user.username
    full_name=message.from_user.full_name
    try:
        user =await db.add_user(full_name=full_name,username=username,telegram_id=telegram_id)
    except asyncpg.exceptions.UniqueViolationError:
        user=await db.select_user(telegram_id=telegram_id)

    await message.answer(f"Salom qadrli mijoz , {message.from_user.full_name}!",reply_markup=sign_up)
    msg = "Yangi foydalanuvchi qoshildi\n"
    msg += f"Full_name: {user[1]}\n"
    await bot.send_message(ADMINS[0], msg)

@dp.message_handler(text="Ro'yxatdan o'tish")
async def mijoz_start(message: types.Message):
    await message.answer("Kim sifatida ro'yxatdan o'tmoqchisiz?",reply_markup=buttons)