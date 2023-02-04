def total(a,b):
    result=a+b
    print("function result is",result)
a=int(input("enter the value of a"))
b=int(input("enter the value pf b "))
total(a,b)



def total(a,b):
    result=a+b
    print("function result is ",result)
def diff(a,b):
    result2=a-b
    print("function result2 is ",result2)
def prod(a,b):
    result3=a*b
    print("funcion result3 is ",result3)
def div(a,b):
    result4=a/b
    print("function result is ",result4)
x=int(input("enter the value of a"))
y=int(input("enter the value of b"))
total(x,y)
diff(x,y)
prod(x,y)
div(x,y)



def pk(money):
    print("give pinku the sum of ",money)
money=50
pk(money)



var = 'vijay'
def show():
    global var1
    var1 = 'tall'
    print("in function var is",var)
show()
print("outside fun",var1)
print("var is ",var)



def outf():
    var = 10
    def innf():
        var = 20
        print("inner var",var)
    innf()
    print("outer var",var)
outf()



def cube(x):
    return(x*x*x)
num= 10
result= cube(num)
print("output of the evaluation is ",result)


def display(str1):
    print(str1)
str1='hi'
display(str1)
        

def display(name,age):
    print("name",name)
    print("age",age)
n= "vj"
y= 77
display(name=n, age= y)


def fib(n):
    if n<2:
        return 1
    return(fib(n-1)+fib(n-2))
n= int(input())
for i in range(n):
    print("fibonacci (",i,")",fib(i))



















