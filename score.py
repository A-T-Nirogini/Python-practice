# This program checks if a student is eligible based on their score percentage.
score=int(input("Score Persentage: "))
if(score>=70):
    name=input("Enter your name: ")
    department=input("Enter your department: ")
    location=input("Enter your location: ")
    print("You are  eligible.")

else:
    print("You are not eligible.")