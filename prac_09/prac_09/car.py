from random import randint


class Car:
    """A class to represent a Car."""

    def __init__(self, name, fuel):
        """Initialize a Car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of the Car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}km"

    def drive(self, distance):
        """Drive the car a given distance."""
        if distance <= self.fuel:
            self.odometer += distance
            self.fuel -= distance
        else:
            print("Not enough fuel to drive that far")
            distance = 0
        return distance


class GasGuzzler(Car):
    """A class representing a Gas Guzzler car."""

    def __init__(self, name, fuel, fuel_efficiency_factor):
        super().__init__(name, fuel)
        self.fuel_efficiency_factor = fuel_efficiency_factor

    def drive(self, distance):
        """Drive the car a given distance."""
        distance_driven = super().drive(distance)
        self.fuel -= distance_driven * self.fuel_efficiency_factor
        return distance_driven


class Bomb(Car):
    """A class representing a Bomb car."""

    def drive(self, distance):
        """Drive the car a given distance."""
        self.fuel -= distance
        return 0
