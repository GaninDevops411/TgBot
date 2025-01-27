import telebot
import random
import os
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, BotCommand

load_dotenv()

token = os.getenv("TOKEN")

if not token:
    raise ValueError("Токен не найден. Проверьте файл .env и переменную TOKEN.")

bot = telebot.TeleBot(token, parse_mode='HTML')  # Установлен режим HTML для удобства


# Хранилище состояний для обработки ввода (глобальный словарь)
user_states = {}

# --- Главное меню ---
def main_menu(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("🎲 Рандом"),
        KeyboardButton("📂 Файл Fix"),
        KeyboardButton("ℹ️ Помощь")
    )
    bot.send_message(chat_id, "Выберите действие:", reply_markup=markup)


# --- Команда /start ---
@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message.chat.id)


# --- Обработчик кнопки 🎲 Рандом ---
@bot.message_handler(func=lambda message: message.text == "🎲 Рандом")
def handle_random(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("🕹️ Случайная игра"),
        KeyboardButton("🔢 Случайное число"),
        KeyboardButton("🔙 Назад")
    )
    bot.send_message(message.chat.id, "Что вы хотите зарандомить?", reply_markup=markup)


# --- Обработчик кнопки 🔢 Случайное число ---
@bot.message_handler(func=lambda message: message.text == "🔢 Случайное число")
def random_number_request(message):
    user_states[message.chat.id] = "waiting_for_range"
    bot.send_message(
        message.chat.id,
        "Введите диапазон чисел в формате 'min max' (например, '1 10')."
    )


@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "waiting_for_range")
def random_number_response(message):
    try:
        # Разбираем диапазон
        min_num, max_num = map(int, message.text.split())
        random_num = random.randint(min_num, max_num)
        bot.send_message(message.chat.id, f"Случайное число: {random_num}")
        user_states[message.chat.id] = None  # Сбрасываем состояние
    except (ValueError, IndexError):
        bot.send_message(
            message.chat.id,
            "Некорректный ввод. Убедитесь, что вы отправили два числа через пробел, например, '1 10'."
        )


# --- Обработчик кнопки 🕹️ Случайная игра ---
@bot.message_handler(func=lambda message: message.text == "🕹️ Случайная игра")
def random_game(message):
    games = [
        'CS2\nhttps://store.steampowered.com/app/730/CounterStrike_2/',
        'Valorant\nhttps://playvalorant.com/ru-ru/',
        'Terraria\nhttps://store.steampowered.com/app/105600/Terraria/',
        'Lethal Company\nhttps://store.steampowered.com/app/1966720/Lethal_Company/',
        'Phasmophobia\nhttps://store.steampowered.com/app/739630/Phasmophobia/',
        'Genshin Impact\nhttps://genshin.hoyoverse.com/ru/',
        'Dota 2\nhttps://store.steampowered.com/app/570/Dota_2/',
        'PUBG\nhttps://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/',
        'LoL\nhttps://www.leagueoflegends.com/ru-ru/download/',
        'DeadLock\nhttps://store.steampowered.com/app/1422450/Deadlock/',
        'Minecraft\nhttps://www.minecraft.net/ru-ru'
    ]
    game = random.choice(games)
    bot.send_message(message.chat.id, f"Попробуйте эту игру: {game}")


# --- Обработчик кнопки 📂 Файл Fix ---
@bot.message_handler(func=lambda message: message.text == "📂 Файл Fix")
def send_fix_file(message):
    file_path = r"C:\Users\artem\Downloads\YouTubeFix.rar"
    try:
        with open(file_path, "rb") as file:
            bot.send_document(message.chat.id, file)
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Файл не найден. Проверьте путь.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")


# --- Обработчик кнопки ℹ️ Помощь ---
@bot.message_handler(func=lambda message: message.text == "ℹ️ Помощь")
def help(message):
    bot.send_message(
        message.chat.id,
        "/random - открыть меню рандома\n"
        "/randomgames - случайная игра\n"
        "/randomnumbers - случайное число\n"
        "/disfix - получить файл Fix"
    )


# --- Обработчик кнопки 🔙 Назад ---
@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def go_back(message):
    user_states[message.chat.id] = None  # Сбрасываем состояние
    main_menu(message.chat.id)


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
    games = ['cs2\nhttps://store.steampowered.com/app/730/CounterStrike_2/',
             'valorant\nhttps://playvalorant.com/ru-ru/',
             'terraria\nhttps://store.steampowered.com/app/105600/Terraria/',
             'lethal company\nhttps://store.steampowered.com/app/1966720/Lethal_Company/',
             'Phasmaphobia\nhttps://store.steampowered.com/app/739630/Phasmophobia/',
             'Genshin Impact\nhttps://genshin.hoyoverse.com/ru/',
             'Dota 2\nhttps://store.steampowered.com/app/570/Dota_2/',
             'Pubg\nhttps://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/',
             'LoL\nhttps://www.leagueoflegends.com/ru-ru/download/',
             'DeadLock\nhttps://store.steampowered.com/app/1422450/Deadlock/'
             'Minecraft\nhttps://www.minecraft.net/ru-ru'
             ]
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


