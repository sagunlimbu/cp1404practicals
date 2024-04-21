from prac_09.unreliable_car import UnreliableCar

def main():
    my_car = UnreliableCar("Unreliable Car", 100, 50)  # 50% reliability

    # Test driving the unreliable car multiple times
    for i in range(5):
        distance = 10  # Distance to drive
        distance_driven = my_car.drive(distance)
        if distance_driven == 0:
            print(f"Attempt {i+1}: Failed to drive due to unreliability")
        else:
            print(f"Attempt {i+1}: Successfully drove {distance_driven} km")

if __name__ == "__main__":
    main()
