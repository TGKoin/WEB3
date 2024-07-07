import telebot

# Ваш токен бота
TOKEN = '7042638042:AAEUuqWYxiVJ8M5OThIZd3hPQ0g_CuGF3Yk'

# URL на вашу веб-страницу
WEBPAGE_URL = 'https://tgkoin.github.io/'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Переходите по ссылке для получения информации: {WEBPAGE_URL}')

# Запуск бота
if __name__ == '__main__':
    bot.polling()
