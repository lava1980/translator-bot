#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext.dispatcher import run_async

# from __future__ import unicode_literals
from telegram import ChatAction
from tinytag import TinyTag 
from google.cloud import speech
# from google.cloud import storage
from google.cloud.speech import enums
from google.cloud import translate
from google.cloud.speech import types
import os
import io
import logging

from config import *


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'tgbot.log'
                    )




@run_async
def voice_to_text(update, context):
    chat_id = update.message.chat.id
    file_name = str(chat_id) + '_' + str(update.message.from_user.id) + str(update.message.message_id) + '.ogg'

    update.message.voice.get_file().download(file_name)
    tag = TinyTag.get(file_name)
    
    speech_client = speech.SpeechClient()

    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=tag.samplerate,
        language_code='ru-RU')

    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    response = speech_client.long_running_recognize(config, audio).result(timeout=500) \
        # if to_gs else \
        # speech_client.recognize(config, audio)
    
    message_text = ''
    for result in response.results:
        message_text += result.alternatives[0].transcript + '\n'

    
    message_text = transl(message_text.encode('utf-8'), 'en')

    update.message.reply_text(message_text)
    os.remove(os.getcwd() + '/' + file_name)
    




def transl(user_text, target_lang):
    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    
    text = user_text.decode('utf-8')
    # The target language
    target = target_lang

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    # print(u'Text: {}'.format(text))
    # print(u'Translation: {}'.format(translation['translatedText']))
    return translation['translatedText']











def ping_me(update, context, error):
    if not error.message == 'Timed out':
        context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=error.message)


if __name__ == "__main__":
    transl('ru')