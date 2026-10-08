
# EXERCISE : 16.1
# Digital Wallet Simulator

balance = 0.0
transactions = []

def add_funds():
    global balance
    amount = float(input("Enter amount to add: ₹"))

    if amount > 0:
        balance += amount
        transactions.append("Added funds: ₹" + str(amount))
        print("Funds added successfully!")
        print("Current balance: ₹", balance)
    else:
        print("Amount must be greater than 0.")

def pay_bill():
    global balance
    bill_name = input("Enter bill name: ")
    amount = float(input("Enter bill amount: ₹"))

    if amount <= 0:
        print("Amount must be greater than 0.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        transactions.append("Paid " + bill_name + ": ₹" + str(amount))
        print("Bill paid successfully!")
        print("Remaining balance: ₹", balance)

def view_balance():
    print("Current wallet balance: ₹", balance)

def transaction_history():
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("\n===== TRANSACTION HISTORY =====")
        for i in range(len(transactions)):
            print(i + 1, ".", transactions[i])

def main():
    while True:
        print("\n===== DIGITAL WALLET =====")
        print("1. Add Funds")
        print("2. Pay Bill")
        print("3. View Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_funds()
        elif choice == "2":
            pay_bill()
        elif choice == "3":
            view_balance()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("Thank you for using the Digital Wallet!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# EXERCISE : 16.2
# Inventory Tracking System

inventory = {}

def add_stock():
    product = input("Enter product name: ").strip()
    quantity = int(input("Enter quantity to add: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

    print(quantity, product, "added successfully!")
    print("Current stock:", inventory[product])

def register_sale():
    product = input("Enter product name: ").strip()

    if product not in inventory:
        print("Product not found in inventory.")
        return

    quantity = int(input("Enter quantity sold: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
    elif quantity > inventory[product]:
        print("Not enough stock available.")
    else:
        inventory[product] -= quantity
        print("Sale registered successfully!")
        print("Remaining", product, "stock:", inventory[product])

def display_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("\n===== CURRENT INVENTORY =====")
        for product, quantity in inventory.items():
            print(product, ":", quantity)

def main():
    while True:
        print("\n===== SHOP INVENTORY SYSTEM =====")
        print("1. Add Stock")
        print("2. Register Sale")
        print("3. Display Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            register_sale()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            print("Thank you for using the Inventory System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
