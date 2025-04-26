import telebot
import requests
import random
from telebot import types

# Замените "YOUR_BOT_TOKEN" на токен вашего бота
BOT_TOKEN = "7694377233:AAH0No73vLWoNQEknCSLkS1c0IV2HhR8bfQ"
bot = telebot.TeleBot(BOT_TOKEN)

# Замените "YOUR_OPENWEATHERMAP_API_KEY" на ваш API ключ от OpenWeatherMap
WEATHER_API_KEY = "f334359f9286535a9db485e5cf8a9e0e"
CITY = "Vladimir"  # Город по умолчанию

# Ваши любимые стикеры (замените на свои sticker_id)
sticker_ids = [
    "CAACAgIAAxkBAAEOSXBn-iCB6VRCVn_xaoRHDFfLgPFx3AACVQEAAhZCawqIth7z4PmTbDYE",
    "CAACAgIAAxkBAAEOSXJn-iC4EdGKeZIdrFiZVYMhUpKYowACCxMAAr0MQEt7NM6GTNplzTYE",
    "CAACAgIAAxkBAAEOSXRn-iDP-TKKToFIn3xcTo4noxtXJAACiAsAAi8P8AZbWs6pV7klEzYE",
]

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return temperature, description
    except requests.exceptions.RequestException as e:
        return None, str(e)
    except (KeyError, TypeError):
        return None, "Ошибка получения данных о погоде"

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weather_button = types.KeyboardButton("Текущая погода")
    sticker_button = types.KeyboardButton("Стикер")
    markup.add(weather_button, sticker_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы узнать погоду или получить стикер.", reply_markup=markup)

# Обработчик текстовых сообщений (для "Привет")
@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def hello(message):
    bot.reply_to(message, "Привет, человек")

# Обработчик нажатия на кнопку "Текущая погода"
@bot.message_handler(func=lambda message: message.text == "Текущая погода")
def weather(message):
    temperature, description = get_weather(CITY)
    if temperature is not None:
        bot.send_message(message.chat.id, f"Погода в городе {CITY}: {temperature:.1f}°C, {description}")
    else:
        bot.send_message(message.chat.id, description) # Отправляем сообщение об ошибке

# Обработчик нажатия на кнопку "Стикер"
@bot.message_handler(func=lambda message: message.text == "Стикер")
def sticker(message):
    random_sticker = random.choice(sticker_ids)
    bot.send_sticker(message.chat.id, random_sticker)

if __name__ == '__main__':
    bot.infinity_polling()