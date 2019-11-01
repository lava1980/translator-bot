import logging
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup

from config import buttons_pages, languages
from google_utils import transl
from messages import *
from utils import write_data_to_base, write_initial_data_to_group_table, \
    get_cell_group



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )



def lang_list_keyboard():
    inlinekeyboard = [
        [InlineKeyboardButton('English', callback_data=languages['English']),
        InlineKeyboardButton('Меня пригласили', callback_data='invited_user')]]
    kbd_markup = InlineKeyboardMarkup(inlinekeyboard)
    return kbd_markup


def inlinekeyboard_list(kb_number):   
    lang_list = buttons_pages[kb_number]
    inlinekb_list = []
    for language in lang_list:
        inlinekb_list.append(
            InlineKeyboardButton(language, callback_data=languages[language])
            )
    return inlinekb_list


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


def get_button_list_1(update, context):
    button_list = inlinekeyboard_list(1)
    menu = build_menu(button_list, n_cols=2)
    menu.insert(0, [InlineKeyboardButton('>', callback_data='2')])
    reply_markup = InlineKeyboardMarkup(menu)
    return reply_markup


def get_button_list_2(update, context):
    button_list = inlinekeyboard_list(2)
    menu = build_menu(button_list, n_cols=2)
    menu.insert(0, [InlineKeyboardButton('<', callback_data='1'),
                    InlineKeyboardButton('>', callback_data='3')])    
    reply_markup = InlineKeyboardMarkup(menu)
    return reply_markup


def get_button_list_3(update, context):
    button_list = inlinekeyboard_list(3)
    menu = build_menu(button_list, n_cols=2)
    menu.insert(0, [InlineKeyboardButton('<', callback_data='2'),
                    InlineKeyboardButton('>', callback_data='4')])    
    reply_markup = InlineKeyboardMarkup(menu)
    return reply_markup


def get_button_list_4(update, context):
    button_list = inlinekeyboard_list(4)
    menu = build_menu(button_list, n_cols=2)
    menu.insert(0, [InlineKeyboardButton('<', callback_data='3'),
                    InlineKeyboardButton('>', callback_data='5')])    
    reply_markup = InlineKeyboardMarkup(menu)
    return reply_markup


def get_button_list_5(update, context):
    button_list = inlinekeyboard_list(5)
    menu = build_menu(button_list, n_cols=2)
    menu.insert(0, [InlineKeyboardButton('<', callback_data='4'),
                    InlineKeyboardButton('>', callback_data='6')])    
    reply_markup = InlineKeyboardMarkup(menu)
    return reply_markup


def get_button_list_6(update, context):
    button_list = inlinekeyboard_list(6)
    menu = build_menu(button_list, n_cols=2)
    menu.insert(0, [InlineKeyboardButton('<', callback_data='5'),
                    InlineKeyboardButton('>', callback_data='7')])    
    reply_markup = InlineKeyboardMarkup(menu)
    return reply_markup


def get_button_list_7(update, context):
    button_list = inlinekeyboard_list(7)
    menu = build_menu(button_list, n_cols=2)
    menu.insert(0, [InlineKeyboardButton('<', callback_data='6')])
    reply_markup = InlineKeyboardMarkup(menu)
    return reply_markup


"""БЛОК ОБРАБОТЧИКОВ КЛАВИАТУРЫ"""


def lang_menu(update, context):
    query = update.callback_query
    if query.data == '1':        
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=msg_select_lang_of_speech,
            reply_markup=get_button_list_1(update, context)
        )


    if query.data == '2':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=msg_select_lang_of_speech,
            reply_markup=get_button_list_2(update, context)
        )        
        

    if query.data == '3':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=msg_select_lang_of_speech,
            reply_markup=get_button_list_3(update, context)
        )        


    if query.data == '4':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=msg_select_lang_of_speech,
            reply_markup=get_button_list_4(update, context)
        )        


    if query.data == '5':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=msg_select_lang_of_speech,
            reply_markup=get_button_list_5(update, context)
        )        


    if query.data == '6':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=msg_select_lang_of_speech,
            reply_markup=get_button_list_6(update, context)
        )        


    if query.data == '7':
        context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=msg_select_lang_of_speech,
            reply_markup=get_button_list_7(update, context)
        )    
    
    l_list = list(languages.items())
    for lang in l_list:
        if query.data == lang[1]:                        
            # Возможно, добавить все эти данные в context.user_data
            context.user_data['native_lang'] = query.data
            user_id = query.from_user.id
            first_name = query.from_user.first_name
            data = (user_id, first_name, query.data)
            write_data_to_base(data)            


            


# Что надо сделать? что мне надо сделать? Надо слать сообщения юзеру... надо 
# понимать, что у него за родной язык
# Вот чел что-то сказал в чате... его данные записались в базу 
# есть база... есть два человека. У каждого есть свой чат-айди
# Первый человек прислал сообщение. Бот смотрит язык второго, и подставляет его в нужное место.
# 
# Вопрос в том, как посмотреть язык второго                    


            


            # Добавляем в базу id группы
            write_initial_data_to_group_table(
                (query.message.chat_id,)
            )           

            context.bot.send_chat_action(
                chat_id=query.message.chat_id, action=ChatAction.TYPING)        
            query.message.reply_text(
                transl(msg_select_lang_ok, query.data.split('-')[0])                
                )
            return










if __name__ == "__main__":
    pass