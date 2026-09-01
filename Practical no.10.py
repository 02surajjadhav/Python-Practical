product_name=[]
product_price=[]
product_qty=[]

while True:
    print("*"*45)
    print("Product Inventory System")
    print("*"*45)
    print("1. Add Product.")
    print("2. Delete Product.")
    print("3. Update Product Price.")
    print("4. Display All Product.")
    print("5. Searching Product.")
    print("6. Sort Product by Price(Accending).")
    print("7. Sort Product by Price(Decending).")
    print("8. Sort Product by Price(Alphabetical).")
    print("9. Show Costliest/Cheapest Product.")
    print("10. Exit.")

    choice=input("Enter your choice(1-10):").strip()

    if choice=='1':
        name=input("Enter Product name=")
        if name is  product_name:
            print("Product Already Exists!!!! Use update Instead.")
        else:
            price=float(input("Enter Product Price="))
            qty=float(input("Enter Product qty="))
            product_name.append(name)
            product_price.append(price)
            product_qty.append(qty)
            print(f"Product '{name}' Added Successfully!!")

    elif choice=='2':
        name=input("Enter Product name to Delete=")
        if name in product_name:
            index=product_name.index(name)
            product_name.pop(index)
            product_price.pop(index)
            product_qty.pop(index)
            print(f"Product'{name}' Deleted Successfully!!")
        else:
            print("Product is not Found!!!!")

    elif choice=='3':
        name=(input("Enter Product name to Update="))
        if name in product_name:
            index=product_name.index(name)
            new_price=float(input(f"Enter New Product Price for '{name}'="))
            product_price[index]=new_price
            print(f"price for '{name}' is Update Successfully!!!!")
        else:
            print("Product is not Found!!!!")

    elif choice=='4':
        if len(product_name)==0:
            print("No Product To Display!!!")
        else:
            print("\n {:<5},{:<10},{:<20}".format("no.","Name.","Price.","qty."))
            print("="*40)
            for i in range(len(product_name)):
                print("{:<5},{:<10},{:<20}".format(i+1,product_name[i],product_price[i],product_qty[i]))
            print()

    elif choice=='5':
        name=(input("Enter Product name to Search=")).strip()
        if name in product_name:
            index=product_name.index(name)
            print(f"Found-> Name:{product_name[index]}"
                  f"Price={product_price[index]},Qty={product_qty[index]}\n")
        else:
            print(f"Product '{name}' not Found.\n")

    elif choice=='6':
        if len(product_name)==0:
            print("No Product To Sort!.\n")
        else:
            combined=list(zip(product_price,product_name,product_qty))
            combined.sort()

            product_price=[item[0] for item in combined]
            product_name=[item[1] for item in combined]
            product_qty=[item[2] for item in combined]
            print("Product sorted by price(ascending) ")
            
    elif choice=='7':
        if len(product_name)==0:
            print("No product to sort!\n")
        else:
            combined= list(zip(product_price,product_name,product_qty))
            combined.sort(reverse=True)
            
            product_price=[item[0] for item in combined]
            product_name=[item[1] for item in combined]
            product_qty=[item[2] for item in combined]
            print("Product sorted by price(Descending)!\n ")
    
    elif choice=='8':
        if len(product_name)==0:
            print("No Product to Sort!!!\n")
        else:
            combined= list(zip(product_name,product_price,product_qty))
            combined.sort(reverse=True)
                        
            product_name=[item[0] for item in combined]
            product_price=[item[1] for item in combined]
            product_qty=[item[2] for item in combined]
            print("Product sorted by Name(alphabetically))!\n ")
            
    elif choice=='9':
        if len(product_price)==0:
            print("No Products Available!!!\n")
        else:
            highest= max(product_price)
            lowest= min(product_price)
            
            costliest_index = product_price.index(highest)
            cheapest_index = product_price.index(lowest)
            
            print("\n=====Price Summary=====")
            print(f"costliest Product : {product_name[costliest_index]} (price:{ highest})")                 
            print(f"cheapest Product : {product_name[cheapest_index]} (price:{ lowest})") 
            print()
            
            
    elif choice== '10':
        print("Exiting Program. Thank You!!!\n")
        break
    else:
        print("Invalid Choice. Please choose a number between 1 and 10.\n")
