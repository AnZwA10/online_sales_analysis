# Online Sales Analysis

A Python project that manages the products of an online store and a customer's shopping cart.

## Classes

- **Product** (`product.py`): stores name, price and quantity. Methods: `display_info()` and `update_quantity()`.
- **ProductManager** (`product_manager.py`): keeps the list of available products. Methods: `add_product()`, `display_products()`, `total_value()` and `remove_product()`.
- **Cart** (`cart.py`): keeps the products in the customer's cart. Methods: `add_product()`, `total_price()` and `display_cart()`.

## Usage

Run `python main.py` to create products, add 3 random ones to the cart and display the total to pay.

## Git workflow

- `add-product-removal`: added product removal by name.
- `add-cart-functionality`: added the Cart class.
- `config.json` and screenshots are ignored through `.gitignore`.
