import csv

with open("report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Divya", 20, "Hyderabad"])
    writer.writerow(["Aditri", 24, "Delhi"])
    writer.writerow(["varshitha",21,"pune"])

print("CSV report created")
