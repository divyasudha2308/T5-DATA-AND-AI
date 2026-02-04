from decorators.access import registration, login
from employee.access import show_employee
@registration
def register(name,email,phone,designation,salary):
    show_employee(name,email,phone,designation,salary)
@login
def user_login(username,login_status):
    print("Accessing Dashboard...")
register("Divya","divya@gmail.com",9492287323,"product Manager",85000)
user_login("Divya",True)