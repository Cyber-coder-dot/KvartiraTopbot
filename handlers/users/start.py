from aiogram import types
from keyboards.default.royhatdan_otish import sign_up
from keyboards.inline.sign_up import buttons
from loader import dp


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=sign_up)

@dp.message_handler(text="Ro'yxatdan o'tish")
async def mijoz_start(message: types.Message):
    await message.answer("Kim sifatida ro'yxatdan o'tmoqchisiz?",reply_markup=buttons)