def calculate_total(cart_items):
    """Calculates the total price of items in the cart, applying a discount if necessary."""
    if not cart_items:
        return "Cart is empty. Total Price: $0"

    total_price = sum(cart_items.values())

    if len(cart_items) > 5:
        total_price *= 0.9  # Apply 10% discount

    return f"Total Price: ${total_price:.2f}"

# Example Input
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(calculate_total(cart_items))
