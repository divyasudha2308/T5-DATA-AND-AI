def travel_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

def bill_calculator(*args):
    total = 0
    for amount in args:
        total += amount
    return total

