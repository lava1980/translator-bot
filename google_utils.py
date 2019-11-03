#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext.dispatcher import run_async

# from __future__ import unicode_literals
from telegram import ChatAction
from tinytag import TinyTag 
from google.cloud import speech
# from google.cloud import storage
from google.cloud.speech import enums
from google.cloud import texttospeech
from google.cloud import translate_v2
from google.cloud.speech import types
from google.cloud import texttospeech # pip install google-cloud-texttospeech
from google.cloud import translate_v2

import os
import io
import logging

from config import *
from utils import handle_text


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )




@run_async
def voice_to_text(update, context):
    chat_id = update.message.chat.id
    file_name = str(abs(chat_id)) + '_' + str(update.message.from_user.id) + str(update.message.message_id) + '.ogg'

    update.message.voice.get_file().download(file_name)
    tag = TinyTag.get(file_name)
    
    speech_client = speech.SpeechClient()

    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    native_lang = context.user_data['native_lang']
    logging.info(f'Родной язык из контекста подтянулся такой: {str(native_lang)}')

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=tag.samplerate,
        language_code=native_lang)

    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    response = speech_client.long_running_recognize(config, audio).result(timeout=500) \
        # if to_gs else \
        # speech_client.recognize(config, audio)
    
    message_text = ''
    for result in response.results:
        message_text += result.alternatives[0].transcript + '\n'

    lang = context.user_data['lang']
    message_text = transl(message_text.encode('utf-8'), lang)

    update.message.reply_text(message_text)
    os.remove(os.getcwd() + '/' + file_name)
    

def transl(user_text, target_lang):
    # Instantiates a client
    translate_client = translate_v2.Client()

    # The text to translate
    if isinstance(user_text, str) == False:        
        user_text = user_text.decode('utf-8')
    # The target language   

    # Translates some text into Russian    
    translation = translate_client.translate(
        user_text,
        target_language=target_lang)
    return translation['translatedText']


def text_to_voice(text, lang):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=lang,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.OGG_OPUS)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.ogg', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.ogg"')


def ping_me(update, context, error):
    if not error.message == 'Timed out':
        context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=error.message)


if __name__ == "__main__":
    # transl('Сообщение справки', 'en')
    # text_to_voice('иди в жопу')
    text_to_voice('Катя хорошая девочка', 'ru-RU')