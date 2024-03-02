"""
CP1404 - Practical 5
Name: <SAGUN LIMBU>
"""
"""
Hex Colours Lookup
Estimate: 15 minutes
Actual:   [to be filled out after completion]
"""

COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff",
    # Add more colours as needed
}

print("Enter a colour name to get its hexadecimal code. Enter a blank to stop.")

while True:
    colour_name = input("Colour Name: ").strip()
    if not colour_name:  # Exit loop if input is blank
        break
    colour_name_formatted = colour_name.capitalize()  # Adjust if your dictionary keys vary in case sensitivity

    # Attempt to retrieve and print the hexadecimal code
    try:
        hex_code = COLOUR_TO_HEX[colour_name_formatted]
        print(f"The hexadecimal code for {colour_name_formatted} is {hex_code}.")
    except KeyError:
        print("Invalid colour name.")

# Fill in the actual time spent here after completion
