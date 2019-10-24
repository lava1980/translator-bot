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
import utils



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'tgbot.log'
                    )


    






mybot = Updater(config.TOKEN, use_context=True)

def main():        
    
    # Инициализируем MessageQueue 
    mybot.bot._msg_queue = mq.MessageQueue()
    mybot.bot._is_messages_queued_default=True


    logging.info('Бот запускается.')

    dp = mybot.dispatcher
    

    
  
    dp.add_handler(MessageHandler(Filters.voice, utils.voice_to_text))  
    dp.add_error_handler(utils.ping_me)
    # dp.add_handler(CallbackQueryHandler(set_delay, pattern='no'))   
    # dp.add_handler(CommandHandler('start', check_if_is_subscriber))      
    # dp.add_handler(CommandHandler('now', send_resume))    
    # dp.add_handler(CallbackQueryHandler(callback_other_handler))   



    # webhook_domain = 'https://python-developer.ru'    
    # PORT = 5000

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