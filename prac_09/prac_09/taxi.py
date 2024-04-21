from random import randint
from car import Car

class Taxi(Car):
    """A class representing a Taxi."""

    price_per_km = 1.23

    def __init__(self, name, fuel):
        super().__init__(name, fuel)

class EcoTaxi(Taxi):
    """A class representing an Eco Taxi."""

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.price_per_km *= 0.9  # 10% discount

    def drive(self, distance):
        """Drive the taxi a given distance."""
        distance_driven = super().drive(distance)
        self.fuel -= distance_driven / 2  # Use half the fuel
        return distance_driven

class CrazyTaxi(Taxi):
    """A class representing a Crazy Taxi."""

    def get_fare(self):
        """Return a random fare."""
        return randint(10, 100)
