from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Отправить локацию', request_location=True),
     KeyboardButton(text='Отправить контакт', request_contact=True)]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://youtube.com/@sudoteach')],
    [InlineKeyboardButton(text='Telegram', url='https://t.me/prostooyura')]
])

open_youtube = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Открыть кинопоиск', web_app=WebAppInfo(url='https://hd.kinopoisk.ru/'))]
])

'''inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Корзина', callback_data='basket')],
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])'''