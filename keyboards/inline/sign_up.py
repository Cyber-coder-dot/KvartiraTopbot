from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup

buttons=InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="Xaridor",callback_data="client"),
        ],
        [
            InlineKeyboardButton(text="Sotuvchi",callback_data="owner"),
        ],
    ]
)