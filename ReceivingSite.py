import threading

class ReceivingSite:
    id = 0
    stock = None
    lock = threading.Lock()

    def __init__(self, id):
        self.id = id

    def add_stock(self, stock):
        self.lock.acquire()
        try:
            self.stock = stock
        finally:
            self.lock.release()

    def __str__(self):
        if self.stock is None:
            return "Delivery Site: id:" + str(self.id) + " stock:None"
        else:
            return "Delivery Site: id:" + str(self.id) + " stock:" + str(self.stock.id)
