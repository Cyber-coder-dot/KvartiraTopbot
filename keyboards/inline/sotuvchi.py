from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup
from  loader import dp
xizmatlar=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ijaraga kvartira berish",callback_data="ik"),],
        [InlineKeyboardButton(text="Ijaraga yotoqxona berish",callback_data="iy"),],
        [InlineKeyboardButton(text="Turarjoy sotish",callback_data="ts"),],
    ]
)