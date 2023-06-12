import threading

class StockKeepingUnit:
    id = 0
    lock = threading.Lock()
    stock = None

    def add_stock(self, stock):
        self.stock = stock

    def __init__(self, id):
        self.id = id
