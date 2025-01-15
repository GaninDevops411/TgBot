import telebot
import random
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

if not token:
    raise ValueError("Токен не найден. Проверьте файл .env и переменную TOKEN.")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    text = 'Привет! Это Рандомезноу. Напиши /help чтобы увидеть больше команд'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/random")


@bot.message_handler(commands=['random'])
def randomcomand(message):
    text = 'Что ты хочешь зарандомить?\n/randomgame\n/randomnumbers'
    #\n - перенос строки
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['randomgame'])
def randomgame(message):
    games = ['cs2\nhttps://store.steampowered.com/app/730/CounterStrike_2/','valorant\nhttps://playvalorant.com/ru-ru/','terraria\nhttps://store.steampowered.com/app/105600/Terraria/','lethal company\nhttps://store.steampowered.com/app/1966720/Lethal_Company/','Phasmaphobia\nhttps://store.steampowered.com/app/739630/Phasmophobia/','Genshin Impact\nhttps://genshin.hoyoverse.com/ru/','Dota 2\nhttps://store.steampowered.com/app/570/Dota_2/','Pubg\nhttps://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/','LoL\nhttps://www.leagueoflegends.com/ru-ru/download/']
    game = games[random.randint(0, len(games) - 1)]
    bot.send_message(message.chat.id, game)

@bot.message_handler(commands=['!Бот_еблан'])
def randomcomand(message):
        text = 'Сам еблан!'
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['randomnumber'])
def randomnuber(message):
    numbers_list = message.text.split()[1:]

    if len(numbers_list) == 2:
        a, b = numbers_list

        if a.isdigit() & b.isdigit():
            number = random.randint(int(a), int(b))
            bot.send_message(message.chat.id, number)
            return

    bot.send_message(message.chat.id, 'Неправильная команда')

bot.infinity_polling(none_stop=True)
