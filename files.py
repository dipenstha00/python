#file = open('file_name','modes')
#operations
#file.close()

#with open('file_name','modes'):
#operation

#   modes
#   r -> read
#   x -> create
#   w -> write
#   a -> append


with open('data.txt', 'r')as file:
    x = file.read()
    x = x.split('\n')
    print(x)

n = int(input("Enter n = "))
print(x[n-1])

with open('data.txt', 'r')as file:
    x = file.readline()
    print(x)

with open('JJ.txt','a') as file:
    file.write("\nJOker is not your regular person")
import os
try:
    os.remove('JJ.txt')
except:
    print("The file is not there!")

s = str()
grand_total = 0
def bills():
    global s
    global grand_total
    n = int(input("Enter the number of products to enter = "))
    for i in range(1, n+1):
        product_name = input("Enter the name of the product = ")
        quantity = int(input("Enter the quantity = "))
        unit_price = int(input("Enter the price of a unit of the product = "))
        total_price = quantity * unit_price
        grand_total = grand_total + total_price
        s = s + f"{i},{product_name},{quantity},{unit_price},{total_price}\n"

bills()
print(s)
print("Grand Total = ", grand_total)

with open('bills.csv','w') as file:
    file.write('SN,Name,Quantity, Price, Total\n')
    file.write(s)



