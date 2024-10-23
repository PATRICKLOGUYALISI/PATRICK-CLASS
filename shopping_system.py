class Product:
    
    
    
    
    
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        print(f"Product: {self.product_name}, Price: {self.price}, Quantity in stock: {self.quantity_in_stock}")

class ShoppingCart:
    total_carts = 0
    
    
    
    

    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Not enough stock for {product.product_name}.")

    def remove_from_cart(self, product):
        
        
        
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                print(f"Removed {product.product_name} from the cart.")
                return
        print(f"{product.product_name} not found in the cart.")

    def display_cart(self):
        if not self.items:
            print("The cart is empty.")
        else:
            for product, quantity in self.items:
                print(f"Product: {product.product_name}, Quantity: {quantity}")

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total


product1 = Product("Bags", 1000, 5)
product2 = Product("Suits", 500, 10)
product3 = Product("Shirts", 100, 15)


cart1 = ShoppingCart()
cart2 = ShoppingCart()


cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 1)
cart1.display_cart()
print(f"Total amount due for cart1: {cart1.calculate_total()}")


cart2.add_to_cart(product3, 5)
cart2.add_to_cart(product2, 2)
cart2.remove_from_cart(product2)
cart2.display_cart()
print(f"Total amount due for cart2: {cart2.calculate_total()}")
