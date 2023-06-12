from StockKeepingUnit import StockKeepingUnit


class Warehouse:
    grid = []

    def __init__(self, size):
        self.grid = [StockKeepingUnit(i) for i in range(size)]




