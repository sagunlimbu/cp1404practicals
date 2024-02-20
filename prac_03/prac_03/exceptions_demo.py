"""
Questions
1. When will a ValueError occur?
   - A ValueError will occur if the user enters a value that cannot be converted to an integer, such as a string or a floating-point number.

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError will occur if the user enters 0 as the input because division by zero is not allowed.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, we can add a condition to check if the user input is 0 and prompt the user to enter a non-zero value.

4. If you could figure out the answer to question 3, then make this change now.
"""

finished = False
result = 0
while not finished:
    try:
        number = int(input("Enter a valid non-zero integer: "))
        if number == 0:
            print("Please enter a non-zero integer.")
        else:
            result = 10 / number
            finished = True
    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", result)
