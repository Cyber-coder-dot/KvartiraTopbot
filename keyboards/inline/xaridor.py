from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

maqsad=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ijaraga kvartira olish",callback_data="ijara"),
        ],
        [
            InlineKeyboardButton(text="Xonadon sotib olish", callback_data="xarid"),
        ],
        [
            InlineKeyboardButton(text="Yotoqxona topish",callback_data="yotoq"),
        ],

    ]
)



