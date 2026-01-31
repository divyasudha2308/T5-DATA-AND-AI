class Employee:

    def __init__(self, name, emp_id, age, salary):
        self.name = name
        self.emp_id = emp_id
        self.age = age
        self.salary = salary

    def display(self, *args):
        if len(args) == 0:
            print(f"Name: {self.name}, ID: {self.emp_id}, Age: {self.age}, Salary: {self.salary}")
        elif len(args) == 1:
            print(f"Name: {self.name}")
        elif len(args) == 2:
            print(f"Name: {self.name}, Age: {self.age}")
        elif len(args) == 3:
            print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
        else:
            print("Invalid")


name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
emp_id = int(input("Enter employee ID: "))

e1 = Employee(name, emp_id, age, salary)

e1.display()
e1.display(1)
e1.display(1, 2)
e1.display(1, 2, 3)
