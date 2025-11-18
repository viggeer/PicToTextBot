# PicToTextBot

Telegram-бот для распознавания текста с изображений и последующего перевода.  
Написан на Python с использованием библиотеки **telebot**.

Проект реализован с разделением логики на команды, модульный код и системой логирования действий пользователей.

---

## Возможности

### Команды
| Команда | Описание |
|--------|----------|
| `/start` | Запускает бота и показывает меню |
| `/recognize` | Переходит в режим распознавания текста |
| `/translate` | Переходит в режим перевода текста |

### Кнопки
- Распознать текст  
- Перевести текст  

Обе кнопки работают аналогично командам.

---

## Используемые технологии

- **Python 3.10+**
- `telebot` — работа с Telegram Bot API
- `Pillow (PIL)` — обработка изображений
- `pytesseract` — OCR (распознавание текста)
- `deep_translator` — перевод текста
- **Tesseract OCR** — движок распознавания текста
- Паттерн **Command** для обработки команд
- `logging` для записи логов

---

## Структура проекта

    picToTextBot/
    │── bot.py
    │── logger.py
    │── requirements.txt
    │── README.md
    │
    └── commands/
        │── start_command.py
        │── recognize_command.py
        │── translate_command.py

---

## Быстрый старт (локально)

### Требования:

- Python 3.10+ (рекомендуется)
- Tesseract OCR установлен в системе (см. ниже)

1. Клонируйте репозиторий:


    git clone <ваш-репо>.git
    cd picToTextBot

2. Создайте виртуальное окружение и установите зависимости:


    python -m venv .venv
    source .venv/bin/activate  # linux / mac
    .venv\Scripts\activate     # windows
    pip install -r requirements.txt

3. Установите Tesseract OCR (пример для Ubuntu/Debian):

    
    sudo apt update
    sudo apt install tesseract-ocr

Для других платформ — используйте официальную документацию: https://github.com/tesseract-ocr/tesseract

4. Создайте файл .env или экспортируйте переменные окружения:


    TELEGRAM_TOKEN=ваш_токен_бота
    TESSERACT_CMD=/usr/bin/tesseract  # если tesseract не на PATH

5. Запуск


    python bot.py