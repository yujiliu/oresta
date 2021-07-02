<div align="center"><img src="https://i.ibb.co/0qBh3Ps/logo.png" alt="logo" border="0"></div>

---

```
Alpha 0.0.1a
```

## Що це?

  Ореста - це віртуальний голосовий помічник, що розуміє та відповідає виключно на українській мові.
  
## Що може Ореста?

  - Привітатися з користувачем.
  - Познайомитись з користувачем (за замовчуванням при першому запуску застосунку). Ореста запам’ятає ім’я користувача і в подальшому, буде звертатись з ним до користувача.
  - Можна попросити Оресту змінити ім’я користувача, якщо воно не подобається користувачу, абощо.
  - Ореста може провести діалог з користувачем, але наразі він буде доволі короткий.
  - Відкрити нову вкладку в браузері користувача з новинами.
  - Промовити поточний час (на комп’ютері).
  - Перекласти текст з української на будь-яку іншу мову (функція не доступна у даній версії).
  - Промовити погоду для користувача у будь-якому місті.
  - Знайти потрібну інформацію у Google.
  - Ореста і сама може розказати користувачу, що вона вміє у даній версії. (що ти вмієш)
  - Можна попросити Оресту закрити саму себе.
  
## Локальні файли програми
  
  У папці /TEMP/ за замовчуванням існує один файл /TEMP/null - він пустий і його взагалі можна видалити. Після знайомства з Орестою, з’явиться /TEMP/config і єдиний рядок там - 
  це рядок з ім’ям користувача, яке запамятає Ореста. Також, вже при першому запуску, буде створено /TEMP/log.txt - це простий лог-переписка з Орестою. Використовується виключно
  для дебаггінгу та перевірки запитів. Цей файл нікуди не надсилається у фоновому режимі, інформація про спілкування з Орестою, чи будь-яка інша з комп’ютеру користувача - не
  потрапляє до розробника. Це важливо.
  
## Що планується зробити?

  - Реалізація функції перекладу тексту.
  - Більш складні діалоги, анекдоти та фішки.
  - Додавання задач у власний список задач (TODO List).
  - Нагадування у Windows 10 (зв’язок із попереднім пунктом).
  - Голосовий калькулятор.
  - Рандомайзер числа.
  <br>Ну і найскладніше, на мою думку - режим фонового прослуховування для звернення не через кнопку (аля Привіт, Сірі).
  
## Налаштування погоди

  При запуску функції погоди - виникне помилка, через відсутність API OpenWeatherMap. Необхідно зареєструватись на їхньому сайті, та вставити у app_id у orest_func.py.
  
---

## What it is?

   Oresta is a virtual voice assistant who understands and answers exclusively in Ukrainian.
   
## What can Orestas do?

  - Say hello to the user.
  - Get to know the user (default when you first start the application). Oresta will remember the username and will address the user with it later.
  - You can ask Orestas to change the username if the user doesn't like it or something.
  - Oresta can have a dialogue with the user, but for now it will be quite short.
  - Open a new tab in the user's browser with news.
  - Speak the current time (on the computer).
  - Translate text from Ukrainian into any other language (function is not available in this version).
  - Speak the weather to the user in any city.
  - Find the information you need on Google.
  - Orestas herself can tell the user what she can do in this version. (what can you do)
  - You can ask Orestas to close herself.
  
## Local application files
  
  There is one / TEMP / null file in the / TEMP / folder by default - it is empty and can be deleted altogether. After meeting Orestas, / TEMP / config will appear and the only line there will be -
  this is the string with the username that Orestas remembers. Also, at the first start, /TEMP/log.txt will be created - this is a simple log correspondence with Oresta. Used exclusively
  for debugging and checking queries. This file is not sent anywhere in the background, information about communicating with Orestha, or any other information from the user's computer is not
  gets to the developer. It is important.
  
## What are you planning to do?

  - Implementation of the text translation function.
  - More complex dialogues, anecdotes and chips.
  - Adding tasks to your own to-do list (TODO List).
  - Reminder in Windows 10 (link to the previous item).
  - Voice calculator.
  - Randomizer of numbers.
  <br> Well and the most difficult, in my opinion - a mode of background listening for the address not through the button (ala Hello, Siri).
  
  ## Weather settings

   When starting the weather function - an error will occur due to the lack of the OpenWeatherMap API. You need to register on their site and paste in app_id at orest_func.py.
