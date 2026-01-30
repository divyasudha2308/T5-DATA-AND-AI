
import os
import time
from drivers import update_driver_status

def generate_invoice(trip):
    invoices_folder = "invoices"
    if not os.path.exists(invoices_folder):
        os.makedirs(invoices_folder)

    filepath = os.path.join(invoices_folder, "invoice.txt")

    print("\n--- Trip Status ---")
    for i, status in enumerate(trip['status']):
        trip['status'][i] = status
        print(f"Status: {status}")
        time.sleep(2)  

    
    update_driver_status(trip['driver'], "Available")

   
    feedback_text = input("Please provide feedback for your trip: ")
    trip['feedback'] = feedback_text

    text = f"""
--- UBER TRIP INVOICE ---

User       : {trip['user']}
Phone      : {trip['phone']}
Driver     : {trip['driver']}
Vehicle    : {trip['vehicle']}
Source     : {trip['source']}
Destination: {trip['destination']}
Fare       : ₹ {trip['fare']}
Status     : {trip['status'][-1]}
Feedback   : {trip['feedback']}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"\n🧾 Invoice generated: {filepath}")
    print(f"Fare: ₹{trip['fare']}")
