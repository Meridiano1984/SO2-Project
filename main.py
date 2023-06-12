from Building import Building
from FileLogHandler import FileLogHandler
from Statistics import Statistics
import threading
import time
from WorkerManagementService import WorkerManagementService


time_to_delivery_stock = 3.5
log_handler = FileLogHandler()
log_handler.clear_file()
building = Building(4,4,10,20,log_handler)
statistic_collector = Statistics(building.workers, building.receivingSites, building.deliverySites, building.warehouse.grid)
worker_managment_service = WorkerManagementService(statistic_collector, log_handler)

# Flaga informująca, czy wątek powinien zostać zakończony
should_exit = False

def printing_response(array_response):
    for log in array_response:
        fixed_log = log[:-2]
        print(fixed_log)

def log_menu():
    min_menu ="""////----operacje na logach
                 1-> znajdz hisotirie stock o wybranym id
                 2-> znajdz wszystkie zamowiania danego workera
                 3-> przesledz historie danego sku
                 4-> przesledz historie danej stacji odbierajacej
                 5-> przesledz historie danej stacji wydajacej"""
    print(min_menu)
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

def simulation_menu():
    global should_exit
    print("Symulacja uruchominona, aby wyjsc napisz: kill")
    input_char = input()
    if input_char == "kill":
        should_exit = True

def read_input():
    global should_exit
    global building


    menuv2 = """////----MENU----////
                1-> uruchom symulacje
                2-> wylacz symulacje
                3-> pokaz statystki
                4-> eksploruj logi"""
    while not False:
        print(menuv2)
        # Wczytanie znaku z klawiatury
        input_char = input("->: ")
        if input_char == "w":
            building.add_worker()
        elif input_char == "d":
            building.add_delivery_site()
        # elif input_char == "70":
            # start_simulation()
        elif input_char == "3":
            statistic_collector.print_all_stats()
        elif input_char == "4":
            log_menu()
        elif input_char == "r":
            building.add_receiving_sites()
        elif input_char == "k":
            building.add_stock_to_receiving_sites()
        elif input_char == "s":
            should_exit = True
            break


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


input_thread = threading.Thread(target=read_input)
input_thread.start()

temp_fixture = input("")

creating_stock_thread = threading.Thread(target=creating_stock)
moving_stock_from_receiving_station_to_warehouse_thread = threading.Thread(target=moving_stock_from_receiving_station_to_warehouse)
moving_stock_from_warehouse_to_delivery_site_thread = threading.Thread(target=move_stock_from_warehouse_to_delivery_site)

creating_stock_thread.start()
moving_stock_from_receiving_station_to_warehouse_thread.start()
moving_stock_from_warehouse_to_delivery_site_thread.start()

creating_stock_thread.join()
moving_stock_from_receiving_station_to_warehouse_thread.join()
moving_stock_from_warehouse_to_delivery_site_thread.join()
input_thread.join()

# nowe
input_thread2 = threading.Thread(target=read_input)
input_thread2.start()

# print("cooooo")
input_thread2.join()






