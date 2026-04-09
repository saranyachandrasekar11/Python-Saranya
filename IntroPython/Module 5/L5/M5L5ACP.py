class BMW:
    def fuel_type(self):
        return "Diesel"
    
    def max_speed(self):
        return "240 km/h"

class Ferrari:
    def fuel_type(self):
        return "Gasoline"
    
    def max_speed(self):
        return "340 km/h"

# Polymorphic function
def display_car_info(car):
    print(f"Fuel type: {car.fuel_type()}")
    print(f"Max speed: {car.max_speed()}")

# Create objects
car1 = BMW()
car2 = Ferrari()

# Implementation of polymorphism
for car in (car1, car2):
    print(f"--- {car.__class__.__name__} ---")
    display_car_info(car)
