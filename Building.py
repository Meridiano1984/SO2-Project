import random
import uuid


from DeliverySite import DeliverySite
from FileLogHandler import FileLogHandler
from ReceivingSite import ReceivingSite
from Stock import Stock
from Warehouse import Warehouse
from Worker import Worker


class Building:
    deliverySites: DeliverySite = []
    receivingSites: ReceivingSite = []
    warehouse: Warehouse = 0
    workers: Worker = []
    file_log_handler: FileLogHandler = None

    def __init__(self, quantityOfDeliverySites, quantityOfReceivingSite, quantityOfworkers, warehouseSize, file_log_handler):
        self.createDeliverySite(quantityOfDeliverySites)
        self.createReicievingSite(quantityOfReceivingSite)
        self.createWorkers(quantityOfworkers)
        self.warehouse = Warehouse(warehouseSize)
        self.file_log_handler = file_log_handler

    def createDeliverySite(self, quantityOfDeliverySites):
        for i in range(quantityOfDeliverySites):
            self.deliverySites.append(DeliverySite(uuid.uuid4()))

    def createReicievingSite(self, quantityOfDeliverySites):
        for i in range(quantityOfDeliverySites):
            self.receivingSites.append(ReceivingSite(uuid.uuid4()))

    def createWorkers(self, quantityOfworkers):
        for i in range(quantityOfworkers):
            self.workers.append(Worker(uuid.uuid4()))

    def add_worker(self):
        self.workers.append(Worker(len(self.workers) + 1))

    def add_delivery_site(self):
        self.deliverySites.append(DeliverySite(len(self.deliverySites) + 1))

    def add_receiving_sites(self):
        self.receivingSites.append(ReceivingSite(len(self.receivingSites) + 1))

    def add_stock_to_receiving_sites(self):
        for site in self.receivingSites:
            if isinstance(site, ReceivingSite):
                if site.stock == None:
                    # todo zamien to na dodanie Managerow dodawania i dobre id np UUID
                    random_uuid = uuid.uuid4()
                    site.add_stock(Stock(random_uuid))
                    etap_1_log = f"ETAP 1: Stock o UUID:{random_uuid} zostal stworzony"
                    print(etap_1_log)
                    self.file_log_handler.append_log(etap_1_log)
                    break

    # def moveStockToWarehouse(self):
    #     for worker in self.workers:
    #         if isinstance(worker, Worker):
    #             if worker.state.ResourceState.check_state()

    def __str__(self):
        print("Magazyn:")
        print("pracownikow: " + str(len(self.workers)))
        self.display_workers()
        print("stacji przyjmujacych: " + str(len(self.receivingSites)))
        self.display_receiving_sites()
        print("stacji odbierajcych: " + str(len(self.deliverySites)))
        self.display_delivery_sites()

    def display_workers(self):
        i = 1
        for worker in self.workers:
            if isinstance(worker, Worker):
                print(str(i) + ". " + worker.__str__())
                i += 1

    def display_receiving_sites(self):
        i = 1
        for site in self.receivingSites:
            if isinstance(site, ReceivingSite):
                print(str(i) + ". " + site.__str__())
                i += 1

    def display_delivery_sites(self):
        i = 1
        for site in self.deliverySites:
            if isinstance(site, DeliverySite):
                print(str(i)  + ". " + site.__str__())
                i += 1

    def __str__(self):
        print("Magazyn:")
        print("pracownikow: " + str(len(self.workers)))
        self.display_workers()
        print("stacji przyjmujacych: " + str(len(self.receivingSites)))
        self.display_receiving_sites()
        print("stacji odbierajcych: " + str(len(self.deliverySites)))
        self.display_delivery_sites()
