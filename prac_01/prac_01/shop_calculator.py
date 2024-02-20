def main():
    # Initialize variables
    total_price = 0

    # Get the number of items
    while True:
        try:
            num_items = int(input("Number of items: "))
            if num_items >= 0:
                break
            else:
                print("Invalid number of items!")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    # Calculate total price
    for i in range(num_items):
        while True:
            try:
                item_price = float(input(f"Price of item {i + 1}: $"))
                if item_price >= 0:
                    break
                else:
                    print("Invalid price! Please enter a valid positive number.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        total_price += item_price

    # Apply discount if total price is over $100
    if total_price > 100:
        discount = total_price * 0.10
        total_price -= discount

    # Display the result
    print(f"Total price for {num_items} items is ${total_price:.2f}")


if __name__ == "__main__":
    main()
