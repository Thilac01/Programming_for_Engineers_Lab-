# Initialize an empty shopping cart as a list
shopping_cart = []

# Initialize product prices as a dictionary
product_prices = {
    "apple": 50,
    "banana": 30,
    "orange": 40,
    "grapes": 90,
    "mango": 70
}

# Function to add an item to the cart
def add_item_to_cart():
    product = input("Enter the item you want to add: ").lower()
    if product in product_prices:
        shopping_cart.append(product)
        print(product.capitalize() + " added to your cart.")
    else:
        print("Sorry, " + product + " is not available.")

# Function to remove an item from the cart
def remove_item_from_cart():
    product = input("Enter the item you want to remove: ").lower()
    if product in shopping_cart:
        shopping_cart.remove(product)
        print(product.capitalize() + " removed from your cart.")
    else:
        print(product.capitalize() + " is not in the cart.")

# Function to view all items in the cart
def view_cart():
    if shopping_cart:
        print("Items in your cart:")
        for item in shopping_cart:
            print(item.capitalize() + ": $" + str(product_prices[item]))
    else:
        print("Your cart is empty.")

# Function to checkout and calculate the total price
def checkout():
    if shopping_cart:
        total = 0
        for item in shopping_cart:
            total += product_prices[item]
        print("Total price: $" + str(total))
    else:
        print("Your cart is empty.")

# Function to add a new product to the price list
def add_product():
    product = input("Enter the new product name: ").lower()
    price = int(input("Enter the price for " + product + ": "))
    if product not in product_prices:
        product_prices[product] = price
        print(product.capitalize() + " added with a price of $" + str(price) + ".")
    else:
        print(product.capitalize() + " is already in the price list.")

# Function to display unique items in the cart
def get_unique_items():
    unique_items = []
    for item in shopping_cart:
        if item not in unique_items:
            unique_items.append(item)
    if unique_items:
        print("Unique items in your cart:")
        for item in unique_items:
            print(item.capitalize())
    else:
        print("Your cart is empty.")

# Main program loop
while True:
    print("\nAvailable Products:")
    for product in product_prices:
        print(product.capitalize() + " $" + str(product_prices[product]))
    
    print("\nWhat would you like to do?")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Add a new product to the price list")
    print("6. Get unique items in cart")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        add_item_to_cart()
    elif choice == '2':
        remove_item_from_cart()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        checkout()
    elif choice == '5':
        add_product()
    elif choice == '6':
        get_unique_items()
    elif choice == '7':
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please try again.")
