from transport.client import Client
from transport.train import Train
from transport.airplane import Airplane
from transport.transport_company import TransportCompany

def main():
    company = TransportCompany("My Transport Company")

    while True:
        print("\nМеню:")
        print("1. Добавить транспортное средство")
        print("2. Добавить клиента")
        print("3. Показать все транспортные средства")
        print("4. Оптимизировать распределение грузов")
        print("5. Выйти из программы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            vehicle_type = input("Введите тип транспортного средства (train/airplane): ")
            capacity = float(input("Введите грузоподъемность: "))
            if vehicle_type == 'train':
                number_of_cars = int(input("Введите количество вагонов: "))
                vehicle = Train(capacity, number_of_cars)
            elif vehicle_type == 'airplane':
                max_altitude = int(input("Введите максимальную высоту полета: "))
                vehicle = Airplane(capacity, max_altitude)
            else:
                print("Неверный тип транспортного средства")
                continue
            company.add_vehicle(vehicle)
            print("Транспортное средство добавлено.")

        elif choice == '2':
            name = input("Введите имя клиента: ")
            cargo_weight = float(input("Введите вес груза: "))
            is_vip = input("Является ли клиент VIP (yes/no): ").lower() == 'yes'
            client = Client(name, cargo_weight, is_vip)
            company.add_client(client)
            print("Клиент добавлен.")

        elif choice == '3':
            vehicles = company.list_vehicles()
            for vehicle in vehicles:
                print(vehicle)

        elif choice == '4':
            company.optimize_cargo_distribution()
            print("Распределение грузов оптимизировано.")

        elif choice == '5':
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
