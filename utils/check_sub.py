from loader import bot
from aiogram import Bot
from typing import Union
from data.config import CHANNELS


async def check(user_id,channel:Union[str,int]):
    bot=Bot.get_current()
    member= await bot.get_chat_member(user_id=user_id,chat_id=channel)
    return member.is_chat_member()