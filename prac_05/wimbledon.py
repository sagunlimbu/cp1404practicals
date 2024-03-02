"""
CP1404 - Practical 5
Name: <SAGUN LIMBU>
"""
import csv


def read_wimbledon_data(filename):
    """Reads the Wimbledon data from a CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


def process_champions(data):
    """Processes the champions and their win counts."""
    champions = {}
    for row in data:
        name = row[1]
        champions[name] = champions.get(name, 0) + 1
    return champions


def process_countries(data):
    """Extracts and sorts the list of unique countries."""
    countries = {row[2] for row in data}  # Using a set to ensure uniqueness
    return sorted(countries)


def display_information(champions, countries):
    """Displays the processed information."""
    print("Champions and their win counts:")
    for champion, count in champions.items():
        print(f"{champion}: {count}")
    print("\nCountries of the champions in alphabetical order:")
    print(", ".join(countries))


def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champions = process_champions(data[1:])  # Exclude the header row
    countries = process_countries(data[1:])  # Exclude the header row
    display_information(champions, countries)


if __name__ == "__main__":
    main()
