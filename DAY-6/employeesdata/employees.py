import csv

def get_employee_details():
    search_name = input("Enter employee name to search: ")
    found = False

    with open("employees.csv", mode="r") as file:
        csvFile = csv.reader(file)
        next(csvFile)  

        for row in csvFile:
            if search_name.lower() == row[1].lower():
                print("\nEmployee Details Found\n")
                print("ID:", row[0])
                print("Name:", row[1])
                print("City:", row[2])
                print("Designation:", row[3])
                print("Salary:", row[4])
                found = True
                break

    if not found:
        print("\nEmployee not found")
