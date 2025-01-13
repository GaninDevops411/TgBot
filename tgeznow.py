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
    lst = ['cs2','valorant','terraria','lethal company','Phasmaphobia','Genshin Impact','Dota 2','Pubg','LoL']
    game = random.choice(lst)
    bot.send_message(message.chat.id, game)

@bot.message_handler(commands=['randomnumber'])
def randomnuber(message):

    number = random.randint(1, 10 )
    bot.send_message(message.chat.id, message.text)
    message.text


bot.infinity_polling(none_stop=True)
