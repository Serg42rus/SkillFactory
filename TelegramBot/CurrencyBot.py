import telebot
from config import keys, TOKEN
from extensions import ApiException,CurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text='чтобы заработало введит команду в формате: \n<в какую валюту ты хочешь перевести> \
<что ты хочешь перевести> <количество> \n\
по команде /values вывод доступных для конвертации валют'
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='вывод доступных для конвертации валют'
    for key in keys.keys():
        text ='\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ApiException('неправильное количество параметров')

        quote, base, amount = values
        total_base = CurrencyConverter.convert(quote, base, amount)
    except ApiException as e:
        bot.reply_to(message, f',ошибка ввода пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f',не удалось обработать команду \n{e}')
    else:
        text = f'сколько стоит {amount} {base} в {quote} - {total_base}'
        bot.send_message(message.chat.id,text)

bot.polling()