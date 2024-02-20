def calculate_bonus(sales):
    if sales < 1000:
        bonus_percentage = 0.10
    else:
        bonus_percentage = 0.15

    bonus = sales * bonus_percentage
    return bonus


def main():
    while True:
        sales = float(input("Enter sales: $"))

        if sales < 0:
            break

        bonus = calculate_bonus(sales)
        print(f"Bonus: ${bonus:.2f}")


if __name__ == "__main__":
    main()
