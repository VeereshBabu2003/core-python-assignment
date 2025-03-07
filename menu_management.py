def add_item(menu, item):
    """Adds an item to the menu if not already present."""
    if item not in menu:
        menu.append(item)
    return menu

def remove_item(menu, item):
    """Removes an item if it exists, else returns a message."""
    if item in menu:
        menu.remove(item)
    else:
        return f"{item} is not in the menu."
    return menu

def check_item(menu, item):
    """Checks if an item is available in the menu."""
    return f"{item} is available" if item in menu else f"{item} is not available"

# Example Input
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
updated_menu = add_item(initial_menu, "Tacos")
updated_menu = remove_item(updated_menu, "Salad")
availability = check_item(updated_menu, "Pizza")

print("Updated Menu:", updated_menu)
print("Availability:", availability)
