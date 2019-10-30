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
    data = get_initial_data(update)
    write_initial_data_to_base(data)
    
    for member in update.message.new_chat_members:        
        context.bot.send_message(
            update.message.chat_id, message_select_lang_of_speech, reply_markup=get_button_list_1(update, context)
            )
        # update.message.reply_text(
        #     message_select_lang_of_speech, 
        #     reply_markup=get_button_list_1(update, context))
        

def start_message(update, context):  
    data = get_initial_data(update)
    write_initial_data_to_base(data)
    update.message.reply_text(
        message_select_lang_of_speech, 
        reply_markup=get_button_list_1(update, context))    





def is_voice_or_text(update, context):
    if update.message.voice == None:
        try:
            native_lang = context.user_data['native_lang']            
            native_lang = native_lang.split('-')[0]
        except KeyError:
            return
        google_utils.transl(update.message.text, native_lang)
    else:
        google_utils.voice_to_text(update, context)


# TODO Сделать, чтобы данные юзера подгружались при его контакте с ботом
# TODO Записать инфу в базу


if __name__ == "__main__":
    pass