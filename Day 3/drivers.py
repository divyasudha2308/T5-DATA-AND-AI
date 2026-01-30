

drivers = []

def register_drivers(*names):
    for name in names:
        drivers.append({
            "name": name,
            "trips": [],
            "status": "Available"
        })

def assign_driver():
    available = [d for d in drivers if d["status"] == "Available"]
    if not available:
        return None
    driver = sorted(available, key=lambda d: len(d['trips']))[0]
    driver["status"] = "Booked"
    return driver

def update_driver_status(driver_name, status):
    for d in drivers:
        if d["name"] == driver_name:
            d["status"] = status
            return True
    return False
