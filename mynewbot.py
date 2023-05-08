 # Мой первый чат-бот, создан в 4 мая 2023 года

import telebot

bot = telebot.TeleBot("6040735150:AAGfNaYLuCznUNoxsa7sGLoH8kSmNjV6Jlw", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f"Привет, {message.from_user.first_name} {message.from_user.last_name} !😀"
						  f"\n устал листать каталоги 😃 \n"
						  f"Design-Bot подберет Вам за пару кликов классную итальянскую мебель для твоей квартиры 😉 \n"
						  f" Тогда напиши быстрей, хочу ")

# 1 дополение
# там где if message.text - это вводит пользователь
# bot.send_message - бот отвечает

@bot.message_handler()
def get_user_text(message):
	if message.text == ("хочу"):
		bot.send_message(message.chat.id, "Если нужны комфортные диваны - нажмите 1,\n "
										  "если мягкие кровати - нажмите 2 \n "
										  "дизайнерский столы - нажмите 3 \n"
										  "Дизайнерский свет - 4 \n"
										  "Хорошая музыка - 5 \n"
										  "VIDEO новинки с ISaloni Milan-6 ", parse_mode="html")


	elif message.text == ("1"):
		bot.send_message(message.chat.id, "Прекрасно! \n "
										  "Могу предложить замечательную фабрику Frigerio \n"
										  "средняя стоимость диванов как на фото: от 13 до 16.000 евро", parse_mode="html")
		photo = open("fri_divan_01.png", 'rb')
		bot.send_photo(message.chat.id, photo,'13 000 евро')
		photo = open("fri_divan_02.png", 'rb')
		bot.send_photo(message.chat.id, photo,'14 000 евро')
		photo = open("fri_divan_03.png", 'rb')
		bot.send_photo(message.chat.id, photo,'15 000 евро')
		photo = open("fri_divan_04.png", 'rb')
		bot.send_photo(message.chat.id, photo,'16 000 евро')

	elif message.text == ("2"):
		bot.send_message(message.chat.id, "Замечательно! могу предложить Bonaldo", parse_mode="html")
		photo = open("bon_letti_01.png", 'rb')
		bot.send_photo(message.chat.id, photo, '5 000 евро')
		photo = open("bon_letti_02.png", 'rb')
		bot.send_photo(message.chat.id, photo, '6 000 евро')
		photo = open("bon_letti_03.png", 'rb')
		bot.send_photo(message.chat.id, photo, '5 000 евро')
		photo = open("bon_letti_04.png", 'rb')
		bot.send_photo(message.chat.id, photo, '5 000 евро')

	elif message.text == ("3"):
		bot.send_message(message.chat.id, "Центром внимания вашей гостиной могут стать \n"
										  "дизайнерские столы ручной работы Ceccotti", parse_mode="html")
		photo = open("cec_tav_01.png", 'rb')
		bot.send_photo(message.chat.id, photo, '13 000 евро')
		photo = open("cec_tav_02.png", 'rb')
		bot.send_photo(message.chat.id, photo, '14 000 евро')
		photo = open("cec_tav_03.png", 'rb')
		bot.send_photo(message.chat.id, photo, '15 000 евро')
		photo = open("cec_tav_04.png", 'rb')
		bot.send_photo(message.chat.id, photo, '16 000 евро')

	elif message.text == ("4"):
		bot.send_message(message.chat.id, "Дизайнерские светильники Stilnovo \n"
										  "придадут интерьеру особеный цвет", parse_mode="html")
		photo = open("stil_svet_01.png", 'rb')
		bot.send_photo(message.chat.id, photo, '800 евро')
		photo = open("stil_svet_02.png", 'rb')
		bot.send_photo(message.chat.id, photo, '900 евро')
		photo = open("stil_svet_03.png", 'rb')
		bot.send_photo(message.chat.id, photo, '100 евро')
		photo = open("stil_svet_04.png", 'rb')
		bot.send_photo(message.chat.id, photo, '1100 евро')
		photo = open("stil_svet_05.png", 'rb')
		bot.send_photo(message.chat.id, photo, '1200 евро')
		photo = open("stil_svet_06.png", 'rb')
		bot.send_photo(message.chat.id, photo, '900 евро')
		photo = open("stil_svet_07.png", 'rb')
		bot.send_photo(message.chat.id, photo, '1100 евро')
		photo = open("stil_svet_08.png", 'rb')
		bot.send_photo(message.chat.id, photo, '9000 евро')

	elif message.text == ("5"):
		bot.send_message(message.chat.id, "Песенка для хорошего настроения)", parse_mode="html")
		audio = open('Nina_Brodskaya_-_Pesenka_Buratino_56992022.mp3', 'rb')
		tb.send_audio(audio.chat.id, audio)
		tb.send_audio(audio.chat.id, "Буратино")

	elif message.text == ("6"):
		bot.send_message(message.chat.id, "Новинки с Миланской выставки 2023", parse_mode="html")
		video = open('bon_video.mp4', 'rb')
		tb.send_video(audio.chat.id, video)
		tb.send_video(audio.chat.id, "Новинки с ISaloni Milan 2023")


	else:
		bot.send_message(message.chat.id, "Вы наверное опечатались, \n "
										  "давайте попробуем снова, думаю у Вас получится 😃",parse_mode="html")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

# Commit - до этого места все работает












