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
    bot.send_message(message.chat.id, "/random - отправляет в список, где вам нужно выбрать команды для рандома игр и рандома чисел \n\n/disfix - отправляет файл для разблокировки ютуба и дискорда")


@bot.message_handler(commands=['random'])
def randomcomand(message):
    text = 'Что ты хочешь зарандомить?\n/randomgames\n/randomnumbers'
    #\n - перенос строки
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['randomgames'])
def randomgame(message):
    games = ['cs2\nhttps://store.steampowered.com/app/730/CounterStrike_2/','valorant\nhttps://playvalorant.com/ru-ru/','terraria\nhttps://store.steampowered.com/app/105600/Terraria/','lethal company\nhttps://store.steampowered.com/app/1966720/Lethal_Company/','Phasmaphobia\nhttps://store.steampowered.com/app/739630/Phasmophobia/','Genshin Impact\nhttps://genshin.hoyoverse.com/ru/','Dota 2\nhttps://store.steampowered.com/app/570/Dota_2/','Pubg\nhttps://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/','LoL\nhttps://www.leagueoflegends.com/ru-ru/download/']
    game = games[random.randint(0, len(games) - 1)]
    bot.send_message(message.chat.id, game)


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


@bot.message_handler(commands=['disfix'])
def disfix(message):
    # Путь к файлу
    file_path = r"C:\Users\artem\Downloads\YouTubeFix.rar"

    try:
        with open(file_path, "rb") as file:
            bot.send_document(message.chat.id, file)  # Отправляем только файл
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Файл не найден. Проверьте путь.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")


# Запускаем бота
print("Бот запущен и ожидает сообщений...")
bot.polling()



