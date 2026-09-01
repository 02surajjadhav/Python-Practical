product_names = []
product_prices = []
product_qty = []

while True:
    print("=" *45)
    print(" PRODUCT INVENTORY SYSTEM ")
    print("=" *45)
    print("1. Add product ")
    print("2. Delete product ")
    print("3. Update product price " )
    print("4. Display all Products ")
    print("5. Search Product (by name)")
    print("6. Sort Product by Price(Ascending)")
    print("7. Sort Product by Price(Descending)")
    print("8. Sort Product by Price(Alphabetical)")
    print("9. Show Costliest / Cheaper Product ")
    print("10. Exit")
    print("=" *40)

    choice = input("Enter your choice(1-10):").strip()
    if choice == '1':
            name = input("Enter Product Name:").strip()
    
            if name in product_names :
                print(f"Product '{name}' already exists! use update option instead.\n")
            else:
                price = float(input(f"Enter price for {name}: "))
                qty = int(input(f"Enter quantity for {name}: "))
                product_names .append(name)
                product_prices.append(price)
                product_qty .append(qty)
                print(f"Product '{name}' added succesfully.\n")
    elif choice == '2':
         name = input("Enter Product Name to delete: ").strip()
                         
         if name in product_names :
              index = product_names.index(name)
              product_names.pop(index)
              product_prices.pop(index)
              product_qty.pop(index)
              print(f"Product '{name}' deleted succesfully.\n")
         else:
            print(f"Product '{name}' not found.\n")

    elif choice =='3':
             name = input("Enter Product Name to update: ").strip()
    
             if name in product_names :
                  index = product_names.index(name)
                  new_price = float(input(f"Enter new price for {name}: "))
                  product_prices[index] = new_price 
                  print(f"price  for '{name}' updated succesfully.\n")
             else:
                 print(f"product '{name}' not found.\n")        
         
    elif choice == '4':
            if len(product_names) == 0:
                print("No Products to display.\n")
            else:
                print("\n{:<5} {:<20} {:<10}".format("No.", "Name", "Price", "qty"))
                print("=" *45)
                for i in range(len(product_names)):
                    print("{:<5} {:<20} {:<30}".format(i+1, product_names[i] , product_names[i]))
                    print()  

    elif choice == '5' :
            name = input("Enter Product name to searching: ").strip()
            if name in product_names:
                index = product_names.index(name)
                print(f"Found -> Name : {product_names[index]},"
                      f"Price: {product_names[index]},Qty: {product_names[index]}\n")
            else:
                print(f"Product '{name}' not found.\n")
    
    elif choice == '6':   
         if len(product_names) == 0:
              print("no product to sort.\n") 
         else:
              combined = list(zip(product_prices, product_names, product_qty))
              combined.sort()

              product_prices = [item[0] for item in combined]
              product_names = [item[1] for item in combined]
              product_qty = [item[2] for item in combined]
              print("Product sorted by price(ascending).\n")

    elif choice == '8':   
                 if len(product_names) == 0:
                      print("no product to sort.\n") 
                 else:
                      combined = list(zip(product_prices, product_names, product_qty))
                      combined.sort()
    
                      product_prices = [item[0] for item in combined]
                      product_names = [item[1] for item in combined]
                      product_qty = [item[2] for item in combined]
                      print("Product sorted by Alphabeticaly by name.\n")

    elif choice == '9':   
                     if len(product_prices) == 0:
                          print("no product available.\n") 
                     else:
                           highest = max(product_prices)
                           lowest = min(product_prices) 

                     costliest_index = product_prices.index(highest)
                     cheapest_index = product_prices.index(lowest)

                     print("\n**********Price summery **********")
                     print(f"Costliest Product : {product_names[costliest_index]} (Price: {highest})")
                     print(f"Cheapest Product : {product_names[cheapest_index]} (Price: {lowest})")

    elif choice == '10':
          print("Exiting program. Thank you!")
          break
    else:
          print("Invalid choice. Please enter a number between 1 to 10.\n")
