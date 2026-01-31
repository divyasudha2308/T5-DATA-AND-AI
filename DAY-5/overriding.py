class Employee:

    def __init__(self, name, emp_id, age, salary):
        self.name = name
        self.emp_id = emp_id
        self.age = age
        self.salary = salary

    def display(self, *args):
        if len(args) == 0:
            print(f"Employee → Name: {self.name}, ID: {self.emp_id}, Age: {self.age}, Salary: {self.salary}")
        elif len(args) == 1:
            print(f"Employee → Name: {self.name}")
        elif len(args) == 2:
            print(f"Employee → Name: {self.name}, Age: {self.age}")
        else:
            print("Employee → Invalid")


class Manager(Employee):

    def __init__(self, name, emp_id, age, salary, dept):
        super().__init__(name, emp_id, age, salary)
        self.dept = dept

    def display(self, *args):
        if len(args) == 0:
            print(f"Manager → Name: {self.name}, ID: {self.emp_id}, Age: {self.age}, Salary: {self.salary}, Dept: {self.dept}")
        elif len(args) == 1:
            print(f"Manager → Name: {self.name}, Salary: {self.salary}, Dept: {self.dept}")
        elif len(args) == 2:
            print(f"Manager → Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Dept: {self.dept}")
        else:
            print("Manager → Invalid")


name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
emp_id = int(input("Enter employee ID: "))
dept = input("Enter department: ")

e = Employee(name, emp_id, age, salary)
m = Manager(name, emp_id, age, salary, dept)

e.display()
e.display(1)
e.display(1, 2)

m.display()
m.display(1)
m.display(1, 2)
