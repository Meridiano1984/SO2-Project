import random

from DeliverySite import DeliverySite
from ReceivingSite import ReceivingSite
from Stock import Stock
from Warehouse import Warehouse
from Worker import Worker


class Building:
    deliverySites: DeliverySite = []
    receivingSites: ReceivingSite = []
    warehouse: Warehouse = 0
    workers: Worker = []

    def __init__(self, quantityOfDeliverySites, quantityOfReceivingSite, quantityOfworkers, warehouseSize):
        self.createDeliverySite(quantityOfDeliverySites)
        self.createReicievingSite(quantityOfReceivingSite)
        self.createWorkers(quantityOfworkers)
        self.warehouse = Warehouse(warehouseSize)

    def createDeliverySite(self, quantityOfDeliverySites):
        for i in range(quantityOfDeliverySites):
            self.deliverySites.append(DeliverySite(i))

    def createReicievingSite(self, quantityOfDeliverySites):
        for i in range(quantityOfDeliverySites):
            self.receivingSites.append(ReceivingSite(i))

    def createWorkers(self, quantityOfworkers):
        for i in range(quantityOfworkers):
            self.workers.append(Worker(i))

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
                    site.add_stock(Stock(random.randint(1,100)))
                    break

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
