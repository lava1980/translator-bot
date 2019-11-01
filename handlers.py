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
    for member in update.message.new_chat_members:  
        logging.info(f'id пользователя = {str(member.id)}')
        logging.info(f'имя пользователя = {str(member.first_name)}')

        if member.is_bot:
            logging.info(f'ЭТО БОТ: id пользователя = {str(member.id)}')
            logging.info(f'ЭТО БОТ: имя пользователя = {str(member.first_name)}')
            context.user_data['group_chat_id'] = update.message.chat_id
            context.bot.send_message(
                update.message.chat_id, 
                msg_select_lang_of_speech, 
                reply_markup=get_button_list_1(update, context)
                )
            logging.info(
                f'chat_id = {str(update.message.chat_id)};')


def start_message(update, context):  
    update.message.reply_text(
        msg_select_lang_of_speech, 
        reply_markup=get_button_list_1(update, context))    


def is_voice_or_text(update, context):  
    user_id = str(update.message.from_user.id)
    try:
        native_lang = data_to_context('native_lang', user_id, context)  
    except TypeError:
        start_message(update, context)
        return
        
    if update.message.voice == None: 
        logging.info(
            f'{update.message.from_user.id}:{update.message.from_user.first_name}:{native_lang}')





        native_lang_t = native_lang.split('-')[0]           
            
        tr_text = google_utils.transl(update.message.text, 'en')
        update.message.reply_text(tr_text)
    else:
        google_utils.voice_to_text(update, context)


def help_message(update, context):
    update.message.reply_text(msg_help)



# TODO сделать обработчики на точки входа в общение: 

# - при добавлении бота в группу: 
# - при начале общения
# - при начале общения напрямую в боте.



# TODO Получить список участников чата
# TODO Проверить или есть у них родной язык
# TODO Если есть -- вытянуть, если нет -- написать сообщение в чат



# TODO Человек пишет что-то в чате:
# TODO 



# TODO Сделать проверку или у собеседника выбран родной язык. Если не выбран, написать 
# в чат сообщение на английском, чтобы выбрал


# TODO Удалять сообщение в клавиатурой, после выбора языка

# TODO когда чел пишет что-то в группу, проверять, или в user_data есть его родной язык

# TODO Сделать, чтобы данные юзера подгружались при его контакте с ботом
# TODO Записать инфу в базу



# Человек кидает сообщение в чат. Оно переводится на тот язык, 
# который указан у человека в качестве родного языка. 







if __name__ == "__main__":
    pass