import random
n=int(input("How many passwords do You need : "))
a='abcdefghijklmnopqrstuvwxyz'
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
length=int(input("Enter length of password :"))
c='1234567890'
all = a+b+c
i=0
while i<n:
    pwd="".join(random.sample(all,length))
    print(pwd)
    i=i+1
