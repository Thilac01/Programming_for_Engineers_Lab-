# Initialize empty shopping cart as a list
shopping_cart = []

# Initialize product prices as a dictionary
product_prices = {
    "apple": 50,
    "banana": 30,
    "orange": 40,
    "grapes": 90,
    "mango": 70
}

# Function to add item to the cart
def add_item_to_cart(product):
    """
    Add a new item to the cart if the item exists in the product_prices list
    """
    product = product.lower()
    if product in product_prices:
        shopping_cart.append(product)
        print(f"{product.capitalize()} added to your cart.")
    else:
        print(f"Sorry, {product} is not available.")

# Function to remove an item from the cart
def remove_item_from_cart(product):
    """
    Remove an item from the cart if it exists in the cart
    """
    product = product.lower()
    if product in shopping_cart:
        shopping_cart.remove(product)
        print(f"{product.capitalize()} removed from your cart.")
    else:
        print(f"{product.capitalize()} is not in the cart.")

# Function to view all items in the cart
def view_cart():
    """
    Display all items currently in the shopping cart
    """
    if shopping_cart:
        print("Items in your cart:")
        for item in shopping_cart:
            print(f"- {item.capitalize()}: ${product_prices[item]}")
    else:
        print("Your cart is empty.")

# Function to checkout and calculate the total price
def checkout():
    """
    Calculate and display the total price of all items in the shopping cart
    """
    if shopping_cart:
        total = sum([product_prices[item] for item in shopping_cart])
        print(f"Total price: ${total}")
    else:
        print("Your cart is empty. Add some items first.")

# Function to add a new product to the product price list
def add_product(product, price):
    """
    Add a new product to the product_price list.
    """
    product = product.lower()
    if product not in product_prices:
        product_prices[product] = price
        print(f"{product.capitalize()} added with a price of ${price}.")
    else:
        print(f"{product.capitalize()} is already in the price list.")

# Function to get unique items in the cart
def get_unique_items(cart):
    """
    Get unique items in the shopping cart.
    """
    unique_items = set(cart)
    if unique_items:
        print("Unique items in your cart:")
        for item in unique_items:
            print(f"- {item.capitalize()}")
    else:
        print("Your cart is empty.")

# Main program loop to simulate the shopping experience
def shopping_program():
    while True:
        print("\nAvailable Products:")
        for product, price in product_prices.items():
            print(f"- {product.capitalize()} ${price}")
        
        print("""
What would you like to do?
1. Add item to cart
2. Remove item from cart
3. View cart
4. Checkout
5. Add a new product to the price list
6. Get unique items in cart
7. Exit
        """)
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            product = input("Enter the item you want to add: ")
            add_item_to_cart(product)
        elif choice == '2':
            product = input("Enter the item you want to remove: ")
            remove_item_from_cart(product)
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            product = input("Enter the new product name: ")
            price = float(input(f"Enter the price for {product}: "))
            add_product(product, price)
        elif choice == '6':
            get_unique_items(shopping_cart)
        elif choice == '7':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

shopping_program()
