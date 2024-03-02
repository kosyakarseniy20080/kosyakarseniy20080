import telebot

API_TOKEN = "7032435790:AAEsoRckUzP0yy310ovJUcUNMJ3S6cjQH_U"


bot = telebot.TeleBot(API_TOKEN)

photo = open('./images/khl.jpg', 'rb')

rulesRemovalhockey= "1.Малый штраф — это обычное двухминутное удаление, Подножка, удар клюшкой и т.д",
"2.Двойной малый штраф присуждается игрокам, совершившим более серьёзное нарушение правил, чем вышеупомянутые подножки и т.п. Самым популярным способом получить сразу четыре минуты является игра высокоподнятой клюшкой, особенно, если был задет соперник",
"3.Большим штрафом наказывается игрок, совершивший умышленное нарушение правил, принесшее повреждение представителю команды соперника. Среди наиболее часто встречающихся проступков, за которые присуждают 5 минут штрафа, обычно выделяют удар в голову, удар коленом в колено, атака сзади, подсечка, колющий удар.",
"4.Дисциплинарный штраф в хоккее — это удаление хоккеиста на 10 минут, которое в большинстве случаев идёт дополнением к другому нарушению правил."

@bot.message_handler(commands=["start"])

def buttons(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton(text="play-off")
    button2 = telebot.types.KeyboardButton(text="rules")
    markup.add(button1,button2)
    bot.send_message(message.from_user.id, "Привет, выбирай команду", reply_markup=markup)
    
playoff_photo = open('./images/khl play-off.jpg', 'rb')

@bot.message_handler(content_types=['text'])

def get_tex_message(message):
    chat_id = message.from_user.id
    if message.text == "Привет":
       bot.send_message(chat_id, f'Привет, {message.from_user.username}')
    elif message.text == "/start":
        bot.send_message(message.from_user.id, 'Друг ты же любишь смотреть хоккей?')
    elif message.text == "photo":
        bot.send_photo(chat_id, photo)
    elif message.text == "rules":
        bot.send_message(chat_id, rulesRemovalhockey)

bot.polling(none_stop=True, interval=0)