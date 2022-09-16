"""b = ["Oreo", "kitkat", "Dairy Milk", "Snickers"]
#print(b[0:4:1])
c = ["Mars"]
d = b+c
print(d)

a = [1,2,3,4]
print(a*2)

l = list()
n = int(input("Enter the range = "))
for i in range(n):
    #x = input("Enter the string = ")
    x = int(input("Enter the number = "))
    l = l + [x]
print("the max value is = ",max(l))
print("The minimum value is = ", min(l))
print("the sum of the list is = ", sum(l))
l.sort()
print(l)
l.reverse()
print(l)

b = ["Oreo", "kitkat", "Dairy Milk", "Snickers"]
for i in b:
    if i != 'Oreo':
        print(i)

if 'Oreo' in b:
    print("yes",b.count('Oreo'))
else:
    print("No")
#append(),isnert(),extend()
b = ["Oreo", "kitkat", "Dairy Milk", "Snickers"]
a = ["Kurkure", "Ramen"]
b.append("Mars")
print(b)
b.insert(4,"Lays")
print(b)
b.extend(a)
print(b)

b = ["Oreo", "kitkat", "Dairy Milk", "Snickers"]
b[0:3] = [1,2,3]
a[0] = "Mars"
print(a)
print(b)

#del(), remove(), pop()
a = ["Oreo", "kitkat", "Dairy Milk", "Snickers"]
del a[1]
print(a)
#del a[0:2]
a.remove('Oreo')
print(a)

a = ["Oreo", "kitkat", "Dairy Milk", "Snickers"]
b = a.pop(3)
print(b)

#to use del() and pop() we need to have good understanding of index in the list

#make search in list case insensitive

data = []
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter add = ")
    data.append([name, age, add])
print(data)

data = [['Dipen', 23, 'Jorpati'], ['Shrestha', 24, 'Boudha']]
name = input("Enter the name to search = ")
for i in data:
    if name in i:
        print(i)

a = [['Dipen', 23, 'Jorpati'], ['Shrestha', 24, 'Boudha']]

a = []
n = int(input(print("Enter n = ")))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter address = ")
    data = {'name' : name , 'age' : age, 'add' : add}
    a.append(data)
print(a)"""

b = [{'name': 'Dipen', 'age': 23, 'add': 'Jorpati'}, {'name': 'Shrestha', 'age': 22, 'add': 'Boudha'}]
#to delete
del b[0]
print(b)
#to add
data =  {'name' : 'Joker', 'age' : 25, 'add' : 'Chabahil'}
b.append(data)
print(b)
#to update
b[0] = {'name': 'Dipen', 'age': 23, 'add': 'Jorpati'}
print(b)
#to update specific keys or values
b[0]['age'] = 25
print(b)