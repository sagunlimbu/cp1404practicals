class Band:
    """A class to represent a musical band."""

    def __init__(self, name):
        """Initialize a Band instance."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of the Band."""
        members_info = ", ".join([str(member) for member in self.members])
        return f"{self.name} ({members_info})"

    def add_musician(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def play(self):
        """Make the band play."""
        for member in self.members:
            if member.instrument:
                print(f"{member.name} is playing: {member.instrument}")
            else:
                print(f"{member.name} needs an instrument!")
