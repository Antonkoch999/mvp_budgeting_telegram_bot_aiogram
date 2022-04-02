"""Keyboard for bot."""

from aiogram.types import ReplyKeyboardMarkup

from aiogram_modul.constants import (
    USER_IDS,
    BackEnum,
    CategoryExpenseList,
    CategoryIncomeEnum,
    IncomeExpenseEnum,
)

user_key_board_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
).add(*USER_IDS.values()).row(BackEnum.CANCEL.value)

income_and_expense_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
).add(*IncomeExpenseEnum.list_value()).row(BackEnum.BACK.value)

category_income_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
).add(*CategoryIncomeEnum.list_value()).row(BackEnum.BACK.value)

category_expense_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
).add(*CategoryExpenseList.list_value()).row(BackEnum.BACK.value)

back_keyboard_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
).row(BackEnum.BACK.value)
