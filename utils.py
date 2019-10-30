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








def lang_list_to_file(texttt):
    with open('lang_list.txt', 'w') as f:
        string_list = texttt.split('\n')
        for string in string_list:
            str_list = string.split('\t')
            f.write(f"'{str_list[-1].split()[0]}': '{str_list[-2]}',\n")



if __name__ == "__main__":
    pass
    











