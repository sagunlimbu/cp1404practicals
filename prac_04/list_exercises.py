"""
CP1404 - Practical 4
Name: <SAGUN LIMBU>
"""

def main():
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


if __name__ == "__main__":
    main()

# List of usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask for user's username
username = input("Enter your username: ")

# Check if the username is in the list of authorised users
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
