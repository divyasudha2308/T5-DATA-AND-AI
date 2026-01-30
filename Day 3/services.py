

UBER_SERVICES = {"Bike", "Auto", "Car"}
RATE_PER_KM = {"Bike": 10, "Auto": 15, "Car": 20}
DISTANCES = {
    ("Pondicherry", "Chennai"): 150,
    ("Pondicherry", "Bangalore"): 310,
    ("Chennai", "Bangalore"): 350
}

def show_services():
    print("\nAvailable Vehicles:")
    for i, s in enumerate(sorted(UBER_SERVICES), start=1):
        print(f"{i}. {s}")

def is_valid_service(vehicle):
    return vehicle.title() in UBER_SERVICES

def calculate_fare(vehicle, source, destination):
    vehicle = vehicle.title()
    distance = DISTANCES.get((source, destination)) or DISTANCES.get((destination, source))
    if not distance:
        return None
    return distance * RATE_PER_KM[vehicle]
