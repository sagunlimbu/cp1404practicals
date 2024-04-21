import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A representation of an unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if the random number is less than reliability."""
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
