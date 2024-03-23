"""
CP1404 - Practical 7
Name: <SAGUN LIMBU>
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, name of the guitar (default "")
        year: int, year the guitar was made (default 0)
        cost: float, cost of the guitar (default 0.0)
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"
