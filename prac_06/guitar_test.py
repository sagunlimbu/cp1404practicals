"""
CP1404 - Practical 6
Name: <SAGUN LIMBU>
"""
from guitar import Guitar

def main():
    """Test the Guitar class methods."""
    # Create a guitar
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

    # Test get_age()
    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age(2022)}")
    print(f"Another Guitar get_age() - Expected 9. Got {guitar.get_age(2022)}")

    # Test is_vintage()
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage(2022)}")
    print(f"Another Guitar is_vintage() - Expected False. Got {guitar.is_vintage(2022)}")

if __name__ == "__main__":
    main()
