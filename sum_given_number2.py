#read numbers from the users and find their sum and average
sum=0

a=[]
count=int(input("Enter the count: "))

for i in range(1,count+1):
    num=int(input("Enter the number: "+str(i)))
    a.append(num)

for i in a:
    sum=sum+ i
    
average=sum/count
print(a)
print("Sum:",sum)
print("Average:",average)