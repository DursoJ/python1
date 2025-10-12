# Simple Inventory Management System

# The inventory will be stored as a list of dictionaries
inventory = []

# Function to add a new item
def add_item():
    name = input("Enter item name: ").strip()
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ").strip()

    # Check if item already exists — update instead of adding duplicate
    for item in inventory:
        if item["name"].lower() == name.lower():
            print("Item already exists. Use 'Update Item' instead.")
            return

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }
    inventory.append(item)
    print(f"{name} added to inventory.")


# Function to update an existing item
def update_item():
    name = input("Enter the name of the item to update: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():
            print(f"Current details: {item}")
            item["price"] = float(input("Enter new price: "))
            item["quantity"] = int(input("Enter new quantity: "))
            item["category"] = input("Enter new category: ").strip()
            print(f"{name} has been updated.")
            return
    print("Item not found.")


# Function to view all inventory items
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n=== Inventory List ===")
    for item in inventory:
        print(f"Name: {item['name']}, Price: ${item['price']:.2f}, Quantity: {item['quantity']}, Category: {item['category']}")
    print("======================\n")


# Function to remove an item by name
def remove_item():
    name = input("Enter the name of the item to remove: ").strip()
    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"{name} has been removed from inventory.")
            return
    print("Item not found.")


# Function to search items by category
def search_by_category():
    category = input("Enter category to search: ").strip().lower()
    found_items = [item for item in inventory if item["category"].lower() == category]

    if not found_items:
        print("No items found in that category.")
    else:
        print(f"\nItems in category '{category}':")
        for item in found_items:
            print(f"- {item['name']} (${item['price']:.2f}, Qty: {item['quantity']})")
        print()


# Main program loop
def main():
    while True:
        print("""
========= Inventory Management System =========
1. Add Item
2. Update Item
3. View Inventory
4. Remove Item
5. Search by Category
6. Exit
===============================================
""")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            search_by_category()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
