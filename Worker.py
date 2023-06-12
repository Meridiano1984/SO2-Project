import threading

import ResourceState
import Stock


class Worker:
    id = 0
    stock: Stock = None
    lock = threading.Lock()

    def __init__(self, id):
        self.id = id
        self.stock = None
        # self.state = ResourceState

    def take_stock(self, stock):
        self.stock = stock

    def __str__(self):
        return "id = " + str(self.id)