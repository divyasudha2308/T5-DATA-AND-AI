
is_logged_in = True


def login_required(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Access denied  Please login first")
    return wrapper



@login_required
def dashboard():
    print("Welcome to Dashboard ")


dashboard()
