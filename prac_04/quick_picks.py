"""
CP1404 - Practical 4
Name: <SAGUN LIMBU>
"""

import random

NUM_QUICK_PICKS = 5
NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_pick():
    """Generate a single quick pick line."""
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_LINE))

def display_quick_picks(quick_picks):
    """Display quick picks."""
    for quick_pick in quick_picks:
        print(" ".join(f"{number:2}" for number in quick_pick))

def main():
    num_quick_picks = int(input("How many quick picks? "))
    quick_picks = [generate_quick_pick() for _ in range(num_quick_picks)]
    display_quick_picks(quick_picks)

if __name__ == "__main__":
    main()
