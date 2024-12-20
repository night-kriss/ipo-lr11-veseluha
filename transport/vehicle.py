import uuid
from .client import Client

class Vehicle:
    def __init__(self, capacity):
        self.vehicle_id = str(uuid.uuid4())
        self.capacity = capacity
        self.current_load = 0
        self.clients_list = []

    def load_cargo(self, client):
        if not isinstance(client, Client):
            raise TypeError("client must be an instance of Client")
        if self.current_load + client.cargo_weight > self.capacity:
            raise ValueError("Exceeding vehicle capacity")
        self.current_load += client.cargo_weight
        self.clients_list.append(client)

    def __str__(self):
        return f"ID: {self.vehicle_id}, Capacity: {self.capacity}, Current Load: {self.current_load}"
