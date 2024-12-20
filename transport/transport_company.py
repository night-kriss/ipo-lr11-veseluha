from .vehicle import Vehicle
from .client import Client

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("vehicle must be an instance of Vehicle")
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        return self.vehicles

    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError("client must be an instance of Client")
        self.clients.append(client)

    def optimize_cargo_distribution(self):
        self.clients.sort(key=lambda x: x.is_vip, reverse=True)
        for client in self.clients:
            for vehicle in self.vehicles:
                try:
                    vehicle.load_cargo(client)
                    break
                except ValueError:
                    continue
