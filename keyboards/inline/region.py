from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

manzil=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Samarqand viloyati",callback_data="sam"),
        ],
        [
            InlineKeyboardButton(text="Buxoro viloyati", callback_data="bux"),
        ],
        [
            InlineKeyboardButton(text="Toshkent viloyati",callback_data="tosh"),
        ],
        [
            InlineKeyboardButton(text="Jizzax viloyati", callback_data="jiz"),
        ],
        [
            InlineKeyboardButton(text="Sirdaryo viloyati", callback_data="sir"),
        ],
        [
            InlineKeyboardButton(text="Navoiy viloyati", callback_data="nav"),
        ], [
            InlineKeyboardButton(text="Qashqadaryo viloyati",callback_data="qash"),
        ],
        [
            InlineKeyboardButton(text="Surxondaryo viloyati", callback_data="sur"),
        ],
        [
            InlineKeyboardButton(text="Andijon viloyati",callback_data="and"),
        ],
        [
            InlineKeyboardButton(text="Farg'ona viloyati", callback_data="far"),
        ],
        [
            InlineKeyboardButton(text="Namangan viloyati", callback_data="nam"),
        ],
        [
            InlineKeyboardButton(text="Xorazm viloyati", callback_data="xor"),
        ],
        [
            InlineKeyboardButton(text="Qoraqalpog'iston respubliasi", callback_data="qr"),
        ],
        [
            InlineKeyboardButton(text="⬅️BACK", callback_data="back"),
        ],

    ]
)