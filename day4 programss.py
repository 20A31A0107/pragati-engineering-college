#day4 programs

import re
str1= "she sells sea shells at sea shore"
p1="sells"
if re.match(p1,str1):
   print("match found")
else:
    print(p1," not present in string")
p2=" she"
if re.match(p2,str1):
    print("match found")
else:
    print(p1," not present in string")

    

import re
str1=" she sells sea shells at sea shore"
p1= "sea"
rep = 'ocean'
ns= re.sub(p1, rep,str1,1)
print(ns)




import re
p=r"[aeiou]"
if re.search(p,"clue"):
    print("matchy vowel")





from collections import Counter
def check(str1, str2):
    if(Counter(str1)==Counter(str2)):
        print("true")
    else:
        print("not")
str1= 'silent'
str2= 'listen'
check(str1, str2)




size =int(input("enter the size of bin"))
max=count=flag=0
x=input()
arr=list(x)
for i in range(0,size):
    if arr[i]=='1':
        count =count+1;
        flag=1;
    elif (arr[i]=='o' and flag ==1):
        count=0
        flag=0
    if count >max:
        max=count
print(max)

              






