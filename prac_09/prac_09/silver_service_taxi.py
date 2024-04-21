from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A class representing a Silver Service Taxi."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness


    def get_fare(self):
        """Return the total fare for the taxi trip."""
        return round(super().get_fare() + self.flagfall, 1)

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
