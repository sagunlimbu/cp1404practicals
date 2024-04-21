from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    print("Let's drive!")
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "q":
            break
        elif choice == "c":
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${bill_to_date:.2f}")
            else:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                fare = current_taxi.drive(distance)
                bill_to_date += fare
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                print(f"Bill to date: ${bill_to_date:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()
