from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Hummer", 200, 2)  # Fanciness of 2

    # Test driving the Silver Service Taxi
    distance = 18  # Distance to drive
    fare = my_taxi.get_fare()
    print(f"For a {my_taxi.name} with fanciness of 2, the fare for a {distance} km trip is ${fare:.2f}")


if __name__ == "__main__":
    main()
