"""
Домашнее задание №8

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from datetime import datetime
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
import ephem

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def get_constellation(update, context):
    user_text = update.message.text
    planet = user_text.split()[1]

    dt = datetime.now()
    
    answer = ''
    if planet in (
        "Mercury", "Venus",
        "Mars", "Jupiter", "Saturn", 
        "Uranus", "Neptune", "Pluto"
    ):
        if planet == 'Mercury':
            ephem_planet = ephem.Mercury(dt)
        elif planet == 'Venus':
            ephem_planet = ephem.Venus(dt)
        elif planet == 'Earth':
            ephem_planet = ephem.Earth(dt)
        elif planet == 'Mars':
            ephem_planet = ephem.Mars(dt)
        elif planet == 'Jupiter':
            ephem_planet = ephem.Jupiter(dt)
        elif planet == 'Saturn':
            ephem_planet = ephem.Saturn(dt)
        elif planet == 'Uranus':
            ephem_planet = ephem.Uranus(dt)
        elif planet == 'Neptune':
            ephem_planet = ephem.Neptune(dt)
        elif planet == 'Pluto':
            ephem_planet = ephem.Pluto(dt)
        
        cons = ephem.constellation(ephem_planet)
        constellations = ', '.join(str(con) for con in cons)
        answer = f"Планета {planet} сегодня находится в созвездиях: {constellations}."
    elif planet == "Earth":
        answer = f"Для планеты {planet} нельзя рассчитать созвездие."
    else:
        answer = f"{planet} не является планетой солнечной системы!"
    
    print(f"Вызван {user_text}, ответ - {answer}")
    update.message.reply_text(answer)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
