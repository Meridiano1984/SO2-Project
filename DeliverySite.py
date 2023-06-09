import threading

from Stock import Stock


class DeliverySite:
    id = 0
    stock: Stock = None
    lock = threading.Lock()

    def __init__(self, id):
        self.id = id

    def take_stock(self, stock):
        self.stock = stock

    def __str__(self):
        if self.stock is None:
            return "Delivery Site: id:" + str(self.id) + " stock:None"
        else:
            return "Delivery Site: id:" + str(self.id) + " stock:" + str(self.stock.id)
