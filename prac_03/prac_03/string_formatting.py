"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

# Example variables
name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# Examples of different string formatting methods
print("My guitar: " + name + ", first made in " + str(year))  # Manual string concatenation
print("My guitar: {}, first made in {}".format(name, year))  # Using str.format()
print("My guitar: {0}, first made in {1}".format(name, year))  # Using str.format() with positional arguments
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))  # Formatting with str.format() and index
print(f"My {name} was first made in {year} (that's right, {year}!)")  # Using f-string formatting

# Formatting currency (grouping with comma, 2 decimal places)
print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")

# Aligning columns by using width after the :
numbers = [1, 19, 123, 456, -25]
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# Output using f-string formatting
print(f"{year} {name} for about ${cost:,.0f}!")

# Output using a for loop with range function and string formatting
for i in range(0, 201, 50):
    print(f"{i:3}")
