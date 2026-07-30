print("===== Monthly Expense Tracker =====")

n = int(input("Enter the number of expenses: "))

expenses = []
total = 0

for i in range(n):
    amount = float(input(f"Enter expense {i + 1}: "))
    expenses.append(amount)
    total += amount   

while True:
    print("\n----- Expense Tracker Menu -----")
    print("1. Show All Expenses")
    print("2. Show Total Expense")
    print("3. Add New Expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nExpense List:")
        for i in range(len(expenses)):
            print(f"Expense {i + 1}: {expenses[i]}")

    elif choice == 2:
        print("Total Monthly Expense =", total)

    elif choice == 3:
        new_expense = float(input("Enter new expense: "))
        expenses.append(new_expense)
        total += new_expense
        print("Expense added successfully.")

    elif choice == 4:
        print("Thank you for using the Monthly Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")