# @My_1_Snake_Bot

import random
import logging
import prettytable as pt
from telegram import ParseMode
from aiogram import Bot, Dispatcher, executor, types
import time

# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")

MSG = "{}, выберите действие:"

bot = Bot("5575485223:AAFEi9ZXh7NxiCOVlwjRdWuqSETHISjoWPU")
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
    btn_snake = types.KeyboardButton('/snake')
    btn_out = types.KeyboardButton('/quit')
    btns.add(btn_snake, btn_out)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)


stop = False


@dp.message_handler(commands=['quit'])
async def quit_handler(message: types.Message):
    global stop
    stop = True
    await bot.send_message(message.from_user.id, 'До свидания!',
                           reply_markup=types.ReplyKeyboardRemove())


board = []
keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard.row(types.InlineKeyboardButton("↑", callback_data="up"),
             types.InlineKeyboardButton("↓", callback_data="down"))
keyboard.row(types.InlineKeyboardButton("←", callback_data="left"),
             types.InlineKeyboardButton("→", callback_data="right"))


def place_apple():
    global board
    i = -1
    j = -1
    while i == -1 or j == -1 or board[i][j] != 0:
        i = random.randint(0, 9)
        j = random.randint(0, 14)
    return (i, j)


def copy_table(table1, table2):
    for i in range(len(table1)):
        table2[i] = table1[i]


def make_board(board):
    table = pt.PrettyTable([str(i) for i in range(15)])
    table.header = False
    table.align = "c"
    table.vrules = pt.FRAME
    table.padding_width = 0
    table._min_width = {str(i): 1 for i in range(15)}
    for i in range(10):
        table.add_row([str(j) if j != 0 else "" for j in board[i]])
    return table


snake = [(0, 0) for i in range(3)]
prev_snake = [(0, 0) for i in range(3)]
apple = (0, 0)
direction = 1
prev_direction = 1
callback_query_count = 0


def draw_board(snake):
    global board
    board[apple[0]][apple[1]] = 'A'
    for i in range(len(snake)):
        if snake[i] != (-1, -1):
            if i != len(snake) - 1:
                board[snake[i][0]][snake[i][1]] = "●"
            else:
                if direction == 1:
                    board[snake[i][0]][snake[i][1]] = "▲"
                elif direction == 3:
                    board[snake[i][0]][snake[i][1]] = "▼"
                elif direction == 2:
                    board[snake[i][0]][snake[i][1]] = "◄"
                elif direction == 4:
                    board[snake[i][0]][snake[i][1]] = "►"


@dp.message_handler(commands=['snake'])
async def start_handler(message: types.Message):
    global board, snake, prev_snake, apple, direction, prev_direction, callback_query_count
    board = [[0 for i in range(15)] for j in range(10)]
    snake = [(0, 0) for i in range(3)]
    prev_snake = [(0, 0) for i in range(3)]
    apple = (0, 0)
    direction = 1
    prev_direction = 1
    callback_query_count = 0
    snake[0] = (5, 7)
    snake[1] = (4, 7)
    snake[2] = (3, 7)
    copy_table(snake, prev_snake)
    apple = place_apple()
    draw_board(snake)
    await bot.send_message(message.from_user.id, "Открытие змейки")
    await bot.send_message(message.from_user.id, f'<pre>{make_board(board)}</pre>', parse_mode=ParseMode.HTML, reply_markup=keyboard)


def move():
    global direction, snake, apple, prev_snake
    if direction == 1:
        snake[len(snake) - 1] = (snake[len(snake) - 1][0] - 1, snake[len(snake) - 1][1])
    elif direction == 3:
        snake[len(snake) - 1] = (snake[len(snake) - 1][0] + 1, snake[len(snake) - 1][1])
    elif direction == 2:
        snake[len(snake) - 1] = (snake[len(snake) - 1][0], snake[len(snake) - 1][1] - 1)
    elif direction == 4:
        snake[len(snake) - 1] = (snake[len(snake) - 1][0], snake[len(snake) - 1][1] + 1)
    if snake[len(snake) - 1] == apple:
        snake.insert(0, (-1, -1))
        prev_snake.insert(0, (-1, -1))
        apple = place_apple()


def lose_check():
    global snake
    for i in snake:
        if i != (-1, -1):
            if snake.count(i) > 1:
                return True
            if i[0] not in range(10):
                return True
            if i[1] not in range(15):
                return True
    return False


@dp.callback_query_handler(lambda c: True)
async def callback_calc(query):
    global board, direction, callback_query_count, prev_direction
    callback_query_count += 1
    data = query.data
    if data == "up":
        direction = 1
    elif data == "down":
        direction = 3
    elif data == "left":
        direction = 2
    elif data == "right":
        direction = 4
    if ((direction + 2) - 1) % 4 == prev_direction - 1:
        direction = prev_direction
    else:
        prev_direction = direction
    while callback_query_count <= 1 and not stop and not lose_check():
        time.sleep(0.25)
        for i in snake:
            board[i[0]][i[1]] = 0
        for i in range(len(snake) - 1):
            snake[i] = snake[i + 1]
        move()
        if not lose_check():
            draw_board(snake)
        if lose_check():
            draw_board(prev_snake)
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text=f'<pre>{make_board(board)}\nВы проиграли!</pre>', parse_mode=ParseMode.HTML, reply_markup=keyboard)
        else:
            copy_table(snake, prev_snake)
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text=f'<pre>{make_board(board)}</pre>', parse_mode=ParseMode.HTML, reply_markup=keyboard)
    else:
        callback_query_count -= 1


if __name__ == '__main__':
    executor.start_polling(dp)
