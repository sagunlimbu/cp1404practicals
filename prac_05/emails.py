"""
CP1404 - Practical 5
Name: <SAGUN LIMBU>
"""
"""
Email to Name Program
"""


def extract_name_from_email(email):
    """Extract a potential name from the given email address."""
    parts = email.split('@')[0]  # Split the email at '@' and take the first part
    possible_name = parts.split('.')  # Split the part before '@' by '.'
    possible_name = [name.title() for name in possible_name]  # Capitalize the first letter of each part
    return ' '.join(possible_name)


def main():
    emails_to_names = {}

    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()

        if confirmation not in ('y', 'yes', ''):
            name = input("Name: ").title()  # Ask for the name if the confirmation is anything but 'yes' or blank

        emails_to_names[email] = name
        email = input("Email: ")

    print()
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
