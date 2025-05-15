class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Transaction:
    def __init__(self, inventory):
        self.inventory = inventory
        self.selected_items = []

    def retrieve_items(self):
        print("\nItem Name\tPrice")
        for item in self.inventory:
            print(f"{item.name}\t${item.price}")

    def add_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.selected_items.append(item)
                return True
        return False

    def calculate_total(self):
        return sum(item.price for item in self.selected_items)

class Purchase(Transaction):
    def complete(self, reports):
        self.retrieve_items()
        while True:
            item_name = input("Which items would you like to buy? ").strip()
            if not self.add_item(item_name):
                print("Item not found. Please try again.")
            else:
                more = input("Anything else? (Y/N): ").strip().lower()
                if more != 'y':
                    break
        total = self.calculate_total()
        print(f"Your Total is ${total}.")
        print("Thank you for shopping at Target!\n")
        reports.append(total)

class Return(Transaction):
    def complete(self, reports):
        self.retrieve_items()
        while True:
            item_name = input("Which items would you like to return? ").strip()
            if not self.add_item(item_name):
                print("Item not found. Please try again.")
            else:
                more = input("Anything else? (Y/N): ").strip().lower()
                if more != 'y':
                    break
        total = self.calculate_total()
        print(f"Your Refund total is ${total}.")
        print("Thank you for shopping at Target!\n")
        reports.append(-total)  # Negative value for refund

class InventoryManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def display_inventory(self):
        print("\nThe following items are currently stored in the system:")
        print("Item Name\tPrice")
        for item in self.inventory:
            print(f"{item.name}\t${item.price}")

    def add_item(self):
        name = input("Item Name: ").strip()
        while True:
            try:
                price = float(input("Item Price: "))
                break
            except ValueError:
                print("Please enter a valid price.")
        self.inventory.append(Item(name, price))
        print("Added Successfully!!")

    def remove_item(self):
        name = input("Item Name to remove: ").strip()
        for item in self.inventory:
            if item.name.lower() == name.lower():
                self.inventory.remove(item)
                print("Item Removed Successfully")
                return
        print("Item Not Found! Please Try Again!")

def view_reports(reports):
    print("\nReports:")
    print(f"Total Customers: {len(reports)}")
    print(f"Total Profit: ${sum(reports)}")
    input("Click any key to go back to the main menu.\n")

def main():
    inventory = [
        Item("Playing cards", 4.95),
        Item("Monopoly", 12.99),
        Item("Candy Land", 11.99),
        Item("Lego Star wars", 25.99),
        Item("Lego Indiana Jones", 19.99),
        Item("Lego Harry Potter", 29.99)
    ]
    reports = []

    while True:
        print("Welcome to Target! Choose the following options:")
        print("1) Make a Purchase")
        print("2) Make a Return")
        print("3) Manage Inventory")
        print("4) View Report")
        print("5) Exit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            transaction = Purchase(inventory)
            transaction.complete(reports)
        elif choice == '2':
            transaction = Return(inventory)
            transaction.complete(reports)
        elif choice == '3':
            manager = InventoryManager(inventory)
            while True:
                manager.display_inventory()
                print("1) Add New Item")
                print("2) Remove Item")
                print("3) Main Menu")
                sub_choice = input("Select an option: ").strip()
                if sub_choice == '1':
                    manager.add_item()
                elif sub_choice == '2':
                    manager.remove_item()
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid option. Try again.")
        elif choice == '4':
            view_reports(reports)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()