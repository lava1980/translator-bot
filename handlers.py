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
import utils




def lang_menu(update, context):
    query = update.callback_query
    if query.data == '1':                
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=message_select_lang_of_speech,
            reply_markup=get_button_list_1(update, context)
        )


    if query.data == '2':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=message_select_lang_of_speech,
            reply_markup=get_button_list_2(update, context)
        )        
        

    if query.data == '3':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=message_select_lang_of_speech,
            reply_markup=get_button_list_3(update, context)
        )        


    if query.data == '4':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=message_select_lang_of_speech,
            reply_markup=get_button_list_4(update, context)
        )        


    if query.data == '5':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=message_select_lang_of_speech,
            reply_markup=get_button_list_5(update, context)
        )        


    if query.data == '6':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=message_select_lang_of_speech,
            reply_markup=get_button_list_6(update, context)
        )        


    if query.data == '7':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=message_select_lang_of_speech,
            reply_markup=get_button_list_7(update, context)
        )        



if __name__ == "__main__":
    pass