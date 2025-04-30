from aiogram import Dispatcher
from . must_sub import CheckChannel
from loader import dp
from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(CheckChannel())
