"""
CP1404 - Practical 6
Name: <SAGUN LIMBU>
"""


class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
