from functions import travel_profile, bill_calculator

name = input("Enter name: ").strip()
email = input("Enter email: ").strip()
phone = input("Enter phone number: ").strip()
age = input("Enter age: ").strip()
place = input("Enter travel location: ").strip()
days = input("Enter number of trip days: ").strip()

food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))
restaurant = float(input("Enter restaurant expense: "))
stay = float(input("Enter stay expense: "))

masked_phone = phone[:2] + "******" + phone[-2:]

user_profile = travel_profile(
    name=name,
    email=email,
    phone=masked_phone,
    age=age,
    location=place,
    trip_days=days
)

total_bill = bill_calculator(food, travel, restaurant, stay)

print("\nTraveller Profile")
for key, value in user_profile.items():
    print(f"{key}: {value}")

print(f"\nTotal Expenditure: ₹{total_bill}")
