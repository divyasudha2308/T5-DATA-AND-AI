# def my_decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello")

# greet()



# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("before function")
#         res=func(*args,**kwargs)
#         print("after function")
#         return res
#     return wrapper

# @decorator
# def add(a,b):
#     return a+b
# print(add(3,5))

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def greet():
#     print("HI")
# greet()


# class Mathutils:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(Mathutils.add(23,10))
# obj=Mathutils()
# print(obj.add(10,20))

# class student:
#     school_name="DAV High School"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     @classmethod
#     def change_school_name(cls,new_name):
#         cls.school_name=new_name

# print("before change:",student.school_name)
# student.change_school_name("cmrcet")
# print("after change:",student.school_name)

# def designation_decorator(func):
#     def wrapper(desg, sal):
#         print("Designation:", desg)
#         func(desg, sal)   
#     return wrapper


# def salary_decorator(func):
#     def wrapper(desg, sal):
#         func(desg, sal)   
#         print("Salary:", sal)
#     return wrapper


# @salary_decorator
# @designation_decorator
# def employee_details(desg, sal):
#     print("Employee details displayed")


# employee_details("product engineer",80000)

class Person:
    def __init__(self, name):
        self.name = name   

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:  
            raise ValueError("Name cannot be empty")
        self._name = value



p = Person("divya")
print(p.name)




    
