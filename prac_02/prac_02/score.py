"""Program to determine the score result."""

import random

def main():
    """Orchestrates the main part of the program."""
    user_score = float(input("Enter your score: "))
    print("Result:", get_result(user_score))

    # Generate a random score and print the result
    random_score = random.uniform(0, 100)
    print("Random Score:", random_score)
    print("Result for Random Score:", get_result(random_score))

def get_result(score):
    """Returns the result based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
