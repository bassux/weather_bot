import telebot

from API_KEYS.get_key import get_key
from weather.weather import Weather
from thrds.threads import new_thread
from users.users_log import add_users_to_log


bot = telebot.TeleBot(get_key('test_bot_key.txt'))
weather = Weather()


@bot.message_handler(commands=['start', 'st', 'help', 'h', 'hlp'])
@new_thread
def start(message: telebot.types.Message) -> None:
    """
    Greetings
    :param message: telebot.types.Message
    :return: None
    """
    bot.send_message(message.from_user.id,
                     f'Привет, {message.from_user.first_name}! Просто отправь мне город и увидишь погоду.')

    add_users_to_log(message.from_user.username, 'start/help')



@bot.message_handler()
@new_thread
def weather_message(message: telebot.types.Message) -> None:
    """
    Send weather by city name.
    :param message: telebot.types.Message
    :return: None
    """
    weather.get_weather(message.text)
    bot.send_message(message.from_user.id, weather.last_weather)

    add_users_to_log(message.from_user.username, message.text)

