#n = int(input("Enter any number"))
#for i in range(1,11):
    #a = i*n
    #print(n, "x", i, "=",a)

"""s = ""
n = int(input("enter n = "))
for i in range(n):
    name = input("Enter name")
    phone = input("Enter phone")
    s = s+name + " " + phone +"\n"

print(s)

fac = 1
n = int(input("Enter a number = "))
for i in range(1, n+1):
    fac = fac * i
print (fac)"""

#WAP to create a billing taking data from user like product_name, price, quantity

bill = str()
grand_total = 0
n = int(input("Enter the number of products = "))
for i in range(n):
    product_name = input("Enter the name of the product = ")
    quantity = int(input("Enter the quantity = "))
    unit_price = int(input("Enter the price of a unit of the product = "))
    total_price = quantity * unit_price
    grand_total = grand_total + total_price
    bill= bill + f"{product_name}  {quantity} {unit_price} {total_price}\n"

print(bill)
print("Grand Total = ", grand_total)
"""
i = 1
n = int(input("Enter a number"))
while i<=10:

    print(n, "*", i, " = ",n * i)
    i +=1

s = ""
i = 0
n = int(input("Enter n = "))
while i<n:
    name = input("Enter name = ")
    phone = input("Enter phone = ")
    s = s + name + " " + phone + "\n"
    i+=1
print(s)

for i in range(20):
    if i == 10:
        break
    print(i)

for i in range(20):
    if i == 10:
        continue
    print(i) """

#find prime