import threading
import time


class Magazyn:
    def __init__(self):
        self.miejsce_skladowania = []
        self.transportery = []
        self.wozki_widlowe = []

    def dodaj_do_magazynu(self, towar):
        self.miejsce_skladowania.append(towar)

    def usun_z_magazynu(self, towar):
        self.miejsce_skladowania.remove(towar)


class Pracownik(threading.Thread):
    def __init__(self, id, magazyn):
        threading.Thread.__init__(self)
        self.id = id
        self.magazyn = magazyn
