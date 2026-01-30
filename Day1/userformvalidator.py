email=input("enter the mail :")
password=input("enter the password:")
name=input("Enter name:")
age=input("enter age:")
if '@' not in email:
    print("invalid mail")
elif len(password)<6:
    print("password is short")
elif not name.isalpha() and len(name)>2:
    print("enter name in characters and greater than 2 letters")
elif not age.isdigit() and age>0:
    print("enter age in numbers and greater than 0")
else:
    print("form submitted succesfully")