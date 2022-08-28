import telebot
from telebot import types

bot = telebot.TeleBot('5662440604:AAGqVqqNRTT6cY_0OhgwtogElp8K7jvcibc')


@bot.message_handler(commands=['go', 'start'])  # Обработка команды для старта
def welcome(message):
    #sti = open('stiker.tgs', 'rb')
    #bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item3 = types.KeyboardButton("Игры")
    item2 = types.KeyboardButton("Кодинг")
    item1 = types.KeyboardButton('О нас')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n\nЯ - <b>{1.first_name}</b>, бот команды Арена геим плей, "
                     "создан для того, "
                     "чтобы помочь Вам влиться в нашу команду,"
                     "просто узнать что-то о нас или же просто пообщаться и весело провести время.\n\n"
                     "<i>Have a nice time</i>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")



def get_name(message):  # получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        pass  # .... #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        pass  # ... #переспрашиваем


@bot.message_handler(commands=['stop'])  # Обработка команды для выхода
def bye(message):
    #bye_Sti = open('byeMorty.tgs', 'rb')

    hideBoard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "Досвидания, {0.first_name}!\nМы, команда <b>{1.first_name}</b>, надеемся, что ты хорошо провел(а) время \n\n"
                     "Присоединяйся к нашей команде в <a href='<https://office_compressor.ru'>web</a>\n"
                     "Наш <a href='<https://instagram.com/office_compressor>'>inst</a>\n\n"
                     "Напиши Координатору проектов (<a href='<https://office_compressor.ru/admin>'>Админ</a>) и задай интересующие тебя вопросы по <i>проектной деятельности</i>\n\n"
                     "Надеемся, что тебе ответят очень скоро \n\n"
                     "<u>Don't be ill and have a nice day</u> \n\n\n"
                     "P.S.: Если есть какие-то пожелания или вопросы по боту, то напиши <a href='<https://office_compressor.ru/setmyaddresspls>'>мне</a>".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=hideBoard)
    #exit()


name = ''
surname = ''
age = 0
bot.polling(none_stop=True, interval=0)
