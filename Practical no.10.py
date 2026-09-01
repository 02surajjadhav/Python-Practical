product_name = []
product_price = []
product_qty = []

while True:

    print("\n" + "*" * 45)
    print("        PRODUCT INVENTORY SYSTEM")
    print("*" * 45)

    print("1. Add Product")
    print("2. Delete Product")
    print("3. Update Product Price")
    print("4. Display All Products")
    print("5. Search Product")
    print("6. Sort Product by Price (Ascending)")
    print("7. Sort Product by Price (Descending)")
    print("8. Sort Product by Name (Alphabetical)")
    print("9. Show Costliest/Cheapest Product")
    print("10. Exit")

    print("*" * 45)

    choice = input("Enter your choice (1-10): ").strip()

    # Add Product
    if choice == "1":

        name = input("Enter Product Name = ").strip()

        if name in product_name:
            print("Product Already Exists! Use Update Instead.")

        else:
            price = float(input("Enter Product Price = "))
            qty = int(input("Enter Product Quantity = "))

            product_name.append(name)
            product_price.append(price)
            product_qty.append(qty)

            print("Product Added Successfully!")

    # Delete Product
    elif choice == "2":

        name = input("Enter Product Name to Delete = ").strip()

        if name in product_name:

            index = product_name.index(name)

            product_name.pop(index)
            product_price.pop(index)
            product_qty.pop(index)

            print("Product Deleted Successfully!")

        else:
            print("Product Not Found!")

    # Update Price
    elif choice == "3":

        name = input("Enter Product Name to Update = ").strip()

        if name in product_name:

            index = product_name.index(name)

            new_price = float(
                input("Enter New Product Price = ")
            )

            product_price[index] = new_price

            print("Price Updated Successfully!")

        else:
            print("Product Not Found!")

    # Display Products
    elif choice == "4":

        if len(product_name) == 0:

            print("No Products Available!")

        else:

            print("\n" + "-" * 55)
            print("{:<5} {:<20} {:<15} {:<10}".format(
                "No.", "Name", "Price", "Qty"
            ))
            print("-" * 55)

            for i in range(len(product_name)):

                print("{:<5} {:<20} ₹{:<14.2f} {:<10}".format(
                    i + 1,
                    product_name[i],
                    product_price[i],
                    product_qty[i]
                ))

            print("-" * 55)

    # Search Product
    elif choice == "5":

        name = input("Enter Product Name to Search = ").strip()

        if name in product_name:

            index = product_name.index(name)

            print("\nProduct Found!")
            print("Name     :", product_name[index])
            print("Price    :", product_price[index])
            print("Quantity :", product_qty[index])

        else:
            print("Product Not Found!")

    # Sort by Price Ascending
    elif choice == "6":

        if len(product_name) == 0:

            print("No Products to Sort!")

        else:

            combined = list(
                zip(product_price, product_name, product_qty)
            )

            combined.sort()

            product_price = [item[0] for item in combined]
            product_name = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]

            print("Products Sorted by Price (Ascending)!")

    # Sort by Price Descending
    elif choice == "7":

        if len(product_name) == 0:

            print("No Products to Sort!")

        else:

            combined = list(
                zip(product_price, product_name, product_qty)
            )

            combined.sort(reverse=True)

            product_price = [item[0] for item in combined]
            product_name = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]

            print("Products Sorted by Price (Descending)!")

    # Sort by Name
    elif choice == "8":

        if len(product_name) == 0:

            print("No Products to Sort!")

        else:

            combined = list(
                zip(product_name, product_price, product_qty)
            )

            combined.sort()

            product_name = [item[0] for item in combined]
            product_price = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]

            print("Products Sorted by Name (A-Z)!")

    # Costliest and Cheapest
    elif choice == "9":

        if len(product_price) == 0:

            print("No Products Available!")

        else:

            highest = max(product_price)
            lowest = min(product_price)

            costliest_index = product_price.index(highest)
            cheapest_index = product_price.index(lowest)

            print("\n===== PRICE SUMMARY =====")

            print(
                "Costliest Product:",
                product_name[costliest_index],
                "₹", highest
            )

            print(
                "Cheapest Product :",
                product_name[cheapest_index],
                "₹", lowest
            )

    # Exit
    elif choice == "10":

        print("\nExiting Program...")
        print("Thank You!")
        break

    else:

        print("Invalid Choice! Please enter 1-10.")
