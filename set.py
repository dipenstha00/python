#set:
#-no indexing
#-no duplicate data
#- unordered
#- mutable

"""a = set()
b = {1,1,2,2,3,3,4,4}
c = {"Ball",  "Ball", "Apple", "Circle"}
print(b)
print(c)
for i in c:
    print(i)

l = set()
n = int(input("Enter n = "))
for i in range(n):
    x = int(input("Enter x = "))
    l.add(x)
print(l)

a ={1,3,5,7,9}
b= {2,4,6,8}
a.update(b)
a.remove(5)
print(a)

a = [1,2,2,3,3,4,5,6,7,8,9,10]
b =set(a)
b = list(b)
print(a)
print(b)

#union
#intersection
#difference

U = {'Strawberry', 'Mango', 'Orange', 'Apple', 'Blackberry', 'Blueberry', 'Grapes', 'Banana'}
a = {"Apple", "Orange", "Mango", "Strawberry"}
b = {"Strawberry", "Blueberry", "Blackberry"}
print(a.union(b))
print(a.intersection(b))
print(b.difference(a))
print(U-a.union(b))"""

a = {1,2,3,4,5,6,7,8,9,10}
b = {2,4,6,8}
print(b.issubset(a))
print(a.issuperset(b))
