from decorators.registration import registration
from cart.shopping import ShoppingCart
@registration
def start_shopping(name, email, phone):
    print("You can now add products to your cart!")
start_shopping("Divya","divya@gmail.com",9492287323)
cart = ShoppingCart()
cart.add_to_cart(1)
cart.add_to_cart(3)
cart.add_to_cart(5)
cart.show_cart()