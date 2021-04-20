from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import mainmenu, on_menu, stock_menu
from loader import dp
import json

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!",reply_markup=mainmenu)
    with open('data/base.json','r',encoding='utf-8') as file:
        try:
            data = json.loads(file.read())['data'][str(message.from_user.id)]
        except:
            data = {
                "Long": {
                    "Bitmex": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Binance": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "TRX": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BAND": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "UNI": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Bybit": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Okex": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BSV": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "TRX": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BAND": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "UNI": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Huobi": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BSV": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "TRX": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BAND": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "UNI": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "FTX": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BSV": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "TRX": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BAND": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "UNI": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Deribit": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Kraken": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Bitfinex": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "AAX": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    }
                },
                "Short": {
                    "Bitmex": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Binance": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "TRX": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BAND": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "UNI": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Bybit": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Okex": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BSV": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "TRX": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BAND": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "UNI": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Huobi": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BSV": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "TRX": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BAND": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "UNI": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "FTX": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "EOS": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "XRP": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BSV": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "TRX": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ADA": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BAND": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "UNI": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Deribit": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Kraken": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "Bitfinex": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    },
                    "AAX": {
                        "BTC": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "ETH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "BCH": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        },
                        "LINK": {
                            "5min": 0,
                            "1H": 0,
                            "4H": 0
                        }
                    }
                }
            }
            with open('data/base.json','r',encoding='utf-8') as file:
                base = json.loads(file.read())
            base['data'].update({str(message.from_user.id):data})
            with open('data/base.json','w',encoding='utf-8') as file:
                json.dump(base, file, ensure_ascii=False, indent=4)