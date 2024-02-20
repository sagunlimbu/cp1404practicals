def main():
    # Get user's name
    name = input("Enter name: ")

    choice = ""
    while choice.upper() != "Q":
        # Display menu
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")

        # Get user's choice
        choice = input(">>> ").upper()

        # Process user's choice
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        elif choice != "Q":
            print("Invalid choice")

    print("Finished.")


if __name__ == "__main__":
    main()
