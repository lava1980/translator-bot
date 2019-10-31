import datetime
import logging
import random
import sqlite3

from telegram import InlineQuery
from telegram.ext import Updater, CallbackQueryHandler, ConversationHandler, CommandHandler, \
        MessageHandler, RegexHandler, Filters, CallbackQueryHandler
from telegram.ext import messagequeue as mq

import config
# 
# from handlers import *
import google_utils

from keyboard import *
from messages import *
from utils import *




def add_group(update, context):
    # Когда бота добавили в группу, записывать данные 
    # в базу не надо. Т.к. это будут данные группы        
    for member in update.message.new_chat_members:  
        context.chat_data['group_chat_id'] = update.message.chat_id
        context.bot.send_message(
            update.message.chat_id, 
            msg_select_lang_of_speech, 
            reply_markup=get_button_list_1(update, context)
            )
        logging.info(
            f'chat_id = {str(update.message.chat_id)};')


def start_message(update, context):  
    data = get_initial_data(update)
    write_initial_data_to_base(data)
    update.message.reply_text(
        msg_select_lang_of_speech, 
        reply_markup=get_button_list_1(update, context))    


def is_voice_or_text(update, context):
    if update.message.voice == None:
        try:
            native_lang = context.user_data['native_lang']  
            logging.info(f'native_lang {native_lang}')          
            native_lang = native_lang.split('-')[0]
            logging.info(f'native_lang {native_lang}')     
            logging.info(f'text = {update.message.text}')     
            group_chat_id = context.chat_data['group_chat_id']
            logging.info(f'group_chat_id = {group_chat_id}')     
        except KeyError:
            logging.info('Возникло исключение Кей Эррор')
            return
        tr_text = google_utils.transl(update.message.text, 'en')
        update.message.reply_text(tr_text)
    else:
        google_utils.voice_to_text(update, context)


def help_message(update, context):
    update.message.reply_text(msg_help)


# TODO Сделать проверку или у собеседника выбран родной язык. Если не выбран, написать 
# в чат сообщение на английском, чтобы выбрал

# TODO когда чел пишет что-то в группу, проверять, или в user_data есть его родной язык

# TODO Сделать, чтобы данные юзера подгружались при его контакте с ботом
# TODO Записать инфу в базу


# Человек кидает сообщение в чат. Оно переводится на тот язык, 
# который указан у человека в качестве родного языка. 





if __name__ == "__main__":
    pass