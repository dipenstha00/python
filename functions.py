# def function_name():
    #<operation>
#function_name()

def area():
    l = int(input("Enter the value of length = "))      #local variable
    b = int(input("Enter the value of breadth = "))     #local variable
    a = l*b
    print("The area of the rectangle is", a)
area()


l = 20      #global variable
b = 10      #global variable
def area1():
    a = l*b
    print(a)
area1()

def area():
    global l,b
    l = 10
    b = 2
    a = l*b
    print(a)
area()
print(l,b)

# functions without arguments and non return type
# function with argument and non return type
# function without arguments and return type
# function with argument and return type

#argument
def area(x,y):          #parameter
    a = x*y
    print(a)
#l = int(input("Enter the value of length = "))
#b = int(input("Enter the value of breadth = "))
area(10,20)               #Argument

#function with argument and non return type
def area(x,y):
    a = x*y
    print(a)
def volume(x,y,z):
    v = x*y*z
    print(v)
l = int(input("Enter the length = "))
b = int(input("Enter the breadth = "))
h = int(input("Enter the height = "))
area(l,b)
volume(l,b,h)

def language(lan = "Python"):
    print(lan)

language("c")
language("c++")
language("java")
language()

#return type function
def belo():
    return "Hey!"
print(belo())

def belo():
    return"Hello"
x = belo()
print(x)

#function without argument and return type
def area():
    l = 2
    b = 4
    a = l*b
    return a
ar = area()
h = 2
v = ar * h
print("The area is = ",ar)
print("The volume is = ", v)

def area(l,b):
    a = l*b
    return a
l = int(input("Enter the length = "))
b = int(input("Enter the breadth = "))

ar =area(l,b)
print("The area  = ", ar)

#to pass list or tuple as argument
def cal(x):
    l,b,h = x
    v = l*b*h
    return v

l = 2
b = 3
h = 4
data = (l,b,h)
v = cal(data)
print(v)

def SI(x):
    x = p,t,r
    si = p*t*r/100
    return si

p  = int(input("Enter principle = "))
t = int(input("Enter time = "))
r = int(input("Enter rate = "))
d = (p,t,r)
i = SI(d)
print(i)

#recursive funtion
def hello():
    print("Hello")
    x = input("Enter y for more print")
    if x == '' :
        hello()
hello()

s = str()
grand_total = 0
def bills():
    global s
    global grand_total

    product_name = input("Enter the name of the product = ")
    quantity = int(input("Enter the quantity = "))
    unit_price = int(input("Enter the price of a unit of the product = "))
    total_price = quantity * unit_price
    grand_total = grand_total + total_price
    s = s + f"{product_name}  {quantity} {unit_price} {total_price}\n"
    x = input("Enter y for more entry")
    if x == 'y':
        bills()

bills()
print(s)
print("Grand Total = ", grand_total)