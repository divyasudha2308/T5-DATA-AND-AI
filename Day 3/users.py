

users = []

def register_user(name, phone):
    if any(u["phone"] == phone for u in users):
        print("User already registered!")
        return False
    users.append({
        "name": name,
        "phone": phone,
        "trips": []
    })
    print(f"User {name} registered successfully!")
    return True

def is_new_user(name, phone):
    return all(u["name"] != name and u["phone"] != phone for u in users)

def login_user(name):
    for u in users:
        if u["name"] == name:
            print(f"Welcome back {u['name']}!")
            return u
    print("User not found!")
    return None
