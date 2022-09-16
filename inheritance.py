"""
class A:
    pass

class B:
    pass
obj = B()
print(obj)


class Data:
    def __init__(self):
        self.name = "Ram"
        self.add = "Boudha"

class Info(Data):
    def info(self):
        print(f"Hey I am {self.name} from {self.add}")

obj = Info()
obj.info()

class SI:
    def __init__(self):
        self.p = 1200
        self.r = 8
        self.t = 10
        p = int(input("Enter the priciple"))
        t = int(input("Enter the time"))
        r = int(input("Enter the rate"))
class Cal(SI):
    def cal(self):
        si = self.p*self.t*self.r/100
        print("The simple interest is = ",si)
obj = Cal()
obj.cal()

class SI:
    def __init__(self,t,r):

        self.r = t
        self.t = r

class Cal(SI):
    def __init__(self,p,t,r):
        self.p = p
        SI.__init__(self,t,r)
    def cal(self):
        si = self.p*self.t*self.r/100
        print("The simple interest is = ",si)

p = int(input("Enter the priciple"))
t = int(input("Enter the time"))
r = int(input("Enter the rate"))
obj = Cal(p,t,r)
obj.cal()


#multilevel inheritance
class A:
    pass
class B(A):
    pass
class C(B):
    pass
obj = C()


class SI:
    def __init__(self,p):
        self.p = p
class Data(SI):
    def __init__(self,p,t):
        self.t = t
        SI.__init__(self,p)

class Final(Data):
    def __init__(self,p,t,r):
        self.r = r
        Data.__init__(self,p,t)
    def final(self):
        si = self.p*self.t*self.r/100
        print("The simple interest is = ",si)

p = int(input("Enter the priciple"))
t = int(input("Enter the time"))
r = int(input("Enter the rate"))
obj = Final(p,t,r)
obj.final()


#multiple inheritance
class SI:
    def __init__(self,p):
        self.p = p
class Data:
    def __init__(self,p):
        self.t = t

class Final(SI,Data):
    def __init__(self,p,t,r):
        self.r = r
        SI.__init__(self,p)
        Data.__init__(self,t)
    def final(self):
        si = self.p*self.t*self.r/100
        print("The simple interest is = ",si)

p = int(input("Enter the priciple = "))
t = int(input("Enter the time = "))
r = int(input("Enter the rate = "))
obj = Final(p,t,r)
obj.final()
"""
#public member
class Info:
    def __init__(self,name,age,address):
        self.name = name
        self.address = address
        self.age = age

obj = Info("ram",23,"jorpati")
print(obj.name)
print(obj.age)
print(obj.address)


class Info:
    def __init__(self,name,age,address):
        self._name = name
        self._address = address
        self._age = age

obj = Info("ram",23,"jorpati")
print(obj.name)
print(obj.age)
print(obj.address)