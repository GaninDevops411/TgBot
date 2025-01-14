import telebot
import random

token = '7542323404:AAFmM8-AcwdfBv92ANh-mrmhxVecen92zeU'

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
    games = ['cs2', 'valorant', 'terraria', 'lethal company', 'Phasmaphobia', 'Genshin Impact', 'Dota 2', 'Pubg', 'LoL']
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
    


bot.infinity_polling(none_stop=True)
