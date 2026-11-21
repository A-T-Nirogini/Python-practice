a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if(i%2==0):
        print(i)
        count=count+1
print("the even numbers between",a,"to",b,"is",count)
