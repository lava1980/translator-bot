import datetime
import locale
import logging
import random
import requests
import sqlite3
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

import time

from config import *

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )


# В базе должны быть поля: чат-айди, родной язык и как выдавать инфу -- голосом или текстом.


def create_user_base():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (chat_id text PRIMARY KEY, first_name text, native_lang text, 
                    output_voice_or_text text)'''
                    )
    conn.commit()
    conn.close()


def get_initial_data(update):    
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    initial_user_data = (chat_id, first_name)
    return initial_user_data


def write_initial_data_to_base(data):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (chat_id, first_name) VALUES (?, ?)', data)
    conn.commit()
    conn.close()


def write_entry_to_base(column, entry, id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET {column}=? WHERE chat_id=?', (entry, id))
    conn.commit()
    conn.close()


def list_from_base_column(column): # Возвращает список значений столбца
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT {column} FROM users')
    column_list = cursor.fetchall()
    conn.commit()
    conn.close()
    return column_list # [('-yGIB7rf?NKU0Dk',), (None,)]


def get_data_cell(column, chat_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT {column} FROM users WHERE chat_id=?', (chat_id,))
    date_list = cursor.fetchone()
    conn.commit()
    conn.close()
    return date_list[0]


def select_user_data(chat_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        f'SELECT purpose, purpose_type, purpose_sum, purpose_date, current_sum, \
payday_dates, secret_key, purp_currency, save_in_this_month, \
sum_to_save_in_this_month, role FROM users WHERE chat_id=?',
        (chat_id,))
    date_list = cursor.fetchall()
    conn.commit()
    conn.close()
    # print(date_list[0])   
    return date_list[0]








def lang_list_to_file(texttt):
    with open('lang_list.txt', 'w') as f:
        string_list = texttt.split('\n')
        for string in string_list:
            str_list = string.split('\t')
            f.write(f"'{str_list[-1].split()[0]}': '{str_list[-2]}',\n")



if __name__ == "__main__":
    pass
    











