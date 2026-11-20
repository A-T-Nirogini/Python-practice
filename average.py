maths=int(input("Enter your maths marks: "))
science=int(input("Enter your science marks: "))
english=int(input("Enter your english marks: "))
ict=int(input("Enter your ict marks: "))
tamil=int(input("Enter your tamil marks: "))

average=(maths+science+english+ict+tamil)/5
print(average)
if(average<35):
    print("Additional class is required")
else:
    print("You are good to go.")