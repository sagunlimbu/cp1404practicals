"""Program to interactively get a valid score, print result, show stars, or quit."""

import random
from score import get_result

def get_valid_score():
    """Prompts the user for a valid score (0-100 inclusive)."""
    while True:
        try:
            score = float(input("Enter a score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100 inclusive. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_result(score):
    """Prints the result for the given score."""
    result = get_result(score)
    print("Result:", result)

def show_stars(score):
    """Prints stars corresponding to the given score."""
    print("Stars:", '*' * int(score))

def main():
    """Orchestrates the main part of the program."""
    print("Welcome to the Score Program!")

    # Get a valid score
    score = get_valid_score()

    # Menu loop
    while True:
        print("\nMENU:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Thank you for using the Score Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
