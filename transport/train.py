from .vehicle import Vehicle

class Train(Vehicle):
    def __init__(self, capacity, number_of_cars):
        super().__init__(capacity)
        self.number_of_cars = number_of_cars
