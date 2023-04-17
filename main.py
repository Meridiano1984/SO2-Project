import threading
import time

from Building import Building


# class Magazyn:
#     def __init__(self):
#         self.miejsce_skladowania = []
#         self.transportery = []
#         self.wozki_widlowe = []
#
#     def dodaj_do_magazynu(self, towar):
#         self.miejsce_skladowania.append(towar)
#
#     def usun_z_magazynu(self, towar):
#         self.miejsce_skladowania.remove(towar)
#
#
# class Pracownik(threading.Thread):
#     def __init__(self, id, magazyn):
#         threading.Thread.__init__(self)
#         self.id = id
#         self.magazyn = magazyn


# def main():
#
#    # building = Building(4,4,10,20)
#
#
#
#
# if __name__ == "__main__":
#     main()



import threading
import time

time_to_delivery_stock = 3.5

menu = """dodanie robotnika w, dodanie stacji odbierajcaej r, dodanie stacji wydajacej d, dodanie stocku do reaciving station k, wyjdz 'kill' """
building = Building(4,4,10,20)


# Współdzielona wartość
value = 0

# Flaga informująca, czy wątek powinien zostać zakończony
should_exit = False

# Funkcja dla wątku wczytującego znaki
def read_input():
    global value
    global should_exit
    global building
    while not should_exit:
        # Wczytanie znaku z klawiatury
        input_char = input("Twoj wybor: ")
        if input_char == "w":
            building.add_worker()
        elif input_char == "d":
            building.add_delivery_site()
        elif input_char == "r":
            building.add_receiving_sites()
        elif input_char == "k":
            building.add_stock_to_receiving_sites()
        elif input_char == "kill":
            should_exit = True
            break


        print(building.__str__())

        # Jeśli wpisano "kill", ustaw flagę should_exit na True
        # if input_char == "kill":
        #     should_exit = True
        #     break

        # Inkrementacja wartości
        # value += 1

def creating_stock():
    global building
    while not should_exit:
        time.sleep(time_to_delivery_stock)
        # print("Jestem tutaj")
        building.add_stock_to_receiving_sites()



# Funkcja dla wątku inkrementującego wartość co sekundę
def increment_value():
    global value
    while not should_exit:
        # Inkrementacja wartości
        value += 1
        # print(f'Wartość: {value}')

        # Odczekanie sekundy
        time.sleep(1)

# Tworzenie wątków
input_thread = threading.Thread(target=read_input)
increment_thread = threading.Thread(target=increment_value)
creating_stock_thread = threading.Thread(target=creating_stock)

# Uruchamianie wątków
input_thread.start()
increment_thread.start()
creating_stock_thread.start()

# Czekanie na zakończenie wątków
input_thread.join()
increment_thread.join()
creating_stock_thread.join()
print(value)
