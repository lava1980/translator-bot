import datetime
import locale
import logging
import random
import requests
import sqlite3
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

import time

from config import *
# from handlers import start_message

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )


# В базе должны быть поля: чат-айди, родной язык и как выдавать инфу -- голосом или текстом.


def create_user_base():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (user_id text PRIMARY KEY, first_name text, native_lang text, 
                    output_voice_or_text text)
                    '''
                    )
    cursor.execute('''CREATE TABLE IF NOT EXISTS groups
                    (group_id text PRIMARY KEY, user_ids text)         
                   '''
                    )

    conn.commit()
    conn.close()


def write_data_to_base(data):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (user_id, first_name, native_lang) VALUES (?, ?, ?)', data)
    conn.commit()
    conn.close()


def write_initial_data_to_group_table(data):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO groups (group_id) VALUES (?)', data)
    conn.commit()
    conn.close()


def write_entry_to_base(column, entry, id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET {column}=? WHERE user_id=?', (entry, id))
    conn.commit()
    conn.close()


def write_entry_to_group_table(column, entry, group_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f'UPDATE groups SET {column}=? WHERE group_id=?', (entry, group_id))
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


def get_data_cell(column, user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT {column} FROM users WHERE user_id=?', (user_id,))
    date_list = cursor.fetchone()
    conn.commit()
    conn.close()
    return date_list[0]

    
def get_cell_group(column, group_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT {column} FROM groups WHERE group_id=?', (group_id,))
    date_list = cursor.fetchone()
    conn.commit()
    conn.close()
    return date_list[0]


def select_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        f'SELECT purpose, purpose_type, purpose_sum, purpose_date, current_sum, \
payday_dates, secret_key, purp_currency, save_in_this_month, \
sum_to_save_in_this_month, role FROM users WHERE user_id=?',
        (user_id,))
    date_list = cursor.fetchall()
    conn.commit()
    conn.close()
    # print(date_list[0])   
    return date_list[0]


def write_ids_to_base(user_id:str, chat_id:str):
    cell = get_cell_group('user_ids', chat_id)
    if cell == None or cell == '':
        write_entry_to_group_table('user_ids', user_id, chat_id)
    else:
        cell += ', ' + user_id
        write_entry_to_group_table('user_ids', cell, chat_id)
        

def get_chat_users_list(chat_id):
    id_list = get_cell_group('user_ids', chat_id)
    if id_list == None:
        pass
    else:            
        return id_list.split(', ')
       
        
def handle_text(text):  
    if '&#39;' in text:
        text = text.replace('&#39;', "'")    
    if ' / ' in text:
        text = text.replace(' / ', " /")  
    return text

        


def lang_list_to_file(texttt):
    with open('lang_list.txt', 'w') as f:
        string_list = texttt.split('\n')
        for string in string_list:
            str_list = string.split('\t')
            f.write(f"'{str_list[-1].split()[0]}': '{str_list[-2]}',\n")



if __name__ == "__main__":
    # get_chat_users_list('-1001289318869')
    # write_ids_to_base('hjhjkhjhk', '-1001289318869')
    handle_text('Нажмите / hello')
    











