import telebot
import os
import requests

TOKEN = os.environ["CATBOT_TOKEN"]
CATAPI_TOKEN = os.environ["CATAPI"]
CATSURL = "https://api.thecatapi.com/v1/images/search"
bot = telebot.TeleBot(TOKEN)

headers = {"x-api-key": CATAPI_TOKEN}

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(chat_id=message.chat.id, text="I can send cute images of cats= ) Try it! Type /cat")

@bot.message_handler(commands=['cat'])
def send_cat(message):
    r = requests.get(CATSURL, headers=headers)
    image_path = r.json()[0]["url"]
    bot.send_photo(chat_id=message.chat.id, photo=image_path)

bot.polling()