import datetime
import logging
import os
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
    logging.info(f'Состояние chat_id в самом начале функции: {str(context.chat_data)}')      
    user_id = str(update.message.from_user.id)
    add_chat_data_to_context(update, context)
    native_lang = context.chat_data[user_id]
    context.user_data['native_lang'] = native_lang

    if len(context.chat_data) == 1:
        update.message.reply_text(msg_one_chat_member)
        return

    for key in list(context.chat_data.keys()):
        if key != user_id:
            lang = context.chat_data[key].split('-')[0]
            context.user_data['lang'] = lang
            context.chat_data['target_id'] = key
        else:
            continue
        
        logging.info(f'Состояние chat_id перед отправкой сообщения: {str(context.chat_data)}')        
        if update.message.voice == None:      
            tr_text = google_utils.transl(update.message.text, lang)
            context.user_data['user_text'] = tr_text
            send_msg(update, context)            
        else:
            google_utils.voice_to_text(update, context)


def help_message(update, context):
    add_chat_data_to_context(update, context)
    native_lang = context.chat_data[str(update.message.from_user.id)].split('-')[0]
    text = google_utils.transl(msg_help, native_lang)    
    update.message.reply_text(handle_text(text))


# Эту функцию вызывать при начале беседы
def add_chat_data_to_context(update, context):
    user_id = str(update.message.from_user.id)
    if user_id not in context.chat_data or int(user_id) not in context.chat_data:
        users_list = get_chat_users_list(update.message.chat_id) 
        if user_id in users_list:
            for user_id in users_list: 
                try:       
                    native_lang = get_data_cell('native_lang', user_id)
                except TypeError:
                    start_message(update, context)
                    continue
                context.chat_data[user_id] = native_lang
                logging.info(f'Из базы вытянулось значение = {native_lang}') 

        else:            
            start_message(update, context)
              

def send_msg(update, context):
    target_id = context.chat_data['target_id']
    output_voice_or_text = 'text'
    output_voice_or_text = get_data_cell(
        'output_voice_or_text', target_id)
    
    tr_text = context.user_data['user_text']

    if output_voice_or_text == 'voice':        
        lang = context.user_data['lang']
        google_utils.text_to_voice(tr_text, lang)
        context.bot.send_voice(
            update.message.chat_id, open(os.path.join(os.getcwd(), 'output.ogg'), 'rb'))        
        try:
            os.remove(os.path.join(os.getcwd(), 'output.ogg'))
        except Exception as e:
            logging.info('Нет такого файла. Исключение: ' + str(e))
    else:
        update.message.reply_text(tr_text)


def output_format(update, context):
    update.message.reply_text(
        msg_set_output_format, 
        reply_markup=output_format_keyboard())       

    




# TODO исправить КОМАНДЫ, чтобы они не переводились на другой язык

# TODO Сделать чтобы бот реагировал на прямые сообщения в него.
# TODO Удалять сообщение в клавиатурой, после выбора языка









if __name__ == "__main__":
    pass