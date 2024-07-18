import telebot

# Замените 'YOUR_BOT_API_TOKEN' на ваш реальный токен API бота
API_TOKEN = 'Your_bot_token'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши мне что-нибудь, и я покажу твой chat_id.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Ваш chat_id: {chat_id}")

bot.infinity_polling()
