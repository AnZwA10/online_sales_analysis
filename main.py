from product import Product
from product_manager import ProductManager

manager = ProductManager()
manager.add_product(Product("Gaming Laptop", 3500, 8))
manager.add_product(Product("Wireless Mouse", 80, 25))
manager.add_product(Product("Mechanical Keyboard", 150, 12))
manager.add_product(Product("Monitor 27 inch", 900, 7))

