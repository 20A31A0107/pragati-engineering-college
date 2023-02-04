#== comparing value and datatype
a=6
b=True
if(1==b):
    print("yes")
else:
    print("no")

#reverse order of alphabets
    
for i in range(122,96,-1):
    print(chr(i),end=" ")

#double for loop

rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')

        
#for loop

age=[2,4,6,8]
for i in range(len(age)):
    print(i)

#double for
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")


#while loop

i = 1
n = 5
while i <= n:
    print(i)
    i = i + 1

#Check wheter the given number even+ve or odd+ve or even-ve or odd-ve

a=int(input("THE GIVEN NUMBER BE:- "))
if((a%2==0)&(a>0)):
    print("THE GIVEN NUMBER IS EVEN POSITIVE NUMBER")
elif((a%2!=0)&(a>0)):
    print("THE GIVEN NUMBER IS ODD POSITIVE NUMBER")
elif((a%2==0)&(a<0)):
    print("THE GIVEN NUMBER IS EVEN NEGATIVE NUMBER")
elif((a%2!=0)&(a<0)):
    print("THE GIVEN NUMBER IS ODD NEGATIVE NUMBER")
else:
    print("THE NUMBER IS ZERO")



#check whether the given number is divisible by 11 or not

a=int(input("ENTER THE NUMBER a= "))
if(a%11==0):
    print("THE GIVEN NUMBER IS DIVISIBLE BY 11")
else:
    print("THE GIVEN NUMBER IS NOT DIVISIBLE BY 11")
