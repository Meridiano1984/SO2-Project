from StockKeepingUnit import StockKeepingUnit


class Warehouse:
    grid = []

    def __init__(self, size):
        self.grid = [[StockKeepingUnit(i, j)for j in range(size)] for i in range(size)]




