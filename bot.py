import os
import re
import telebot
from PIL import Image
import pytesseract
from deep_translator import GoogleTranslator
from commands.start_command import StartCommand
from commands.recognize_command import RecognizeCommand
from commands.translate_command import TranslateCommand
from logger import log_user_action

# Токен тг бота
bot = telebot.TeleBot("")
# Путь к тессеракту
pytesseract.pytesseract.tesseract_cmd = r''

state_ref = {"state": None}

commands = {
    "/start": StartCommand(),
    "/recognize": RecognizeCommand(),
    "/translate": TranslateCommand(),
    "🔍 Распознать текст": RecognizeCommand(),
    "🌍 Перевести текст": TranslateCommand()
}

def escape_html(text):
    text = re.sub(r'&', '&amp;', text)
    text = re.sub(r'<', '&lt;', text)
    text = re.sub(r'>', '&gt;', text)
    return text

def translate_text_to_russian(text):
    try:
        return GoogleTranslator(source="auto", target="ru").translate(text)
    except Exception as e:
        return f"Ошибка перевода: {str(e)}"

@bot.message_handler(commands=['start'])
def handle_start(message):
    commands["/start"].execute(message, bot, state_ref)

@bot.message_handler(commands=['recognize'])
def handle_recognize_cmd(message):
    commands["/recognize"].execute(message, bot, state_ref)

@bot.message_handler(commands=['translate'])
def handle_translate_cmd(message):
    commands["/translate"].execute(message, bot, state_ref)

@bot.message_handler(func=lambda m: m.text in commands)
def handle_command(message):
    commands[message.text].execute(message, bot, state_ref)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    state = state_ref["state"]
    if state not in ['recognize', 'translate']:
        bot.send_message(message.chat.id, "Сначала выберите действие с помощью кнопок.")
        return

    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", "wb") as f:
        f.write(downloaded_file)

    try:
        image = Image.open("image.jpg").convert("L")
        text = pytesseract.image_to_string(image, lang="rus+eng")

        if text.strip():
            user = message.from_user
            log_user_action(user, "Отправил фото", f"Режим: {state}, Текст: {text[:50]}...")

            if state == 'recognize':
                bot.reply_to(message, f"<b>Распознанный текст:</b>\n{escape_html(text)}", parse_mode="HTML")
            elif state == 'translate':
                translated = translate_text_to_russian(text)
                bot.reply_to(message, f"<b>Перевод:</b>\n{escape_html(translated)}", parse_mode="HTML")
        else:
            bot.reply_to(message, "Текст не распознан.")
    finally:
        if os.path.exists("image.jpg"):
            os.remove("image.jpg")
        state_ref["state"] = None

bot.polling()
