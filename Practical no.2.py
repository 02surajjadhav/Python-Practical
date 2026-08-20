print("========== Grocery Shop Billing Calculator ===========")

customer_name=input("Enter customer name:")

item1 = input("Enter item 1 name:")
qty1 = int(input("Enter item 1 qty:"))
price1 = float(input("Enter item 1 price:"))
amount1 = price1*qty1

item2 = input("Enter item 2 name:")
qty2 = int(input("Enter item 2 qty:"))
price2 = float(input("Enter item 2 price:"))
amount2 = price2*qty2

item3 = input("Enter item 3 name:")
qty3 = int(input("Enter item 3 qty:"))
price3 = float(input("Enter item 3 price:"))
amount3 = price3*qty3

total_bill = amount1+amount2+amount3

if(total_bill>=700):
     discount=total_bill*0.40
     print("Discount : 40%  Discount")
elif(total_bill>= 500):
    discount =total_bill*0.30
    print("Discount : 30%  Discount")
elif(total_bill>=300):
     discount=total_bill*0.20
     print("Discount : 20%  Discount")
else:
     discount=0
     print("Discount : 00%  Discount")

final_amount=total_bill-discount

print("\n********************** Customer Bill *************************\n")
print("customer name is:",customer_name)
print("total bill is:",total_bill)
print("discount is:",discount)
print("final amount:",final_amount)

print("=================== THANK YOU ================")
