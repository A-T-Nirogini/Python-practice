#read numbers from the users and find their sum and average
sum=0
count=0
ran=int(input("Enter the range: "))
rang=int(input())
for i in range(ran,rang+1):
    print("Enter the",i,"number")
    a=int(input())
    sum=sum+a
    count=count+1
average=sum/count
print("Sum:",sum)
print("Average:",average)