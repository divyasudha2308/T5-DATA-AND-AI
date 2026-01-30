

from users import register_user, login_user, is_new_user
from services import show_services
from drivers import register_drivers, drivers
from booking import book_ride
from invoice import generate_invoice

locations = ["Chennai", "Pondicherry", "Bangalore"]

register_drivers("Ravi", "Suresh", "Mahesh", "Kiran")

print("--- Welcome to Uber Application ---")
name = input("Enter your name: ")
phone = input("Enter your phone number: ")

if is_new_user(name, phone):
    print("New user detected. Registering...")
    register_user(name, phone)

current_user = login_user(name)
if not current_user:
    print("Error: User not found!")
    exit()

while True:
    print("\n--- MAIN MENU ---")
    print("1. Book Trip")
    print("2. View My Trips")
    print("3. View Drivers Info")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("\nAvailable Locations:")
        for i, loc in enumerate(locations, start=1):
            print(f"{i}. {loc}")

        src_num = int(input("Choose source number: "))
        dest_num = int(input("Choose destination number: "))
        source = locations[src_num-1]
        destination = locations[dest_num-1]

        show_services()
        vehicle_num = int(input("Choose vehicle number: "))
        vehicle = sorted({"Bike", "Auto", "Car"})[vehicle_num-1]

        trip = book_ride(current_user, source=source, destination=destination, vehicle=vehicle)
        if trip:
            print(f"\nDriver Assigned: {trip['driver']}")
            print(f"Vehicle: {trip['vehicle']}")
            print(f"Destination: {trip['destination']}")
            print(f"Fare: ₹{trip['fare']}")

            
            generate_invoice(trip)

    elif choice == "2":
        print(f"\n--- {current_user['name']}'s Trip History ---")
        if current_user['trips']:
            for t in current_user['trips']:
                print("  ", t)
        else:
            print("  No trips yet")

    elif choice == "3":
        print("\n--- Drivers Information ---")
        for d in drivers:
            print(f"Driver: {d['name']}, Status: {d['status']}, Trips: {len(d['trips'])}")

    elif choice == "4":
        print("Thank you for using Uber ")
        break

    else:
        print("Invalid choice! Try again.")
