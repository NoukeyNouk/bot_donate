from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, web_app_info, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Все верно', callback_data="authtorization"),
        InlineKeyboardButton(text='Я ошибся', callback_data="retry_waiting_for_phone")
    ]
])

keyboard1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Все верно', callback_data="podtverzdenie"),
        InlineKeyboardButton(text='неа', callback_data="retry_waiting_for_fio")
    ]
])