#Bus Fare
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Calculate base fare from the parent class
        base_amount = super().fare()
        # Add a 10% maintenance charge specifically for bus vehicles
        total_fare = base_amount + (base_amount * 0.10)
        return total_fare

# Example usage:
bus_instance = Bus(capacity=50)
print(f"Total fare for the bus: {bus_instance.fare()}")
