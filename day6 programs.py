#program to create and access an obj

class abc:
    var =10
obj= abc()
print(obj.var)



class abc:
    attribute1=10
obj= abc()
print(obj.attribute1)

#program to create self arg and access an obj

class abc:
    attribute1=10
    def display(self):
        print("this is in class")
obj=abc()
print(obj.attribute1)
obj.display()

#program to check the usage of constructor

class abc:
    def __init__(self,value):
       print("this is in class")
       self.value=value
       print("the value is ",value)
obj= abc(10)

#program to check difference between object and class variable

class abc:
    class_var= 0
    def __init__(self,var):
        abc.class_var +=1
        self.var= var
        print("the obj value is ",var)
        print("the class value is ",abc.class_var)
obj1= abc(100)
obj2= abc(101)
obj3= abc(102)

#program to check given no is odd or even by using single stance class object with an attribute following the constructor

class Number:
    even= 0
    def check(self,num):
        if num%2 ==0:
             self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n= Number()
n.even_odd(21)


class Number:
    even= []
    odd= []
    def __init__(self,num):
        self.num=num
        if num%2 ==0:
           Number.even.append(num)
        else:
           Number.odd.append(num)
n1= Number(11)
n2= Number(12)
n3= Number(13)
n4= Number(28)
n5= Number(7)
print("even number list is ",Number.even)
print("odd number list is ",Number.odd)


#program that has a class named circle use a class variable to define values of const pi use this class variable to calculate area and circumference of a circle with specified radius,where radius=7.5 

class circle:
    pi = 3.14159
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.pi*self.r*self.r
    def circum(self):
        return 2*circle.pi*self.r
c= circle(7.5)
print("area=",c.area())
print("circumference",c.circum())























        



















































        
