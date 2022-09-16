# - Tuple
# - Indexing
# - Ordered
# - Multiple values
# - Duplicate values
# - Imutable

"""t = tuple()
t = (1,2,3,4,5,6)
r = ("Apple", "Ball", "Cat")
print(r)
print(type(r))

t = tuple()
n = int(input("enter range = "))
for i in range(n):
    x = input("Enter data = ")
    r = r , [x]
print (r)

t = tuple()
for i in range(3):
    x = int(input("Enter number = "))
    t = t + (x,)
print(t)

x = list(t)
print(x)

data = tuple()
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter add = ")
    data = data + ((name, age, add),)
print(data)
print(type(data))"""

#no append(), insert(), extend()
#no update()
#no del remove() pop()
#no sort()

a = (234,234234, 234,34345,5345,6754)

print(sorted(a))
