"""Program to convert temperature between Celsius and Fahrenheit."""


def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Example usage:
# Get user input
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

# Convert temperatures
fahrenheit_result = celsius_to_fahrenheit(celsius_input)
celsius_result = fahrenheit_to_celsius(fahrenheit_input)

# Output results
print(f"{celsius_input} degrees Celsius is equal to {fahrenheit_result:.2f} degrees Fahrenheit.")
print(f"{fahrenheit_input} degrees Fahrenheit is equal to {celsius_result:.2f} degrees Celsius.")
