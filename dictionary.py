#Dictionary
# Indexing
# Ordered
# Mutable
# Multiple and duplicate data

"""d = {}
e = dict()
print(type(d))
print(type(e))

# d = (<key>:<value>, <key>:<value>}
d = { 'a': 'apple', 'b':'ball', 'c' : 'cat'}
a = {1:1,2:4,3:9,4:16}
print(a,d)

#can have same values but not same keys. When it happens the last value of the key is taken
d = { 'a': 'apple', 'b':'ball', 'c' : 'cat', 'C':'cat'}
print(d)
d = { 'a': 'apple', 'b':'ball', 'c' : 'cat', 'c' : 'cat'}
print(d)

a ={}
a['a'] = "Apple"
a['b'] = "Ball"
a['c'] = "Cat"
print(a)

d = {}
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    phone = int(input("Enter phone number = "))
    key = name
    value = phone
    d[key] = value
print(d)

d = {'Dipen': 9860597634, 'Shrestha': 9808050882}
for i in d.items():
    print("to print elements", i)
for i in d:
    print("to print keys", i)
for i in d.values():
    print("to print values", i)
print(len(d))"""

d = {'Dipen': 9860597634, 'Shrestha': 9808050882}
"""l = []
for i in d.items():
    l.append(i)
print(l)
print(dict(l))
a = {1:1,2:4,3:9}
d.update(a)
print(d)
print(a[3])
#del a[2]
#pop
b = a.pop(2)
print(a)
print(b)

#list inside dictionary

d = {'Dipen': [9860597634,9808085858], 'Shrestha': [9808050882,98989898989]}
print(d['Dipen'])
print(d['Dipen'][0])

d = {}
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    ntc_phone = int(input("Enter ntc phone number = "))
    ncell_phone = int(input("Enter Ncell phone number = "))
    #key = name
    #value = [ntc_phone, ncell_phone]
    #d[key] = value
    d[name] = [ntc_phone, ncell_phone]
print(d)

d = {'name':[], 'age':[], 'add':[]}

n = int(input("enter n = "))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter address = ")

    d['name'].append(name) 
    d['age'].append(age)
    d['add'].append(add)

print(d)

d = {'name': ['Dipen', 'Shrestha'], 'age': [23, 24], 'add': ['Jorpati', 'Boudha']}
d['add'][0]  = 'KTM'
print(d)
del d['name'][0]
del d['age'][0]
del d['add'][0]
print(d)

#dict inside list
#Wap to create dict inside list and perform CRUD
a = [{'name' : 'Ram', 'age' : 45, 'add' : 'Kathmandu'},
     {'name' : 'Shyam', 'age' : 32, 'add' : 'BHaktapur'}]

#nested dictionary

d = {   1 : {'name' : 'Joker', 'age' : 23, 'grade' : 'A'},
        2 : {'name' : 'Puran', 'age' : 21, 'grade' : 'A-'},
        3 : {'name' : 'Prasad', 'age' : 22, 'grade' : 'A+'}}
print(d)

d ={}
n = int(input("Enter the value of n = "))
for i in range(1,n+1):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter address = ")
    data = {'name':name,'age':age,'add':add}
    d[i] = data
print(d)

a = {1: {'name': 'Dipen', 'age': 23, 'add': 'Jorapti'}, 2: {'name': 'Shrestha', 'age': 24, 'add': 'Narayantar'}}
a[3] = {'name':'Joker', 'age':25, 'add' : 'Kathmandu'}
for i in a.items():
    print(i)
a[1]['age'] = 24
print(a)
del a[3]['name']
print(a)"""

#WAP to create a result management system for a class[using dict inside dict]
#physics - th pr
#chemistry - th pr
#grade
#total
sub = {}
for i in range(1,2):
    phyTH = int(input("Enter  theoretical marks in Physics = "))
    phyPR = int(input("Enter  practical marks in Physics = "))
    chemTH = int(input("Enter marks in Chemistry = "))
    chemPR = int(input("Enter marks in Chemistry = "))
    math = int(input("Enter marks in Mathematics = "))
    english = int(input("Enter marks in English = "))
    nepali = int(input("Enter marks in Nepali = "))
    total = phyTH + phyPR + chemTH + chemPR + math + english + nepali
    per = total/700 *100
    if per>= 90:
        grade = "A+"
    elif per>= 80:
        grade = "A"
    elif per>= 70:
        grade = "B+"
    elif per>= 60:
        grade = "B"
    elif per>= 50:
        grade = "C"
    else:
        grade = "Failed"
    data = {'phyTH' : phyTH, 'phyPR': phyPR, 'chemTH': chemTH, 'chemPR' : chemPR,'math':math, 'english':english,'nepali':nepali,'total':total,'grade':grade}
    sub[i] = data
print(sub)