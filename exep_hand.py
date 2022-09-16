"""try:
    a = int(input("Enter a = "))
except:
    print("Enter integer value")

try:
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    c = a/b
except ZeroDivisionError:
    print("The value of b cannot be 0")
except ValueError:
    print("The value of a and b must ne integer")
else:
    print(c)
"""
#assert statement
n = int(input("Enter any number = "))

try:
    assert n > 0
except AssertionError:
    print("Please enter positive value")



