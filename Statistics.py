from DeliverySite import DeliverySite
from ReceivingSite import ReceivingSite
from Worker import Worker


class Statistics:

    stocks_received_id_list = []
    stocks_delivered_id_list = []
    worker_id_list = []
    receiving_stations_id_list = []
    delivery_stations_id_list = []
    stock_keeping_units_id_list = []

    def __init__(self, workers, receiving_stations, delivery_stations, stock_keeping_units):
        for worker in workers:
            if isinstance(worker, Worker):
                self.worker_id_list.append(worker.id)
        for receiving_station in receiving_stations:
            if isinstance(receiving_station, ReceivingSite):
                self.receiving_stations_id_list.append(receiving_station.id)
        for delivery_station in delivery_stations:
            if isinstance(delivery_station, DeliverySite):
                self.delivery_stations_id_list.append(delivery_station.id)
        for stock_keeping_unit in stock_keeping_units:
            if isinstance(stock_keeping_unit, Worker):
                self.stock_keeping_units_id_list.append(stock_keeping_unit.id)

    def add_delivered_stock_id(self, uuid):
        self.stocks_delivered_id_list.append(uuid)

    def add_received_stock_id(self, uuid):
        self.stocks_received_id_list.append(uuid)

    def print_stocks_delicered_id_list(self):
        print("UUID Delivered Stock")
        i = 1
        for stock_id in self.stocks_delivered_id_list:
            print(f"{i}.{stock_id}")
            i+=1

    def print_stocks_received_id_list(self):
        print("UUID Received Stock")
        i = 1
        for stock_id in self.stocks_received_id_list:
            print(f"{i}.{stock_id}")
            i+=1

    def print_worker_id_list(self):
        print("UUID Workers")
        i = 1
        for worker in self.worker_id_list:
            print(f"{i}.{worker}")
            i+=1

    def print_receiving_stations_id_list(self):
        print("UUID Receiving Stations")
        i = 1
        for station in self.receiving_stations_id_list:
            print(f"{i}.{station}")
            i += 1

    def print_receiving_delivery_stations_id_list(self):
        print("UUID Delivery Stations")
        i = 1
        for station in self.delivery_stations_id_list:
            print(f"{i}.{station}")
            i += 1

    def print_receiving_stock_keeping_units_id_list(self):
        print("UUID SKUS")
        i = 1
        for sku in self.stock_keeping_units_id_list:
            print(f"{i}.{sku}")
            i += 1

    def print_all_stats(self):
        print("\nStats\n")
        self.print_stocks_received_id_list()
        print("\n")
        self.print_stocks_delicered_id_list()
        print("\n")
        self.print_worker_id_list()
        print("\n")
        self.print_receiving_stations_id_list()
        print("\n")
        self.print_receiving_delivery_stations_id_list()
        print("\n")
        self.print_receiving_stock_keeping_units_id_list()