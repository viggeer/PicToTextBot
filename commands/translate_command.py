from logger import log_user_action

class TranslateCommand:
    def execute(self, message, bot, state_ref):
        state_ref["state"] = 'translate'
        bot.send_message(message.chat.id, "Отправьте изображение для перевода текста на русский.")
        log_user_action(message.from_user, "Выбор режима", "Перевод текста")
