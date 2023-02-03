# @My_1_2048_Bot

import time
import random
import logging
import prettytable as pt
from telegram import ParseMode
from aiogram import Bot, Dispatcher, executor, types

# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")

MSG = "{}, выберите действие:"

bot = Bot("5844671545:AAEfHnpAByFKlCP6Owr2mn2vUvNZgVkFGQY")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Здравствуйте, {user_full_name}! Давайте сыграем.")
    time.sleep(1)
    btns = types.ReplyKeyboardMarkup(row_width=2)
    btn_2048 = types.KeyboardButton('/2048')
    btn_out = types.KeyboardButton('/quit')
    btns.add(btn_2048, btn_out)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)


@dp.message_handler(commands=['quit'])
async def quit_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'До свидания!',
                           reply_markup=types.ReplyKeyboardRemove())


int_table = [[0 for i in range(4)] for j in range(4)]
old_int_table = [[0 for i in range(4)] for j in range(4)]
keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard.row(types.InlineKeyboardButton("↑", callback_data="up"),
             types.InlineKeyboardButton("↓", callback_data="down"))
keyboard.row(types.InlineKeyboardButton("←", callback_data="left"),
             types.InlineKeyboardButton("→", callback_data="right"))


def fill_random_square():
    global int_table
    i = -1
    j = -1
    while i == -1 or j == -1 or int_table[i][j] != 0:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
    chance = random.randint(1, 4)
    if chance != 4:
        int_table[i][j] = 2
    else:
        int_table[i][j] = 4


def copy_table(table1, table2):
    for i in range(len(table1)):
        for j in range(len(table1)):
            table2[i][j] = table1[i][j]


def make_table(int_table):
    table = pt.PrettyTable(["1", "2", "3", "4"])
    table.header = False
    table.hrules = pt.ALL
    table.align = "c"
    table._min_width = {"1": 4, "2": 4, "3": 4, "4": 4}
    for i in range(4):
        table.add_row([str(j) if j != 0 else "" for j in int_table[i]])
    return table


@dp.message_handler(commands=['2048'])
async def start_handler(message: types.Message):
    global int_table, old_int_table
    int_table = [[0 for i in range(4)] for j in range(4)]
    old_int_table = [[0 for i in range(4)] for j in range(4)]
    fill_random_square()
    fill_random_square()
    copy_table(int_table, old_int_table)
    await bot.send_message(message.from_user.id, "Открытие 2048")
    await bot.send_message(message.from_user.id, f'<pre>{make_table(int_table)}</pre>', parse_mode=ParseMode.HTML, reply_markup=keyboard)


def win_check():
    global int_table
    for i in int_table:
        if 2048 in i:
            return True
    return False


def lose_check():
    global int_table
    lose = False
    for i in range(4):
        for j in range(4):
            if int_table[i][j] == 0:
                lose = True
            if i != 3 and j != 3:
                if int_table[i][j] == int_table[i][j + 1]:
                    lose = True
                if int_table[i][j] == int_table[i + 1][j]:
                    lose = True
            elif i != 3:
                if int_table[i][j] == int_table[i + 1][j]:
                    lose = True
            elif j != 3:
                if int_table[i][j] == int_table[i][j + 1]:
                    lose = True
    return lose


@dp.callback_query_handler(lambda c: True)
async def callback_calc(query):
    global int_table, old_int_table
    data = query.data

    if data == "up":
        for j in range(4):
            stone_wall = (-1, -1)
            for i in range(4):
                if int_table[i][j] != 0:
                    while i - 1 != -1 and (int_table[i - 1][j] == 0 or int_table[i - 1][j] == int_table[i][j]):
                        if int_table[i - 1][j] == 0:
                            int_table[i - 1][j] = int_table[i][j]
                            int_table[i][j] = 0
                            i -= 1
                        elif int_table[i - 1][j] == int_table[i][j]:
                            if (i - 1, j) == stone_wall:
                                break
                            int_table[i - 1][j] *= 2
                            int_table[i][j] = 0
                            stone_wall = (i - 1, j)
                            break
    elif data == "down":
        for j in range(4):
            stone_wall = (-1, -1)
            for i in range(3, -1, -1):
                if int_table[i][j] != 0:
                    while i + 1 != 4 and (int_table[i + 1][j] == 0 or int_table[i + 1][j] == int_table[i][j]):
                        if int_table[i + 1][j] == 0:
                            int_table[i + 1][j] = int_table[i][j]
                            int_table[i][j] = 0
                            i += 1
                        elif int_table[i + 1][j] == int_table[i][j]:
                            if (i + 1, j) == stone_wall:
                                break
                            int_table[i + 1][j] *= 2
                            int_table[i][j] = 0
                            stone_wall = (i + 1, j)
                            break
    elif data == "left":
        for i in range(4):
            stone_wall = (-1, -1)
            for j in range(4):
                if int_table[i][j] != 0:
                    while j - 1 != -1 and (int_table[i][j - 1] == 0 or int_table[i][j - 1] == int_table[i][j]):
                        if int_table[i][j - 1] == 0:
                            int_table[i][j - 1] = int_table[i][j]
                            int_table[i][j] = 0
                            j -= 1
                        elif int_table[i][j - 1] == int_table[i][j]:
                            if (i, j - 1) == stone_wall:
                                break
                            int_table[i][j - 1] *= 2
                            int_table[i][j] = 0
                            stone_wall = (i, j - 1)
                            break
    elif data == "right":
        for i in range(3, -1, -1):
            stone_wall = (-1, -1)
            for j in range(3, -1, -1):
                if int_table[i][j] != 0:
                    while j + 1 != 4 and (int_table[i][j + 1] == 0 or int_table[i][j + 1] == int_table[i][j]):
                        if int_table[i][j + 1] == 0:
                            int_table[i][j + 1] = int_table[i][j]
                            int_table[i][j] = 0
                            j += 1
                        elif int_table[i][j + 1] == int_table[i][j]:
                            if (i, j + 1) == stone_wall:
                                break
                            int_table[i][j + 1] *= 2
                            int_table[i][j] = 0
                            stone_wall = (i, j + 1)
                            break

    if int_table != old_int_table:
        fill_random_square()
        if win_check():
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text=f'<pre>{make_table(int_table)}</pre>\nВы победили!', parse_mode=ParseMode.HTML, reply_markup=keyboard)
        elif not lose_check():
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text=f'<pre>{make_table(int_table)}</pre>\nВы проиграли!', parse_mode=ParseMode.HTML, reply_markup=keyboard)
        else:
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text=f'<pre>{make_table(int_table)}</pre>', parse_mode=ParseMode.HTML, reply_markup=keyboard)

        copy_table(int_table, old_int_table)


if __name__ == '__main__':
    executor.start_polling(dp)
