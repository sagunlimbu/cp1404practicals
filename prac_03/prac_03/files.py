# Task 1: Write user's name to a file
name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)

# Task 2: Read user's name from the file and print it
with open("name.txt", 'r') as file:
    name = file.read()
print("Your name is", name)

# Task 3: Add the first two numbers from numbers.txt
with open("numbers.txt", 'r') as file:
    numbers = file.readlines()

total = 0
for number in numbers[:2]:
    total += int(number.strip())

print("The total of the first two numbers is:", total)

# Task 4: Calculate the total for all numbers in numbers.txt
with open("numbers.txt", 'r') as file:
    numbers = file.readlines()

total = 0
for number in numbers:
    total += int(number.strip())

print("The total of all numbers is:", total)
