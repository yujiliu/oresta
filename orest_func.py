version = '0.0.1a'

import datetime
import sys
from playsound import playsound
from gtts import gTTS
import os
import random
from datetime import datetime
import orest_core
import webbrowser
import requests
from translate import Translator


def o_rest_setup(text):
    language = 'uk'
    recognized_answer = gTTS(text=text, lang=language, slow=False)
    recognized_answer.save("TEMP/temporary_answer.mp3")
    playsound("TEMP/temporary_answer.mp3")
    os.remove("TEMP/temporary_answer.mp3")
    with open('TEMP/log.txt', 'a') as app_log:
        app_log.write(f'{datetime.now().strftime("%H:%M:%S")} - ORESTA: {text}\n')


def re_fucking_check(user_request):
    username = username_getter()
    if user_request.lower() == 'слава україні':
        o_rest_setup('Героям слава!')
    elif 'змінити' or 'імя' in user_request:
        acquaintance()
    else:
        o_rest_setup(f'Щось пішло не так, {username}, Ваш запит я не зрозуміла.')


def acquaintance():
    o_rest_setup('Як я можу звертатись до Вас?')
    while True:
        # Picture listening set
        orest_core.ui.image_change_on_listening()
        username = orest_core.Orest_Main_Window.voice_getter()

        # Picture speaking set
        orest_core.ui.image_change_on_speaking()

        # Save
        with open('TEMP/config', 'w') as config:
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
    hello_answers = [f"Привіт, {username}!",
                     f"Доброго дня, {username}.",
                     f"Вітаю, {username}."]
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

        # Translate username from Russian to Ukrainian (dont ask)
        username = translate_to_ukrainian(username)

        # Picture speaking set
        orest_core.ui.image_change_on_speaking()
        o_rest_setup('Я не дуже крутий співрозмовник. Моя Вам порада: знайдіть друзів.')
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


def translate_to_english(text):
    translator = Translator(from_lang="ukrainian", to_lang="english")
    translation = translator.translate(text)
    return translation


def translate_to_ukrainian(text):
    translator = Translator(from_lang="russian", to_lang="ukrainian")
    translation = translator.translate(text)
    return translation


def weather_check(city_ukrainian=None):
    username = username_getter()
    # Listening of city name
    if city_ukrainian is None:
        o_rest_setup(f'{username}У якому місті Вас цікавить прогноз погоди?')
        orest_core.ui.image_change_on_listening()
        city_ukrainian = orest_core.Orest_Main_Window.voice_getter()
        city = translate_to_english(city_ukrainian)
    else:
        city = translate_to_english(city_ukrainian)

    app_id = "7b60931fa6f6a616614a962761a07cfb"
    city_id = 0

    try:
        # Checking city in OWM list
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': app_id})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        city_id = data['list'][0]['id']
        print(cities)
    except Exception as e:
        orest_core.ui.image_change_on_speaking()
        o_rest_setup(f'Вибачте, але таке місто я не знаю.')
    else:
        # If city in OWM list - here's weather
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()
        weather_status = data['weather'][0]['description']
        weather_temperature = data['main']['temp']
        weather_temperature_min = data['main']['temp_min']
        weather_temperature_max = data['main']['temp_max']

        # Speaking set
        orest_core.ui.image_change_on_speaking()
        weather_status = translate_to_ukrainian(weather_status)
        o_rest_setup(f'Погода у місті {city_ukrainian}, '
                     f'зараз {weather_status}, '
                     f'температура за вікном сягає до {int(weather_temperature)}'
                     f'градусів Цельсія. Максимальна температура вдень {int(weather_temperature_max)}, мінімальна'
                     f'температура впаде до {int(weather_temperature_min)} градусів Цельсія.')


def google_search(user_request):
    print('check 0')
    search_request = ''
    do_not_append = ["знайди", "пошукай", "пошук", "у", "в", "гуглі", "інформація",
                     "гугл", "інформацію", "про", "знайти", "угол", "google", "будь", "ласка"]
    print('check 1')
    for word in user_request:
        if word in do_not_append:
            pass
        else:
            search_request += word + ' '
    final_request = 'https://www.google.com/search?q='
    print('check 2')
    for search_request_word in search_request.split(' '):
        final_request += search_request_word + '+'
    print('check 3')
    webbrowser.open(final_request)
    o_rest_setup('Ось, що я змогла знайти.')


def what_can_i_do():
    o_rest_setup(f'У версії {version} я можу наступне.'
                 f' привітатися та познайомитись з Вами,'
                 f' самостійно закрити себе,'
                 f' озвучити поточний час,'
                 f' озвучити погоду в будь-якому місті,'
                 f' знайти необхідну інформацію у Google,'
                 f' відкрити Google Новини,')


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
    word_conversation = ["справи", "нового", "розкажи", "новини"]
    word_weather = ["погода"]
    word_search = ["пошукай", "знайди", "пошук", "знайти", "інформація", "інформацію", "google"]
    word_what_can_i_do = ["вмієш", "функції"]
    other_word = 0

    for word in request.split():
        request_words.append(word.lower())

    try:
        with open('TEMP/config', 'r') as config:
            pass
    except FileNotFoundError:
        o_rest_setup('Привіт!')
        acquaintance()

    for word in request_words:
        if word in word_hello:
            hello()
            break
        elif word in word_exit:
            app_quit()
            break
        elif word in word_time:
            current_time()
            break
        elif word in word_conversation:
            conversation(word)
            break
        elif word in word_search:
            google_search(request_words)
            break
        elif word in word_what_can_i_do:
            what_can_i_do()
            break
        elif word in word_weather:
            if 'у' in request_words:
                if 'місті' in request_words:
                    city = request_words[request_words.index('у') + 2]
                else:
                    city = request_words[request_words.index('у') + 1]
                weather_check(city)
                break
            elif 'в' in request_words:
                if 'місті' in request_words:
                    city = request_words[request_words.index('в') + 2]
                else:
                    city = request_words[request_words.index('в') + 1]
                weather_check(city)
                break
            else:
                weather_check()
                break
        else:
            other_word += 1
    if other_word == len(request_words):
        re_fucking_check(request)
    else:
        pass
