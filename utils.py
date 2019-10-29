import datetime
import locale
import logging
import random
import requests
import sqlite3
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

import time

from config import languages

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )


def lang_list_keyboard():
    inlinekeyboard = [[InlineKeyboardButton('English', callback_data=config.languages['English']),
                        InlineKeyboardButton('Меня пригласили', callback_data='invited_user')]]
    kbd_markup = InlineKeyboardMarkup(inlinekeyboard)
    return kbd_markup











def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu



def get_button_start(update, context):
    button_list = [        
        InlineKeyboardButton('>', callback_data='1'),

        InlineKeyboardButton('English', callback_data=languages['English']),
        InlineKeyboardButton('Russian', callback_data=languages['Russian']),
        InlineKeyboardButton('Polish', callback_data=languages['Polish']),
        InlineKeyboardButton('Bulgarian', callback_data=languages['Bulgarian'])
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    return reply_markup


def get_button_list_1(update, context):
    button_list = [
        InlineKeyboardButton('<', callback_data='1'),
        InlineKeyboardButton('>', callback_data='2'),

        InlineKeyboardButton('jlkjjk', callback_data=languages['English']),
        InlineKeyboardButton('kkljlj', callback_data=languages['Russian']),
        InlineKeyboardButton('Pwwww', callback_data=languages['Polish']),
        InlineKeyboardButton('ccccc', callback_data=languages['Bulgarian'])
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    return reply_markup


if __name__ == "__main__":
    pass











