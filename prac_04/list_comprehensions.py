"""
CP1404 - Practical 4
Name: <SAGUN LIMBU>
"""

# lowercase_full_names
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

# numbers
numbers = [int(num) for num in almost_numbers]
print(numbers)

# numbers greater than 9
numbers_greater_than_9 = [num for num in numbers if num > 9]
print(numbers_greater_than_9)

# last names longer than 11 characters
long_last_names = [name.split()[1] for name in full_names if len(name.split()[1]) > 11]
print(", ".join(long_last_names))
