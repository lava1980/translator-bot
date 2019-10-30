from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from config import buttons_pages, languages




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

