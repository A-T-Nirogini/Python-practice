#sum of between the given numbers

start=int(input())
end=int(input())
sum=0
for i in range(start,end+1):
    sum=i+sum
print(sum)