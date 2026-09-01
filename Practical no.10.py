product_name = []
product_price = []
product_qty = []
while True:
    print("\n" + "=" * 50)
    print("           PRODUCT INVENTORY MANAGEMENT")
    print("=" * 50)
    print(" [1] Add Product")
    print(" [2] Delete Product")
    print(" [3] Update Product Price")
    print(" [4] Display All Products")
    print(" [5] Search Product")
    print(" [6] Sort Products by Price (Ascending)")
    print(" [7] Sort Products by Price (Descending)")
    print(" [8] Sort Products by Name (Alphabetical)")
    print(" [9] Show Costliest / Cheapest Product")
    print(" [10] Exit")
    print("-" * 50)
    choice = input("Enter your choice (1-10): ").strip()
    if choice == '1':
        name = input("Enter product name: ").strip()
        if name in product_name:
            print("\n[!] Product already exists. Please use Update Price.")
        else:
            price = float(input("Enter product price: "))
            qty = float(input("Enter product quantity: "))
            product_name.append(name)
            product_price.append(price)
            product_qty.append(qty)
            print(f"\n[+] Product '{name}' added successfully.")
    elif choice == '2':
        name = input("Enter product name to delete: ").strip()
        if name in product_name:
            index = product_name.index(name)
            product_name.pop(index)
            product_price.pop(index)
            product_qty.pop(index)
            print(f"\n[-] Product '{name}' deleted successfully.")
        else:
            print("\n[!] Product not found.")
    elif choice == '3':
        name = input("Enter product name to update: ").strip()
        if name in product_name:
            index = product_name.index(name)
            new_price = float(
                input(f"Enter new price for '{name}': ")
            )
            product_price[index] = new_price
            print(f"\n[*] Price of '{name}' updated successfully.")
        else:
            print("\n[!] Product not found.")
    elif choice == '4':
        if len(product_name) == 0:
            print("\n[!] No products available.")
        else:
            print("\n" + "-" * 55)
            print(
                "{:<5} {:<20} {:<12} {:<10}".format(
                    "No.", "Product Name", "Price", "Quantity"
                )
            )
            print("-" * 55)
            for i in range(len(product_name)):
                print(
                    "{:<5} {:<20} {:<12.2f} {:<10}".format(
                        i + 1,
                        product_name[i],
                        product_price[i],
                        product_qty[i]
                    )
                )
            print("-" * 55)
    elif choice == '5':
        name = input("Enter product name to search: ").strip()
        if name in product_name:
            index = product_name.index(name)
            print("\n" + "-" * 35)
            print("          PRODUCT FOUND")
            print("-" * 35)
            print(f"Name     : {product_name[index]}")
            print(f"Price    : {product_price[index]}")
            print(f"Quantity : {product_qty[index]}")
            print("-" * 35)
        else:
            print(f"\n[!] Product '{name}' not found.")
    elif choice == '6':
        if len(product_name) == 0:
            print("\n[!] No products available to sort.")
        else:
            combined = list(
                zip(product_price, product_name, product_qty)
            )
            combined.sort()
            product_price = [item[0] for item in combined]
            product_name = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]
            print("\n[✓] Products sorted by price in ascending order.")
    elif choice == '7':
        if len(product_name) == 0:
            print("\n[!] No products available to sort.")
        else:
            combined = list(
                zip(product_price, product_name, product_qty)
            )
            combined.sort(reverse=True)
            product_price = [item[0] for item in combined]
            product_name = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]
            print("\n[✓] Products sorted by price in descending order.")
    elif choice == '8':
        if len(product_name) == 0:
            print("\n[!] No products available to sort.")
        else:
            combined = list(
                zip(product_name, product_price, product_qty)
            )
            combined.sort()
            product_name = [item[0] for item in combined]
            product_price = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]
            print("\n[✓] Products sorted alphabetically by name.")
    elif choice == '9':
        if len(product_price) == 0:
            print("\n[!] No products available.")
        else:
            highest = max(product_price)
            lowest = min(product_price)
            costliest_index = product_price.index(highest)
            cheapest_index = product_price.index(lowest)
            print("\n" + "=" * 40)
            print("             PRICE SUMMARY")
            print("=" * 40)
            print(
                f"Costliest Product : "
                f"{product_name[costliest_index]}"
            )
            print(
                f"Highest Price     : "
                f"{highest:.2f}"
            )
            print("-" * 40)
            print(
                f"Cheapest Product  : "
                f"{product_name[cheapest_index]}"
            )
            print(f"Lowest Price : "  f"{lowest:.2f}" )
            print("=" * 40)
    elif choice == '10':
        print("\n" + "=" * 50)
        print("Thank you for using the Inventory Management System!")
        print("Program closed successfully.")
        print("=" * 50)
        break
    else:
        print("\n[!] Invalid choice.")
        print("Please enter a number between 1 and 10.")a
