from .vehicle import Vehicle

class Airplane(Vehicle):
    def __init__(self, capacity, max_altitude):
        super().__init__(capacity)
        self.max_altitude = max_altitude
