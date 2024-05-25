

class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1000000
    def horse_powers(self):
        return
class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "Машина"
        self.price = 1200000
    def horse_powers(self):
        return 150
nissan_car = Nissan()
print(nissan_car.vehicle_type)
print(nissan_car.price)
