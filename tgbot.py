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
from handlers import *
from messages import *
import utils



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )


    

def add_group(update, context):

    for member in update.message.new_chat_members:
        update.message.reply_text(message_select_lang_of_speech, reply_markup=utils.get_button_start(update, context))
        # print(update.message.chat_id)




def test_keyboard(update, context):
    # Узнать message_id этого сообщения, и закинуть его в контекст
    update.message.reply_text(
        message_select_lang_of_speech, 
        reply_markup=utils.get_button_start(update, context))




mybot = Updater(config.TOKEN, use_context=True)

def main():        
    
    # Инициализируем MessageQueue 
    mybot.bot._msg_queue = mq.MessageQueue()
    mybot.bot._is_messages_queued_default=True


    logging.info('Бот запускается.')

    dp = mybot.dispatcher
    

    dp.add_handler(CallbackQueryHandler(serf_menu))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, add_group))  
    dp.add_handler(MessageHandler(Filters.voice, google_utils.voice_to_text))  
    dp.add_error_handler(google_utils.ping_me)
    dp.add_handler(CommandHandler('kb', test_keyboard))
    # dp.add_handler(CallbackQueryHandler(set_delay, pattern='no'))   
    # dp.add_handler(CommandHandler('start', check_if_is_subscriber))      
    # dp.add_handler(CommandHandler('now', send_resume))    
    # dp.add_handler(CallbackQueryHandler(callback_other_handler))   



    # webhook_domain = 'https://translatebot.ru'    
    # PORT = 8443

    # mybot.start_webhook(listen='127.0.0.1',
    #                 port=PORT,
    #                 url_path=config.TOKEN,
    #                 webhook_url=f'{webhook_domain}/{config.TOKEN}',
    #                 cert='/etc/ssl/cert-selfsigned/url_cert.pem',
    #                 key='/etc/ssl/cert-selfsigned/url_private.key'               
    #                 )


    # ssl_certificate /etc/ssl/cert-selfsigned/url_cert.pem;
    # ssl_certificate_key /etc/ssl/cert-selfsigned/url_private.key;

    # mybot.bot.set_webhook(f'{webhook_domain}/{config.TOKEN}')
    
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()