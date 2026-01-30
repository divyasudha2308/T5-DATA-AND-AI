

from drivers import assign_driver, update_driver_status
from services import calculate_fare, is_valid_service

STATUS_FLOW = ["Waiting", "Booked", "Trip Completed"]

def book_ride(user, **kwargs):
    source = kwargs.get("source")
    destination = kwargs.get("destination")
    vehicle = kwargs.get("vehicle")

    if not is_valid_service(vehicle):
        print("Invalid vehicle selected!")
        return None

    driver = assign_driver()
    if not driver:
        print("No driver available!")
        return None

    fare = calculate_fare(vehicle, source, destination)
    if fare is None:
        print("Route not available!")
        return None

    trip = {
        "user": user["name"],
        "phone": user["phone"],
        "driver": driver["name"],
        "vehicle": vehicle.title(),
        "source": source,
        "destination": destination,
        "fare": fare,
        "status": STATUS_FLOW.copy(),
        "feedback": None
    }

    driver['trips'].append(f"{vehicle.title()} → {destination} | ₹{fare}")
    user['trips'].append(f"{vehicle.title()} → {destination} | ₹{fare}")

    return trip
