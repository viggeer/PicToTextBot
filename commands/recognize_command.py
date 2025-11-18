from logger import log_user_action

class RecognizeCommand:
    def execute(self, message, bot, state_ref):
        state_ref["state"] = 'recognize'
        bot.send_message(message.chat.id, "Отправьте изображение для распознавания текста.")
        log_user_action(message.from_user, "Выбор режима", "Распознавание текста")
