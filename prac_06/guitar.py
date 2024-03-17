"""
CP1404 - Practical 6
Name: <SAGUN LIMBU>
"""
class Guitar:
    """Represents a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return the age of the guitar in years."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Check if the guitar is vintage."""
        return self.get_age(current_year) >= 50
