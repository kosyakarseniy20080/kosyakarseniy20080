import telebot

API_TOKEN = "7032435790:AAEsoRckUzP0yy310ovJUcUNMJ3S6cjQH_U"


bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['text'])
def get_tex_message(message):
    if message.text == "Привет":
       bot.send_message(message.from_user.id, 'Привет, друг')
    elif message.text == "/start":
        bot.send_message(message.from_user.id, 'Друг ты же любишь смотреть хоккей?')
    elif message.text == "сегодня":
        bot.send_message(message.from_user.id, message.date)


bot.polling(none_stop=True, interval=0)