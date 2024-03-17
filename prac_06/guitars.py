"""
CP1404 - Practical 6
Name: <SAGUN LIMBU>
"""
from guitar import Guitar


def main():
    """Create a program that uses the Guitar class."""
    print("My guitars!")
    guitars = []

    # Uncomment these lines for manual input
    # while True:
    #     name = input("Name: ")
    #     if not name:
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitars.append(Guitar(name, year, cost))

    # Test data for efficiency
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars added yet.")


if __name__ == "__main__":
    main()
