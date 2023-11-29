import telebot 
bot = telebot.TeleBot('6764205051:AAEIpx4bW6jLNYe_Ylbi4gSrtmHOflgJOJo')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'хочешь заказать модные кроссовки? жми на price')

@bot.message_handler(commands=['price'])
def main(message):
    bot.send_message(message.chat.id, 'Заказывай у нас \nУ нас выгодно)')

@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'сайт [для заказа](https://poizonbox.ru)', parse_mode='Markdown')

@bot.message_handler(commands=['contacts'])
def main(message):
    bot.send_message(message.chat.id, '+79243961303 \nprokigor456@mail.ru')


bot.infinity_polling()