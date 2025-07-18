import os
import asyncio
import random
from aiogram import Router,Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from dotenv import load_dotenv
from aiogram.enums import ChatAction
from aiogram.types import InputMediaPhoto, InputMediaVideo
from aiogram.types import Contact
from datetime import datetime

import keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.answer(text='Привет!', reply_markup = kb.main)

@router.message(F.text == 'Привет!')
async def hello(message: Message):
    await message.reply('Как дела?')

@router.message(F.text == 'клавиатура1')
async def hello(message: Message):
    await message.reply('тест клавы 1', reply_markup = kb.main)
@router.message(F.text == 'клавиатура2')
async def hello(message: Message):
    await message.reply('тест клавы 2',  reply_markup=kb.inline_main)


@router.message(F.location)
async def handle_location(message: Message):
    lat, lon = message.location.latitude, message.location.longitude
    await message.answer(f"Ваши координаты: {lat}, {lon}\nhttps://maps.google.com/?q={lat},{lon}")

@router.message(F.text == 'Йоу')
async def wassup(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.reply('Вассап')

@router.message(F.text == "время")
async def send_time(message: Message):
    await message.answer(f"Сейчас: {datetime.now().strftime('%H:%M:%S')}")

@router.message(F.text == 'Голос')
async def voice(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.UPLOAD_VOICE)
    await asyncio.sleep(2)
    await message.reply('Проверка связи!!!')

@router.message(F.sticker)
async def get_sticker_id(message: Message):
    sticker_id = message.sticker.file_id
    await message.answer(f"ID этого стикера: `{sticker_id}`", parse_mode="Markdown")


@router.message(F.text == 'смайлик')
async def smile(message: Message):
    await message.answer("Вот тебе смайлик! \U0001F44D")

@router.message(F.text == "стикер")
async def send_random_sticker(message: Message):
    STICKER_PACK = ['CAACAgQAAxkBAAONaD2mcrFnQ0eLm--SVoikcV46BPwAAvgTAAKIg7hQaViBlEDSgPE2BA',
                    'CAACAgIAAxkBAAOVaD2n9NN--NNVkDdIq-nA6E_NvPsAAooCAAJWnb0KPlJuixPFQGc2BA',
                    'CAACAgIAAxkBAAOTaD2n5Vgoax7kwXIFkQr7zyn_zhUAAltYAAIQVklLnT0fGGtEvWU2BA'
    ]
    random_sticker = random.choice(STICKER_PACK)
    await message.answer_sticker(random_sticker)

@router.message(F.photo)
async def handle_photo(message: Message):
    file_id = message.photo[-1].file_id
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(2)
    await message.answer_photo(file_id, caption = 'Вот твое фото!')

@router.message(F.text == "фото")
async def send_photo_from_url(message: Message):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRK4CJ8sGcxfGWlC7gWv-m_hWaN_6UnHQLFpQ&s"  # Замените на реальный URL
    await message.answer_photo(photo_url, caption="Вот ваше фото из интернета!", has_spoiler=True)

@router.message(F.video)
async def handle_video(message: Message):
    file_id = message.video.file_id
    await message.answer_video(file_id, caption = 'Вот твое видео!')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'{message.from_user.first_name}, вам нужна помощь?')
    await message.answer(f'Ваш ID: {message.from_user.id}')

@router.message(Command('get'))
async def cmd_get(message: Message, command: CommandObject):
    await message.answer(f'Вы ввели команду get с аргументом {command.args}')

@router.message(Command('youtube'))
async def cmd_get(message: Message):
    await message.answer(f'Вы хотите открыть Ютуб',reply_markup = kb.open_youtube)

@router.callback_query(F.data == 'cart')
async def basket(callback: CallbackQuery):
    await callback.message.answer('Ваша корзина пуста.')

@router.message(F.dice)
async def handle_dice(message: Message, bot: Bot):
    emoji = message.dice.emoji
    value = message.dice.value
    await message.reply(f"Ты бросил {emoji} и получил: {value}")
    
@router.message()
async def echo(message: Message):
    await message.answer('Это неизвестная команда.')