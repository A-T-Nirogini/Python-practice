# This program prints all even numbers between two given integers and counts how many even numbers are found.
a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if(i%2==0):
        print(i)
        count=count+1
print("the even numbers between",a,"to",b,"is",count)
