import json
import logging

from aiogram.dispatcher import FSMContext
from bs4 import BeautifulSoup

from keyboards.inline.callback_datas import stocks_callback, symbols_callback, offstocks_callback, offsymbols_callback
from keyboards.inline.choice_buttons import choice, get_symbols_menu, get_offsymbols_menu
from loader import dp
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    InlineKeyboardButton, KeyboardButton
from keyboards.default import mainmenu, on_menu, stock_menu, time_menu
from aiogram.dispatcher.filters import Command, Text
from states.parameters import Parameters, ParforOff

base_path = 'data/base.json'


@dp.message_handler(Command("menu"), state=None)
async def show_menu(message: Message):
    await message.answer("Главное меню", reply_markup=mainmenu)


@dp.message_handler(text_contains="Включение бота", state=None)
async def show_on_menu(message: Message):
    await  message.answer("Тип сигнала", reply_markup=on_menu)
    await Parameters.typeSignal.set()


@dp.message_handler(state=Parameters.typeSignal)
async def get_type_sygnal(message: Message, state=FSMContext):
    answer = message.text
    types_signals = ['Long', 'Short']
    if answer not in types_signals and answer != "Главное меню":
        await  message.answer("Тип сигнала", reply_markup=on_menu)
        await Parameters.typeSignal.set()
    elif answer == "Главное меню":
        await message.answer("Главное меню", reply_markup=mainmenu)
        await state.reset_state(with_data=False)
    else:
        async with state.proxy() as data:
            data["typeSignal"] = answer
        await state.reset_state(with_data=False)
        await message.answer(answer, reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите биржу", reply_markup=choice)
        # await Parameters.stock.set()


@dp.callback_query_handler(stocks_callback.filter())
async def get_stock(call: CallbackQuery, callback_data: dict, state=FSMContext):
    async with state.proxy() as data:
        data["stock"] = callback_data.get('name')
    symbols_menu = await get_symbols_menu(callback_data.get('name'))
    await call.message.edit_reply_markup(symbols_menu)


@dp.callback_query_handler(symbols_callback.filter())
async def get_stock(call: CallbackQuery, callback_data: dict, state=FSMContext):
    symbols = ["BTC", "ETH", "EOS", "BCH", "LTC", "XRP", "BSV", "ETC", "TRX", "ADA", "LINK", "BAND", "UNI"]
    if callback_data.get('name') not in symbols:
        pass
    else:
        async with state.proxy() as data:
            data["symbol"] = callback_data.get('name')
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Таймфрейм для " + callback_data.get('name'), reply_markup=time_menu)
        await Parameters.timeframe.set()


@dp.callback_query_handler(text='back')
async def back(call: CallbackQuery):
    await call.message.edit_reply_markup(choice)


@dp.callback_query_handler(text='offback')
async def offback(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    typesignal = data.get('typeSignal')
    markup = await all_alerts(call.from_user.id, typesignal)
    await call.message.edit_reply_markup(markup)


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Тип сигнала", reply_markup=on_menu)
    await Parameters.typeSignal.set()


@dp.callback_query_handler(text='canceloff')
async def canceloff(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Тип сигнала", reply_markup=on_menu)
    await ParforOff.typeSignal.set()


# @dp.message_handler(state=Parameters.stock)
# async def get_stock(message:Message, state=FSMContext):
#    answer = message.text
#    stocks = ["Bitmex","Binance","Bybit","Okex","Huobi","FTX","Deribit","Kraken","Bitfinex","AAX"]
#    if answer in stocks and answer!='Тип сигнала':
#        async with state.proxy() as data:
#            data["stock"] = answer
#        await message.answer("Выберите таймфрейм",reply_markup=time_menu)
#        await Parameters.timeframe.set()
#    elif answer=='Тип сигнала':
#        await  message.answer("Тип сигнала", reply_markup=on_menu)
#        await Parameters.typeSignal.set()
#    else:
#        await  message.answer("Выберите биржу", reply_markup=stock_menu)
#        await Parameters.stock.set()
# await state.reset_state(with_data=False)


async def add_to_base(data, message,p):
    sygnal = data.get('typeSignal')
    stock = data.get('stock')
    symbol = data.get('symbol')
    timeframe = data.get('timeframe')
    with open(base_path, 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    data['data'][str(message.from_user.id)][sygnal][stock][symbol][timeframe] = p
    with open(base_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    if p==1:
        await message.answer(
            "Уведомления для " + sygnal + " " + stock + " " + symbol + " " + timeframe + " успешно подключены",
            reply_markup=mainmenu)
    elif p==0:
        await message.answer(
            "Уведомления для " + sygnal + " " + stock + " " + symbol + " " + timeframe + " успешно отключены",
            reply_markup=mainmenu)


@dp.message_handler(state=Parameters.timeframe)
async def get_timeframe(message: Message, state=FSMContext):
    answer = message.text
    timeframes = ['5min', '1H', '4H']
    if answer in timeframes and answer != 'Выбор биржи':
        async with state.proxy() as data:
            data["timeframe"] = answer
        await state.reset_state(with_data=False)
        data = await state.get_data()
        await add_to_base(data, message,1)
    elif answer == 'Выбор биржи':
        await message.answer("Выберите биржу", reply_markup=stock_menu)
    else:
        await message.answer("Выберите таймфрейм", reply_markup=time_menu)
        await Parameters.timeframe.set()


@dp.message_handler(Text(equals="state"))
async def getstate(message: Message, state=FSMContext):
    data = await state.get_data()
    await message.answer(
        data.get("typeSignal") + ' ' + data.get('stock') + ' ' + data.get('symbol') + ' ' + data.get('timeframe'),
        reply_markup=mainmenu)


@dp.message_handler(text_contains="Тип позиции", state=None)
async def show_on_menu(message: Message):
    await  message.answer("Тип позиции", reply_markup=on_menu)


@dp.message_handler(Text(equals=["Главное меню"]), state=None)
async def show_on_menu(message: Message, state: FSMContext):
    await state.reset_state(with_data=False)
    await  message.answer("Главное меню", reply_markup=mainmenu)


async def get_alerts(message):
    symbols = ["BTC", "ETH", "EOS", "BCH", "LTC", "XRP", "BSV", "ETC", "TRX", "ADA", "LINK", "BAND", "UNI"]
    stocks = ["Bitmex", "Binance", "Bybit", "Okex", "Huobi", "FTX", "Deribit", "Kraken", "Bitfinex", "AAX"]
    with open(base_path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())['data']
    uid = str(message)
    sdata = {}
    for s in stocks:
        sdata.update({s: {}})
        for st in symbols:
            try:
                if data[uid]['Long'][s][st]:
                    sdata[s].update({st: {"Long": ""}})
                    if data[uid]['Long'][s][st]['5min'] == 1:
                        sdata[s][st]['Long'] += '5min\n'
                    if data[uid]['Long'][s][st]['1H'] == 1:
                        sdata[s][st]['Long'] += '1H\n'
                    if data[uid]['Long'][s][st]['4H'] == 1:
                        sdata[s][st]['Long'] += '4H\n'
            except:
                pass
            try:
                if data[uid]['Short'][s][st]:
                    sdata[s][st].update({"Short": ""})
                    if data[uid]['Short'][s][st]['5min'] == 1:
                        sdata[s][st]['Short'] += '5min\n'
                    if data[uid]['Short'][s][st]['1H'] == 1:
                        sdata[s][st]['Short'] += '1H\n'
                    if data[uid]['Short'][s][st]['4H'] == 1:
                        sdata[s][st]['Short'] += '4H\n'
            except:
                pass
    send_text = 'Long сигналы:\n'
    for s in stocks:
        send_text += '??'
        c = 0
        for st in symbols:
            try:
                if sdata[s][st]['Long'] != '':
                    send_text += '<i>' + st + '</i>\n'
                    send_text += '<code>' + sdata[s][st]['Long'] + '</code>\n'
                    c += 1
            except:
                pass
        if c > 0:
            name = '_____________________\n<b>' + s + '</b>\n'
            send_text = send_text.replace('??', name)
        else:
            send_text = send_text.replace('??', '')
    send_text += 'Short сигналы:\n'
    for s in stocks:
        send_text += '??'
        c = 0
        for st in symbols:
            try:
                if sdata[s][st]['Short'] != '':
                    send_text += '<i>' + st + '</i>\n'
                    send_text += '<code>' + sdata[s][st]['Short'] + '</code>\n'
                    c += 1
            except:
                pass
        if c > 0:
            name = '_____________________\n<b>' + s + '</b>\n'
            send_text = send_text.replace('??', name)
        else:
            send_text = send_text.replace('??', '')
    return send_text


async def all_alerts(message,typesignal):
    send_text = await get_alerts(message)
    if typesignal == 'Long':
        longs = send_text.split('\nShort сигналы:\n')[0].replace('Long сигналы:', '').replace('\n', '')
        soup = BeautifulSoup(longs, 'lxml')
        bs = soup.find_all('b')
        markup = InlineKeyboardMarkup()
        for b in bs:
            markup.insert(InlineKeyboardButton(text=b.text, callback_data='offstock:' + b.text))
        markup.insert(InlineKeyboardButton(text="Отмена", callback_data="canceloff"))
        return markup
    elif typesignal == 'Short':
        short = send_text.split('\nShort сигналы:\n')[1].replace('\n', '')
        soup = BeautifulSoup(short, 'lxml')
        bs = soup.find_all('b')
        markup = InlineKeyboardMarkup()
        for b in bs:
            markup.insert(InlineKeyboardButton(text=b.text,callback_data='offstock:'+b.text))
        markup.insert(InlineKeyboardButton(text="Отмена", callback_data="canceloff"))
        return markup


async def cur_symbols(message,typesignal):
    send_text = await get_alerts(message)
    longs = send_text.split('\nShort сигналы:\n')[0].replace('Long сигналы:', '')
    short = send_text.split('\nShort сигналы:\n')[1].split('_____________________')
    short.remove('')
    longs = longs.split('_____________________')
    longs.remove('\n')
    data = {}
    if typesignal == "Long":
        for l in longs:
            soup = BeautifulSoup(l, 'lxml')
            data.update({soup.find('b').text: {}})
            all_i = soup.find_all('i')
            all_codes = soup.find_all('code')
            for i in range(len(all_i)):
                alc = all_codes[i].text.split('\n')
                alc.remove('')
                data.update({soup.find('b').text: {all_i[i].text: alc}})
        return data
    elif typesignal == "Short":
        for l in short:
            soup = BeautifulSoup(l, 'lxml')
            data.update({soup.find('b').text: {}})
            all_i = soup.find_all('i')
            all_codes = soup.find_all('code')
            for i in range(len(all_i)):
                alc = all_codes[i].text.split('\n')
                alc.remove('')
                data.update({soup.find('b').text: {all_i[i].text: alc}})
        return data

@dp.callback_query_handler(offstocks_callback.filter())
async def get_offstock(call: CallbackQuery, callback_data: dict, state=FSMContext):
    try:
        async with state.proxy() as data:
            data["stock"] = callback_data.get('name')
        async with state.proxy() as data:
            typeSignal = data["typeSignal"]
        symbols_menu = await cur_symbols(call.from_user.id,typeSignal)
        keys = symbols_menu[callback_data.get('name')].keys()
        symbols = list(keys)
        markup = InlineKeyboardMarkup()
        for s in symbols:
            markup.insert(InlineKeyboardButton(text=s,callback_data="offsymbol:"+s))
        await call.message.edit_reply_markup(markup)
    except:
        await call.message.answer("Меню устарело",reply_markup=mainmenu)
        await call.message.edit_reply_markup(None)


@dp.callback_query_handler(offsymbols_callback.filter())
async def get_stock(call: CallbackQuery, callback_data: dict, state=FSMContext):
    try:
        symbols = ["BTC", "ETH", "EOS", "BCH", "LTC", "XRP", "BSV", "ETC", "TRX", "ADA", "LINK", "BAND", "UNI"]
        if callback_data.get('name') not in symbols:
            pass
        else:
            async with state.proxy() as data:
                data["symbol"] = callback_data.get('name')
            async with state.proxy() as data:
                typeSignal = data["typeSignal"]
                stock = data["stock"]
            symbols_menu = await cur_symbols(call.from_user.id,typeSignal)
            times = symbols_menu[stock][callback_data.get('name')]
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for t in times:
                markup.insert(KeyboardButton(text=t))
            await call.message.edit_reply_markup(reply_markup=None)
            await call.message.answer("Таймфрейм для " + callback_data.get('name'), reply_markup=markup)
            await ParforOff.timeframe.set()
    except:
        await call.message.edit_reply_markup(None)
        await call.message.answer("Меню устраело",reply_markup=mainmenu)


@dp.message_handler(state=ParforOff.timeframe)
async def get_timeframe(message: Message, state=FSMContext):
    answer = message.text
    timeframes = ['5min', '1H', '4H']
    if answer in timeframes and answer != 'Выбор биржи':
        async with state.proxy() as data:
            data["timeframe"] = answer
        await state.reset_state(with_data=False)
        data = await state.get_data()
        await add_to_base(data, message,0)
    elif answer == 'Выбор биржи':
        await message.answer("Выберите биржу", reply_markup=stock_menu)
    else:
        async with state.proxy() as data:
            typeSignal = data["typeSignal"]
            stock = data["stock"]
            symbol = data["symbol"]
        symbols_menu = await cur_symbols(message.from_user.id, typeSignal)
        times = symbols_menu[stock][symbol]
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for t in times:
            markup.insert(KeyboardButton(text=t))
        await message.answer("Выберите таймфрейм", reply_markup=markup)
        await ParforOff.timeframe.set()


@dp.message_handler(text_contains="Мои сигналы", state=None)
async def show_signals(message: Message, state=FSMContext):
    data = await get_alerts(message.from_user.id)
    await message.answer(data, reply_markup=mainmenu)


@dp.message_handler(state=ParforOff.typeSignal)
async def get_type_sygnal(message: Message, state=FSMContext):
    answer = message.text
    types_signals = ['Long', 'Short']
    if answer not in types_signals and answer != "Главное меню":
        await message.answer("Тип сигнала", reply_markup=on_menu)
        await ParforOff.typeSignal.set()
    elif answer == "Главное меню":
        await message.answer("Главное меню", reply_markup=mainmenu)
        await state.reset_state(with_data=False)
    else:
        async with state.proxy() as data:
            data["typeSignal"] = answer
        await state.reset_state(with_data=False)
        await message.answer(answer, reply_markup=ReplyKeyboardRemove())
        await cur_symbols(message.from_user.id,answer)
        markup = await all_alerts(message.from_user.id,answer)
        await message.answer(answer, reply_markup=markup)


@dp.message_handler(text_contains="Отключить", state=None)
async def show_on_menu(message: Message):
    await message.answer('Тип позиции',reply_markup=on_menu)
    await ParforOff.typeSignal.set()


@dp.message_handler(text_contains="О боте", state=None)
async def about(message: Message):
    data = """Тут информация о боте"""
    await message.answer(data, reply_markup=mainmenu)
