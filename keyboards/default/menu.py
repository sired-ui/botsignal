from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔊 Включение бота"),
        ],
        [
            KeyboardButton(text="🔔 Мои сигналы"),
        ],
        [
            KeyboardButton(text="📋 О боте"),
        ],
        [
            KeyboardButton(text="🔇 Отключить")
        ],
    ],
    resize_keyboard=True
)

on_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Long"),
        ],
        [
            KeyboardButton(text="Short"),
        ],
        [
            KeyboardButton(text="Главное меню"),
        ],
    ],
    resize_keyboard=True
)

stock_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bitmex"),
        ],
        [
            KeyboardButton(text="Binance"),
        ],
        [
            KeyboardButton(text="Bybit"),
        ],
        [
            KeyboardButton(text="Okex"),
        ],
        [
            KeyboardButton(text="Huobi"),
        ],
        [
            KeyboardButton(text="FTX"),
        ],
        [
            KeyboardButton(text="Deribit"),
        ],
        [
            KeyboardButton(text="Kraken"),
        ],
        [
            KeyboardButton(text="Bitfinex"),
        ],
        [
            KeyboardButton(text="AAX"),
        ],
        [
            KeyboardButton(text="Тип сигнала"),
        ],
    ],
    resize_keyboard=True
)

time_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='5min')
        ],
        [
            KeyboardButton(text='1H')
        ],
        [
            KeyboardButton(text='4H')
        ],
    ],
    resize_keyboard=True
)