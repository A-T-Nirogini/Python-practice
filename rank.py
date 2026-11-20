score=int(input())
if(score<35):
    print("Poor Student")
elif(35<score<70):
    print("Average Student")
elif(70<score<100):
    print("Good Student")
else:
    print("Invalid score")
