"""
CP1404 - Practical 7
Name: <SAGUN LIMBU>
"""

import datetime

class Project:
    """Represent a project object."""

    def __init__(self, name="", start_date=None, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialize a Project instance.

        name: string, name of the project (default "")
        start_date: datetime.date object, start date of the project (default None)
        priority: int, priority of the project (default 0)
        cost_estimate: float, cost estimate of the project (default 0.0)
        completion_percentage: int, completion percentage of the project (default 0)
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of a Project."""
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

    def update_completion_percentage(self, new_percentage):
        """Update the completion percentage of the project."""
        self.completion_percentage = new_percentage

    def update_priority(self, new_priority):
        """Update the priority of the project."""
        self.priority = new_priority

    def is_incomplete(self):
        """Check if the project is incomplete."""
        return self.completion_percentage < 100

    def is_started_after_date(self, date):
        """Check if the project is started after a given date."""
        return self.start_date > date

    @staticmethod
    def parse_date(date_string):
        """Parse a date string in the format dd/mm/yyyy into a datetime.date object."""
        return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
