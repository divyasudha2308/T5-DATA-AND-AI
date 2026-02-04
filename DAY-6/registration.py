def validate_registration(func):
    def wrapper(name, email, phone):

        if name == "":
            print("Invalid Name")
            return

        if "@" not in email:
            print("Invalid Email")
            return

        if len(str(phone)) != 10:
            print("Invalid Phone Number")
            return

        print("Validation Successful")
        func(name, email, phone)

    return wrapper


@validate_registration
def register_user(name, email, phone):
    print("Registration Successful!")
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
register_user("divya","chinnu@gmail.com",1234567890)