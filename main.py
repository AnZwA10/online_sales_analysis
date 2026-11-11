import random
from cart import Cart
from product import Product
from product_manager import ProductManager

manager = ProductManager()
manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Mouse", 80, 20))
manager.add_product(Product("Keyboard", 150, 10))
manager.add_product(Product("Monitor", 900, 7))

manager.display_products()
print(f"Total inventory value: {manager.total_value()} RON")

cart = Cart()
for product in random.sample(manager.products, 3):
    cart.add_product(product)

cart.display_cart()
print(f"Total to pay: {cart.total_price()} RON")
