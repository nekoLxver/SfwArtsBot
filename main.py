from aiogram.types import Message
from aiogram import F
from aiogram.filters import Command
from random import randint
from aiogram import Bot, Dispatcher
from key_boards import send_keyboard as sk
from custom_filters import TagMaker as tm
from api_work import get_image as gt, tags_list as tl
from dotenv import load_dotenv
import time
import os


load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_cmd(message: Message):
    await message.answer(text=os.getenv('START_MESSAGE'), reply_markup=sk.as_markup(resize_keyboard=True))


@dp.message(Command(commands=['tags']))
async def tags_cmd(message: Message):
    await message.answer(text=os.getenv('TAGS_INFO'))


@dp.message(Command(commands=['repos']))
async def repos_cmd(message: Message):
    await message.answer(text=os.getenv('REPOS_LINK'))


@dp.message(F.text == '/send')
async def send_cmd(message: Message):
    print('There!')
    url = os.getenv('URL')
    rand_num = randint(0, len(tl) - 1)
    url += f'/{tl[rand_num]}'
    print(url)
    data = gt(url)
    print(data)
    if data:
        print(data)
        await message.answer_photo(data['results'][0]['url'])


@dp.message(Command(commands=['send']), tm())
async def send_tag_cmd(message: Message, tag=None, count=None):
    print("Here!", tag, count)
    url = os.getenv('URL')
    if tag:
        url += f'/{tag}'
    if count:
        for i in range(int(count)):
            data = gt(url)
            if data:
                await message.answer_photo(data['results'][0]['url'])
            time.sleep(0.3)
    else:
        data = gt(url)
        if data:
            await message.answer_photo(data['results'][0]['url'])


@dp.message()
async def other_msg(message: Message):
    await message.answer("Не понимаю о чем вы \..[Х_Х]../")


dp.run_polling(bot)