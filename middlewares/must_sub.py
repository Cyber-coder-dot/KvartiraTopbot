from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import CHANNELS
from loader import bot
from aiogram.dispatcher.handler import CancelHandler

from utils.check_sub import check


class CheckChannel(BaseMiddleware):
    async def on_pre_process_manage(self,message:types.Message,data: dict):
        user=message.from_user.id
        natija="Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling\n"
        is_subscribed=True
        for channel in CHANNELS:
            try:
                status = await check(user,channel)
                if not status:
                    is_subscribed=False
                    chat=await bot.get_chat(channel)
                    invite_link=await chat.export_invite_link()
                    natija+=f"<a href='{invite_link}'>{chat.title}<a/>\n"
            except Exception as e:
                print(f"Error checking channel{channel}: {e}")
                continue
        if not is_subscribed:
            await message.answer(
                text=natija,
                parse_mode="HTML",
                disable_web_page_preview=True
            )
            raise CancelHandler()
    async def on_pre_process_callback_query(self,callback_query:types.CallbackQuery,data: dict):
        user=callback_query.from_user.id
        natija="Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling\n"
        is_subscribed=True
        for channel in CHANNELS:
            try:
                status = await check(user,channel)
                if not status:
                    is_subscribed=False
                    chat=await bot.get_chat(channel)
                    invite_link=await chat.export_invite_link()
                    natija+=f"<a href='{invite_link}'>{chat.title}<a/>\n"
            except Exception as e:
                print(f"Error checking channel{channel}: {e}")
                continue
        if not is_subscribed:
            await callback_query.answer(
                text=natija,
                parse_mode="HTML",
                disable_web_page_preview=True
            )
            raise CancelHandler()
