import datetime
import sys
from playsound import playsound
from gtts import gTTS
import os
import random
from datetime import datetime
import orest_core
import webbrowser


def o_rest_setup(text):
    language = 'uk'
    recognized_answer = gTTS(text=text, lang=language, slow=False)
    recognized_answer.save("TEMP/temporary_answer.mp3")
    playsound("TEMP/temporary_answer.mp3")
    os.remove("TEMP/temporary_answer.mp3")
    with open('TEMP/log.txt', 'a') as app_log:
        app_log.write(f'{datetime.now().strftime("%H:%M:%S")} - ORESTA: {text}\n')


def acquaintance():
    o_rest_setup('Я згадала, що ми з Вами не знайомі. Як я можу звертатись до Вас?')
    while True:
        # Picture listening set
        orest_core.ui.image_change_on_listening()
        username = orest_core.Orest_Main_Window.voice_getter()

        # Picture speaking set
        orest_core.ui.image_change_on_speaking()

        # Save
        with open('TEMP/config', 'w+') as config:
            config.write(f'Username: {username}')

        # Confirm
        o_rest_setup(f'Рада познайомитись, {username}.')
        o_rest_setup('Я правильно почула ваше ім\'я?')

        # Picture listening set
        orest_core.ui.image_change_on_listening()
        answer = orest_core.Orest_Main_Window.voice_getter()
        if 'так' or 'правильно' or 'вірно' or 'звісно' in answer.lower():
            # Picture speaking set
            orest_core.ui.image_change_on_speaking()
            o_rest_setup('Супер. Я розумна.')
            break
        else:
            # Picture speaking set
            orest_core.ui.image_change_on_speaking()
            o_rest_setup('Сорі, давайте ще раз. Як Ви кажете Вас звуть?')


def hello():
    username = username_getter()
    hello_answers = [f"Привіт, {username}! Рада бачити Вас. Як у Вас справи?",
                     f"Доброго дня, {username}. Чим можу допомогти?",
                     f"Добрий день, {username}. Як Ваш день?"]
    o_rest_setup(random.choice(hello_answers))


def current_time():
    hours = datetime.now().strftime("%H:%M")
    o_rest_setup(f'Зараз {hours}')


def conversation(request):
    if request != 'новини':
        username = username_getter()
        answers = [f'Нічого, потроху. Як у Вас, {username}?',
                   f'Я нормально. А Ви там як, {username}?']
        current_answer = random.choice(answers)
        # Picture speaking set
        orest_core.ui.image_change_on_speaking()
        o_rest_setup(current_answer)

        # Picture listening set
        orest_core.ui.image_change_on_listening()
        username = orest_core.Orest_Main_Window.voice_getter()

        # Picture speaking set
        orest_core.ui.image_change_on_speaking()
        o_rest_setup('Я не дуже крутий співбесідник. Моя Вам порада: знайдіть друзів.')
    else:
        o_rest_setup('Ось головні новини.')
        webbrowser.open('https://news.google.com/')


def app_quit():
    username = username_getter()
    exit_answers = [f"Допобачення, {username}", f"Побачимось, {username}", f"Гарного дня Вам, {username}"]
    o_rest_setup(random.choice(exit_answers))
    with open('TEMP/log.txt', 'a') as app_log:
        app_log.write(f'SESSION IS OVER'.center(50, "-") + "\n")
    sys.exit()


def username_getter():
    try:
        with open('TEMP/config', 'r') as config:
            username = config.read()
            username = username[10:]
    except FileNotFoundError:
        username = ''
    return username


def main(request):
    username = username_getter()
    request_words = []
    word_hello = ["привіт", "вітаю", "доброго дня", "добрий вечір", "салют", "ку", "доброго ранку", "доброго вечора"]
    word_exit = ["бувай", "вихід", "закрити", "вийти", "папа", "допобачення", "щасливо"]
    word_time = ["час", "година", "годин"]
    word_conversation = ["справи", "ти", "нового", "розкажи", "новини"]

    for word in request.split():
        request_words.append(word.lower())

    for word in request_words:
        if word in word_hello:
            hello()
            try:
                with open('TEMP/config', 'r') as config:
                    pass
            except FileNotFoundError:
                acquaintance()
        elif word in word_exit:
            app_quit()
        elif word in word_time:
            current_time()
        elif word in word_conversation:
            conversation(word)
        else:
            continue
