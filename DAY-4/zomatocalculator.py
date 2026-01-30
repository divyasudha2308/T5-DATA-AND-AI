
try:
    print(" Welcome to Zomato Order Calculator") 
    items = int(input("How many items do you want to order? "))
    if items <= 0:
        raise ValueError("You cannot order 0 or negative items.")
    price_per_item = 150

    total_amount = items * price_per_item

except ValueError as ve:
    print(" Invalid input:", ve)

except Exception as e:
    print("Something went wrong:", e)

else:
    
    print("Order placed successfully!")
    print("Number of items:", items)
    print("Total bill amount: ₹", total_amount)

finally:
   
    print(" Thank you for using Zomato!")
