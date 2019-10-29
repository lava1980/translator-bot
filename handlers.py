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
from messages import *
import utils




def serf_menu(update, context):
    query = update.callback_query
    if query.data == '1':
        context.bot.delete_message(update.message.chat_id, update.message.message_id)
        query.message.reply_text(
            message_select_lang_of_speech, 
            reply_markup=utils.get_button_list_1(update, context))




if __name__ == "__main__":
    pass