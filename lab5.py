print("..............Monthly Expense................")

total_expense = 0

while True:
    expense= float(input("Enter expense amount: "))
    total_expense=total_expense + expense

    choice= input("Add another expense? (y/n): ")

    if choice== "n":
        break

print("\n Monthly Total Expense")
print("Total Expense = $", total_expense)