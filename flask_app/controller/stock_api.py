from flask import render_template,request, redirect, session, flash, Request
import requests
from flask_app import app 
import time

api_key = "34e0c92c646d4f0085cb278d35370c39"

def get_stock_quote():
    url = f"https://api.twelvedata.com/market_movers/stocks?country=usa&outputsize=20&apikey={api_key}"
    response = requests.get(url).json()
    return response

stockdata = get_stock_quote()

symbol = stockdata["values"][0]['symbol']
current_price = stockdata["values"][0]['last']
high_price = stockdata["values"][0]['high']
low_price = stockdata["values"][0]['low']
name = stockdata["values"][0]['name']

stock_price = 0
stock = {
    "name":name,
    "symbol":symbol,
    "last":current_price,
    "high_price":high_price,
    "low_price":low_price,

    }
get_stock_quote()
print(stock)

@app.route('/index/')
def reg_log():
    return render_template('home.html', stock=stockdata["values"])



# stock
# add to database
# create a session that will save the symbol
@app.route('/watchlist',methods=['POST'])
def add_symbol():
    print(request.form['symbol'])
    return redirect('/index')

# washlist
# ticker = session['symbol']
# api_key = "34e0c92c646d4f0085cb278d35370c39"

# def get_stock_price(ticker_symbol, api):
#     url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
#     response = requests.get(url).json()
#     price = response['price'][:-3]
#     return price


# def get_stock_quote(ticker_symbol, api):
#     url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
#     response = requests.get(url).json()
#     print(response)
#     return response

# stockdata = get_stock_quote(ticker, api_key)
# stock_price = get_stock_price(ticker, api_key)

# exchange = stockdata['exchange']
# currency = stockdata['currency']
# open_price = stockdata['open']
# high_price = stockdata['high']
# low_price = stockdata['low']
# close_price = stockdata['close']
# name = stockdata['name']

# stock = {
#     "name":name,
#     "stockprice":stock_price,
#     "exchange":exchange,
#     "currency":currency,
#     "open_price":open_price,
#     "high_price":high_price,
#     "low_price":low_price,
#     "close_price":close_price
# }

# # new_stock = Stock(stock)
# print(f"{name},\n Current Price ${stock_price},\n Oping Price ${open_price}")