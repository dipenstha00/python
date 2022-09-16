#class <class_name>:
#   <operations>
#   obj = <class_name>()

"""class Hello:                    #class
    print("Hello World")
obj = Hello()                   #object

class Hey:
    def hello(self):
        print("hey hey hey")
obj = Hey()
obj.hello()


class Cal:
   #@staticmethod      #used to define if the method has static values so no need to use self in method
   def cal(self):
        l = int(input("Enter length = "))
        b = int(input("Enter breadth = "))
        h = int(input("Enter height = "))
        a = l*b
        v = a*h

        print("The are is = ", a)
        print("The volume is = ",v)
obj = Cal()
obj.cal()

class Cal:
    @staticmethod
    def cal(l,b,h):
        a = l*b
        v = a*h
        print("The area is = ",a)
        print("The volume is = ",v)

l = int(input("Enter length = "))
b = int(input("Enter breadth = "))
h = int(input("Enter height = "))

obj = Cal()
obj.cal(l,b,h)

class Cal:
    def __init__(self,l,b,h):
        self.l = l          #reinitializing the value
        self.b = l
        self.h = h
        #or
        #self.l,self.b,self.h = l,b,h
    def area(self):
        a = self.l*self.b
        print("The area is = ",a)
    def volume(self):
        v = self.l*self.b*self.h
        print("the volume is = ",v)
l = int(input("Enter length = "))
b = int(input("Enter breadth = "))
h = int(input("Enter height = "))

obj = Cal(l,b,h)
obj.area()
obj.volume()

class Info:
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add

    def my_info(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old from {self.add}")
name = input("Enter name = ")
age = int(input("Enter age = "))
add = input("Enter address = ")

obj = Info(name,age,add)
obj.my_info()
print(obj.name,obj.age,obj.add)

class Area:
    def __init__(self,x,y):
        self.x,self.y = x,y

    def area(self):
        a = self.x *self.y
        print("The area is = ",a)
class Volume:
    def __init__(self,x,y,z):
        self.x,self.y,self.z = x,y,z

    def volume(self):
        v = self.x * self.y * self.z
        print("The volume is = ",v)

l = int(input("Enter l = "))
b = int(input("Enter b = "))
h = int(input("Enter h = "))

obj1 = Volume(l,b,h)
obj = Area(l,b)
obj.area()
obj1.volume()


class Info:
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add

    def __str__(self):
        return self.name

name = input("Enter name = ")
age = int(input("Enter age = "))
add = input("Enter address = ")

obj = Info(name,age,add)
print(obj)
print(obj.__str__())
print(str(obj))

class Total:
    def __init__(self, x):
        self.x = x
        print("Object initialization",self.x)

    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        x = self.x+other.x
        print("Object addition",x)
        return Total(x)
obj = Total(1000)
obj1 = Total(2000)
obj2 = Total(3000)
print(obj+obj1+obj2)
"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1+p2)