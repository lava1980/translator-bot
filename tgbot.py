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
from keyboard import *
from messages import *
import utils



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )


    





    




mybot = Updater(config.TOKEN, use_context=True)

def main():        
    
    # Инициализируем MessageQueue 
    mybot.bot._msg_queue = mq.MessageQueue()
    mybot.bot._is_messages_queued_default=True


    logging.info('Бот запускается.')
    create_user_base()

    dp = mybot.dispatcher
    


    dp.add_handler(CallbackQueryHandler(lang_menu))

    
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, add_group))  
    dp.add_handler(MessageHandler(Filters.voice, google_utils.voice_to_text))  

    
    dp.add_error_handler(google_utils.ping_me)
    dp.add_handler(CommandHandler('start', start_message))
    dp.add_handler(CommandHandler('help', help_message))
    dp.add_handler(MessageHandler(Filters.text, is_voice_or_text))  
    # dp.add_handler(MessageHandler(Filters.group, is_voice_or_text))  


    # webhook_domain = 'https://translatebot.ru'    
    # PORT = 8443

    # mybot.start_webhook(listen='127.0.0.1',
    #                 port=PORT,
    #                 url_path=config.TOKEN,
    #                 webhook_url=f'{webhook_domain}/{config.TOKEN}'     
    #                 )

    # mybot.bot.set_webhook(f'{webhook_domain}/{config.TOKEN}')
    
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()