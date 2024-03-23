"""
CP1404 - Practical 7
Name: <SAGUN LIMBU>
"""

from guitar import Guitar

def load_guitars(filename):
    """Read guitars from a file and store them in a list."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    """Display details of guitars in a list."""
    for index, guitar in enumerate(guitars, 1):
        print(f"Guitar {index}: {guitar}")

def sort_guitars_by_year(guitars):
    """Sort guitars in a list by year."""
    guitars.sort(key=lambda x: x.year)

def main():
    """Main function."""
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("List of guitars:")
    display_guitars(guitars)

    print("\nSorted list of guitars by year:")
    sort_guitars_by_year(guitars)
    display_guitars(guitars)

if __name__ == "__main__":
    main()
