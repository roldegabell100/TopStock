class Stock:
    def __init__(self, stockdata) -> None:
        self.exchange = stockdata['exchange']
        self.currency = stockdata['currency']
        self.open_price = stockdata['open']
        self.high_price = stockdata['high']
        self.low_price = stockdata['low']
        self.close_price = stockdata['close']
        self.name = stockdata['name']
        self.stock_price = stockdata['stock_price']

    # @classmethod
    # def get_all(cls, stockdata):
    #     query = "SELECT * FROM users;"
    #     results = connectToMySQL('TopStock').query_db(query)
    #     stocks = []
    #     for u in results:
    #         stocks.append(cls(u))
    #     return stock