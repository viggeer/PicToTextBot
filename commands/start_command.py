from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from logger import log_user_action

class StartCommand:
    def execute(self, message, bot, state_ref):
        state_ref["state"] = None
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            KeyboardButton("🔍 Распознать текст"),
            KeyboardButton("🌍 Перевести текст"),
        )
        bot.send_message(message.chat.id, "<b>Выберите действие:</b>", reply_markup=markup, parse_mode="HTML")
        log_user_action(message.from_user, "Старт бота")
