import telebot

bot = telebot.TeleBot("6402367062:AAFe5EbS48Tf6uK-K_1uHL06D34hyWVkH50")


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Glad to see you Mr or Mrs")


@bot.message_handler(commands=["new"])
def start_handler(message):
    bot.send_message(message.chat.id,
                     "_Compassion is the most important and perhaps the only law of existence for all mankind_",
                     parse_mode="Markdown")


bot.infinity_polling()