from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import logging
from decouple import config
TOKEN = "5188965067:AAHWiNFde-JFjvAHK7zmJBVRfVZfRs5R4qQ"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message:types.chat_photo):
    await message.replay()

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    qustion = "Сколько будет 2+2?"
    answers = ['1', '2', '4']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=qustion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Rhenj",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )

@dp.message_handler(commands=['quiz1'])
async def quiz_2(message: types.Message):
    qustion = "Какой ответ на главный вопрос Вселенной"
    answers = ['1', '2', '42']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=qustion,
        options=answers,
        is_anonymous=False,
        type='quiz1',
        correct_option_id=1,
        explanation="Так говорил Заратустра",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)






