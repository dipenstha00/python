"""a = "String"
b = a[-1]
print(b)

a = "String"
b = a[1:4]
print(b)

a = "String"
b = a[0:3:2]
print(b)

a = "String"
print(a[::-1])

#string formatting
a = "Java"
b = "Python"
c = "PHP"

print(f"Hello these are the programming languages i learned: {a}, {b}, {c}

#search
string = "Hello Hi Greetings Bonjour Ohio Hi".lower()
x = input("Enter a greetings = ")
if x in string:
    print(f"Yes, {x} is valid")
    print(string.count(x))
else:
    print(f"No, {x} is not valid")

# immutable datatype : if original value is not changed even after applying function like lowercasing and uppercasing.

#replace
string = "Hello Hi Greetings Bonjour Ohio Hi"
print(string.replace('Hi','hi'))"""

a = "String"
for i in range(len(a)):
    print(i,a[i])

