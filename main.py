import telebot
import datetime
bot = telebot.TeleBot('5749113407:AAHk1zKxOg8kIroi85lL4PU6bP5a1-DPmmY')
keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('Привет=)', 'Пока=(', 'я лавринович')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Уважаемые тимлидеры, Джуниоры и все, кто был причастен к мероприятию!😚\n Это было мое самое лучшее 1 сентября в жизни. Песня про Беларусь тронула мое сердце до глубины души.😖\nБольшое вам спасибо за организованный праздник!!!😆', reply_markup = keybord1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if 'привет' in message.text.lower():
        bot.send_message(message.chat.id, 'И тебе привет!=)')
    elif 'пока' in message.text.lower():
        bot.send_message(message.chat.id, 'Пока, заходи ещё!)')
    elif message.text.lower() == 'я лавринович':
        bot.send_message(message.chat.id, 'понимаю')
    elif 'дата' or 'день недели' in message.text.lower():
        bot.send_message(message.chat.id, datetime.datetime.now)
bot.polling()