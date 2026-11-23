# This program categorizes a student's performance based on their score. It takes an integer input for the score and prints whether the student is "Poor", "Average", or "Good". If the score is outside the valid range (0-100), it prints "Invalid score".
score=int(input())
if(score<35):
    print("Poor Student")
elif(35<score<70):
    print("Average Student")
elif(70<score<100):
    print("Good Student")
else:
    print("Invalid score")
