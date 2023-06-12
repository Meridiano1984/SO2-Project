import threading
import time

from Building import Building
from FileLogHandler import FileLogHandler
from Statistics import Statistics

menu = """////----MENU----////
          1 -> uruchom symulacje magazynu
          2 -> zakoncz symulacje magazynu
          3 -> prezentacja statystyk
          4 -> wyjdz z programu
          """


import threading
import time

from WorkerManagementService import WorkerManagementService



time_to_delivery_stock = 3.5


# menu = """dodanie robotnika w, dodanie stacji odbierajcaej r, dodanie stacji wydajacej d, dodanie stocku do reaciving station k, wyjdz 'kill' """
log_handler = FileLogHandler()
log_handler.clear_file()
building = Building(4,4,10,20,log_handler)
statistic_collector = Statistics(building.workers, building.receivingSites, building.deliverySites, building.warehouse.grid)
worker_managment_service = WorkerManagementService(statistic_collector, log_handler)



# Współdzielona wartość
value = 0

# Flaga informująca, czy wątek powinien zostać zakończony
should_exit = False

def printing_response(array_response):
    for log in array_response:
        fixed_log = log[:-2]
        print(fixed_log)

def statistic_menu():
    min_menu ="""////----operacje na logach
                 1-> znajdz hisotirie stock o wybranym id
                 2-> znajdz wszystkie zamowiania danego workera
                 3-> przesledz historie danego sku
                 4-> przesledz historie danej stacji odbierajacej
                 5-> przesledz historie danej stacji wydajacej"""
    choice = input("->: ")
    if choice == "1":
        statistic_collector.print_stocks_delicered_id_list()
        statistic_collector.print_stocks_received_id_list()
        UUID_choice = input("Poddaj UUID ktore chcesz znalezc->: ")
        printing_response(log_handler.find_lines_with_phrase(UUID_choice))
        # print(response)
    elif choice == "2":
        statistic_collector.print_worker_id_list()
        UUID_choice = input("Poddaj UUID ktore chcesz znalezc->: ")
        printing_response(log_handler.find_lines_with_phrase(UUID_choice))
    elif choice == "3":
        statistic_collector.print_receiving_stock_keeping_units_id_list()
        UUID_choice = input("Poddaj UUID ktore chcesz znalezc->: ")
        printing_response(log_handler.find_lines_with_phrase(UUID_choice))
    elif choice == "4":
        statistic_collector.print_receiving_stations_id_list()
        UUID_choice = input("Poddaj UUID ktore chcesz znalezc->: ")
        printing_response(log_handler.find_lines_with_phrase(UUID_choice))
    elif choice == "5":
        statistic_collector.print_receiving_delivery_stations_id_list()
        UUID_choice = input("Poddaj UUID ktore chcesz znalezc->: ")
        printing_response(log_handler.find_lines_with_phrase(UUID_choice))

# Funkcja dla wątku wczytującego znaki
def read_input():
    global value
    global should_exit
    global building
    while not False:
        print(menu)
        # Wczytanie znaku z klawiatury
        input_char = input("->: ")
        if input_char == "w":
            building.add_worker()
        elif input_char == "d":
            building.add_delivery_site()
        # elif input_char == "1":
        #     simulation_start()
        # elif input_char == "2":
        #     simulation_stop()
        elif input_char == "3":
            statistic_collector.print_all_stats()
        elif input_char == "5":
            statistic_menu()
        elif input_char == "r":
            building.add_receiving_sites()
        elif input_char == "k":
            building.add_stock_to_receiving_sites()
        elif input_char == "kill":
            should_exit = True
            break


        # print(building.__str__())

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

def moving_stock_from_receiving_station_to_warehouse():
    global building
    global worker_managment_service
    while not should_exit:
        worker_managment_service.move_stock_from_receiving_site_to_warehouse(building.workers, building.receivingSites, building.warehouse)

def move_stock_from_warehouse_to_delivery_site():
    global building
    global worker_managment_service
    while not should_exit:
        worker_managment_service.move_stock_from_warehouse_to_delivery_site(building.workers, building.deliverySites, building.warehouse)


# Funkcja dla wątku inkrementującego wartość co sekundę
def increment_value():
    global value
    while not should_exit:
        # Inkrementacja wartości
        value += 1
        # print(f'Wartość: {value}')

        # Odczekanie sekundy
        time.sleep(1)

# print(menu)

# Tworzenie wątków

input_thread = threading.Thread(target=read_input)
input_thread.start()

# creating_stock_thread: threading.Thread = None
# moving_stock_from_receiving_station_to_warehouse_thread: threading.Thread = None
# moving_stock_from_warehouse_to_delivery_site_thread: threading.Thread = None

# increment_thread = threading.Thread(target=increment_value)
creating_stock_thread = threading.Thread(target=creating_stock)
moving_stock_from_receiving_station_to_warehouse_thread = threading.Thread(
    target=moving_stock_from_receiving_station_to_warehouse)
moving_stock_from_warehouse_to_delivery_site_thread = threading.Thread(
    target=move_stock_from_warehouse_to_delivery_site)


# def simulation_start():
    # if status == "1":


        # Uruchamianie wątków
        # increment_thread.start()
creating_stock_thread.start()
moving_stock_from_receiving_station_to_warehouse_thread.start()
moving_stock_from_warehouse_to_delivery_site_thread.start()
    # if status == "2":
    #     creating_stock_thread.join()
    #     moving_stock_from_receiving_station_to_warehouse_thread.join()
    #     moving_stock_from_warehouse_to_delivery_site_thread.join()


# Czekanie na zakończenie wątków
# increment_thread.join()
# def simulation_stop():
creating_stock_thread.join()
moving_stock_from_receiving_station_to_warehouse_thread.join()
moving_stock_from_warehouse_to_delivery_site_thread.join()

worker_managment_service.statistic_collector.print_all_stats()

input_thread = threading.Thread(target=read_input)
input_thread.start()

print("cooooo")
input_thread.join()





def exit_program():
    input_thread.join()
    print(value)


