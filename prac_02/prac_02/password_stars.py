"""Program to check password length and print asterisks accordingly."""

def main():
    """Orchestrates the main part of the program."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Prompts the user to enter a password and checks its length."""
    while True:
        password = input("Enter your password: ")
        if len(password) < 1:
            print("Password cannot be empty. Please try again.")
        else:
            return password

def print_asterisks(password):
    """Prints asterisks corresponding to the length of the password."""
    print('*' * len(password))

if __name__ == "__main__":
    main()
