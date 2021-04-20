from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import stocks_callback, symbols_callback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bitmex", callback_data="stock:Bitmex"),
            InlineKeyboardButton(text="Binance", callback_data="stock:Binance"),
        ],
        [
            InlineKeyboardButton(text="Bybit", callback_data="stock:Bybit"),
            InlineKeyboardButton(text="Okex", callback_data="stock:Okex"),
        ],
        [
            InlineKeyboardButton(text="Huobi", callback_data="stock:Huobi"),
            InlineKeyboardButton(text="FTX", callback_data="stock:FTX"),
        ],
        [
            InlineKeyboardButton(text="Deribit", callback_data="stock:Deribit"),
            InlineKeyboardButton(text="Kraken", callback_data="stock:Kraken"),
        ],
        [
            InlineKeyboardButton(text="Bitfinex", callback_data="stock:Bitfinex"),
            InlineKeyboardButton(text="AAX", callback_data="stock:AAX"),
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel"),
        ]
    ]
)


async def get_symbols_menu(stock):
    symbols = {
        "Bitmex": ["BTC", "ETH", "EOS", "BCH", "LTC", "XRP", "ADA", "LINK"],
        "Binance": ["BTC", "ETC", "ETH", "EOS", "BCH", "LTC", "XRP", "TRX", "ADA", "LINK", "BAND", "UNI"],
        "Bybit": ["BTC", "ETH", "EOS", "BCH", "LTC", "XRP"],
        "Okex": ["BTC", "ETC", "ETH", "EOS", "BCH", "LTC", "XRP", "BSV", "TRX", "ADA", "LINK", "BAND", "UNI"],
        "Huobi": ["BTC", "ETC", "ETH", "EOS", "BCH", "LTC", "XRP", "BSV", "TRX", "ADA", "LINK", "BAND", "UNI"],
        "FTX": ["BTC", "ETC", "ETH", "EOS", "BCH", "LTC", "XRP", "BSV", "TRX", "ADA", "LINK", "BAND", "UNI"],
        "Deribit": ["BTC", "ETH"],
        "Kraken": ["BTC", "ETH", "BCH", "LTC"],
        "Bitfinex": ["BTC", "ETH"],
        "AAX": ["BTC", "ETH", "BCH", "LINK"]}
    symbols = symbols[stock]
    symbols_menu = InlineKeyboardMarkup(row_width=2)
    for s in symbols:
        symbols_menu.insert(InlineKeyboardButton(text=s,callback_data="symbol:"+s))
    symbols_menu.insert(InlineKeyboardButton(text='Назад', callback_data="back"))
    symbols_menu.row(InlineKeyboardButton(text="Монеты " + stock, callback_data="stock"))
    return symbols_menu


async def get_offsymbols_menu(stock):
    symbols = {
        "Bitmex": ["BTC", "ETH", "EOS", "BCH", "LTC", "XRP", "ADA", "LINK"],
        "Binance": ["BTC", "ETC", "ETH", "EOS", "BCH", "LTC", "XRP", "TRX", "ADA", "LINK", "BAND", "UNI"],
        "Bybit": ["BTC", "ETH", "EOS", "BCH", "LTC", "XRP"],
        "Okex": ["BTC", "ETC", "ETH", "EOS", "BCH", "LTC", "XRP", "BSV", "TRX", "ADA", "LINK", "BAND", "UNI"],
        "Huobi": ["BTC", "ETC", "ETH", "EOS", "BCH", "LTC", "XRP", "BSV", "TRX", "ADA", "LINK", "BAND", "UNI"],
        "FTX": ["BTC", "ETC", "ETH", "EOS", "BCH", "LTC", "XRP", "BSV", "TRX", "ADA", "LINK", "BAND", "UNI"],
        "Deribit": ["BTC", "ETH"],
        "Kraken": ["BTC", "ETH", "BCH", "LTC"],
        "Bitfinex": ["BTC", "ETH"],
        "AAX": ["BTC", "ETH", "BCH", "LINK"]}
    symbols = symbols[stock]
    symbols_menu = InlineKeyboardMarkup(row_width=2)
    for s in symbols:
        symbols_menu.insert(InlineKeyboardButton(text=s,callback_data="symbol:"+s))
    symbols_menu.insert(InlineKeyboardButton(text='Назад', callback_data="offback"))
    symbols_menu.row(InlineKeyboardButton(text="Монеты " + stock, callback_data="stock"))
    return symbols_menu