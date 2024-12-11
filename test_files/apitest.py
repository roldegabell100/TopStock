from flask import render_template,request, redirect, session, flash, Request
import requests
from flask_app import app 
import time
# from models.stock import Stock

api_key = "34e0c92c646d4f0085cb278d35370c39"

# def get_stock_price(api_key):
#     url = f"https://api.twelvedata.com/market_movers/stocks?country=usa&outputsize=20&apikey={api_key}"
#     response = requests.get(url).json()
#     price = response['price'][:-3]
#     return price



def get_stock_quote(api_key):
    url = f"https://api.twelvedata.com/market_movers/stocks?country=usa&outputsize=20&apikey={api_key}"
    response = requests.get(url).json()
    # print(response)
    time.sleep(2)
    return response

stockdata = get_stock_quote(api_key)
# stock_price = get_stock_price(api_key)

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
# # new_stock = Stock(stock)
# print(f"{name},\n Current Price ${stock_price},\n Oping Price ${open_curr}")

@app.route('/index/')
def reg_log():
    return render_template('home.html', stock=stockdata["values"])
