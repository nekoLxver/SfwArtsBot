from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

start_btn = KeyboardButton(text="/send")
tags_btn = KeyboardButton(text="/tags")
gh_btn = KeyboardButton(text="/repos")

send_keyboard = ReplyKeyboardBuilder()
send_keyboard.row(start_btn, width=1)
send_keyboard.add(tags_btn, gh_btn)
send_keyboard.adjust(2)
