import time
import threading
import copy

from DeliverySite import DeliverySite
from FileLogHandler import FileLogHandler
from Statistics import Statistics
from Warehouse import Warehouse
from Worker import Worker
from ReceivingSite import ReceivingSite

class WorkerManagementService:

    statistic_collector: Statistics = None
    file_log_handler: FileLogHandler = None

    def __init__(self, statistic_collector, file_log_handler):
        self.statistic_collector = statistic_collector
        self.file_log_handler = file_log_handler


    def move_stock_from_receiving_site_to_warehouse(self, workers, receivingSites, warehouse):
        # Sprawdzamy czy sa wolni workerzy i czy sa stacja wolene ktore maja Stock
        for worker in workers:
            if isinstance(worker, Worker) and not worker.lock.locked():
                # print(f"Wolny pracownik o id:{worker.id}")
                for receivingSite in receivingSites:
                    if isinstance(receivingSite, ReceivingSite) and not receivingSite.lock.locked() and receivingSite.stock is not None:
                        # print(f"Wolna stacja o id:{receivingSite.id}")
                        # print(f"Wolny pracownik o id:{worker.id}")
                        # print(f"Pracosnik o id:{worker.id}, rozpoczyna zadanie ze stacja przyjmujacej o id:{receivingSite.id}")
                        worker.lock.acquire()
                        receivingSite.lock.acquire()
                        try:
                            # rozpoczynamy symulowanie ruchu do stacji
                            # nie wiem czy tu nie powinnnismy robic deep copy
                            time.sleep(5.0)
                            worker.take_stock(receivingSite.stock)
                            receivingSite.stock = None
                            self.statistic_collector.add_received_stock_id(worker.stock.id)
                            etap_2_log = f"ETAP 2: Pracownik o id:{worker.id} odebral Stok o UUID:{worker.stock.id} ze stacji przyjmujacej o id:{receivingSite.id}"
                            print(etap_2_log)
                            self.file_log_handler.append_log(etap_2_log)
                            # print(f"Pracownik o id:{worker.id} odebral przesylke z stacji przyjmujacej o id:{receivingSite.id}")

                            time.sleep(2.0)

                            # szukamy wolnego miejsca w gridzie
                            if isinstance(warehouse, Warehouse):
                                for sku in warehouse.grid:
                                    if not sku.lock.locked() and sku.stock is None:
                                        # todo nie obsluguje kiedy magazyn jet pełny
                                        try:
                                            sku.lock.acquire()
                                            sku.add_stock(worker.stock)
                                            worker.stock = None
                                            # print(f"Pracownik o id:{worker.id} dostarczył przesylke do miejsca o id:{sku.id}")
                                            etap_3_log = f"ETAP 3: Pracownik o id:{worker.id} przeniosl Stok o UUID:{sku.stock.id} do sku o id:{sku.id}"
                                            print(etap_3_log)
                                            self.file_log_handler.append_log(etap_3_log)

                                        finally:
                                            sku.lock.release()
                                            return
                                        # kod do ewentualnego rozwarznei przypadku pelenego grida
                                        # else:
                                        # print("Nie ma wolnego miejsca w magazynie, Stock jest zwracany na stacje przyjmujacej")
                                        # receivingSite.add_stock_no_lock(worker.stock)
                                        # worker.stock = None
                                        # print(f"Pracownik o id:{worker.id} zwrocil przesylke do stacji przyjmujacej o id:{receivingSite.id}")
                        finally:
                            worker.lock.release()
                            receivingSite.lock.release()


    def move_stock_from_warehouse_to_delivery_site(self, workers, deliverySites, warehouse):
        # Sprawdzamy czy sa wolni workerzy i czy sa stacja wolene ktore maja Stock
        for worker in workers:
            if isinstance(worker, Worker) and not worker.lock.locked():
                if isinstance(warehouse, Warehouse):
                    for sku in warehouse.grid:
                        if not sku.lock.locked() and sku.stock is not None:
                                for deliverySite in deliverySites:
                                    if isinstance(deliverySite, DeliverySite):
                                        worker.lock.acquire()
                                        sku.lock.acquire()
                                        deliverySite.lock.acquire()
                                        # print(f"ETAP 3: Pracownik o id:{worker.id} przeniosl przesylke o UUID:{worker.stock.id} do sku o id:{sku.id}")
                                        # todo zmien logow i nr etapow
                                        etap_4_log = f"THREAD 2, ETAP 4: Pracownik o id:{worker.id} rozpoczyna przenisienie Stok o UUID:{sku.stock.id} z sku o id:{sku.id} do deliverySite o id:{deliverySite.id}"
                                        print(etap_4_log)
                                        self.file_log_handler.append_log(etap_4_log)
                                        try:
                                            # rozpoczynamy symolowanie przenosszeni stocku
                                            time.sleep(1.0)
                                            worker.take_stock(sku.stock)
                                            sku.stock = None

                                            # print(f"THREAD 2 Pracownik o id:{worker.id} odebral Stok z sku o id:{sku.id} ")
                                            etap_5_log = f"THREAD 2, ETAP 5: Pracownik o id:{worker.id} odebral Stok o UUID:{worker.stock.id} z sku o id:{sku.id}"
                                            print(etap_5_log)
                                            self.file_log_handler.append_log(etap_5_log)

                                            time.sleep(2.0)
                                            deliverySite.take_stock(worker.stock)
                                            worker.stock = None
                                            self.statistic_collector.add_delivered_stock_id(deliverySite.stock.id)
                                            # print(f"THREAD 2, ETAP 5: Pracownik o id:{worker.id} odebral Stok o UUID:{worker.stock.id} z sku o id:{sku.id}")
                                            etap_6_log = f"THREAD 2, ETAP 6: Pracownik o id:{worker.id} przeniosl Stok o UUID:{deliverySite.stock.id} do deliverySite o id:{deliverySite.id}"
                                            print(etap_6_log)
                                            self.file_log_handler.append_log(etap_6_log)
                                            deliverySite.stock = None
                                            return
                                        finally:
                                            worker.lock.release()
                                            sku.lock.release()
                                            deliverySite.lock.release()












