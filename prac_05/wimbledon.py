"""
CP1404 - Practical 5
Name: <SAGUN LIMBU>
"""
import csv

def read_data(filename):
    """
    Read data from the CSV file and return a list of lists containing the information.
    """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next
        data = [row for row in reader]
    return data

def find_champions(data):
    """
    Find the champions and count how many times they have won.
    """
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions

def find_countries(data):
    """
    Find the countries of the champions in alphabetical order.
    """
    countries = {row[1] for row in data}
    return sorted(countries)

def main():
    filename = "wimbledon.csv"
    data = read_data(filename)

    champions = find_champions(data)
    countries = find_countries(data)

    print("Wimbledon Champions:")
    for champion, count in sorted(champions.items()):
        print(f"{champion} {count}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))

if __name__ == "__main__":
    main()
