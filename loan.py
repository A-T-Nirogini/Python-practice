# This program checks if a user is eligible for a loan based on their salary and age, and also checks if the requested loan amount is within the allowed limit.
salary=int(input("Enter your salary: "))
age=int(input("Enter your age: "))
if(salary>=20000 or age<=25):
    loan_amount=int(input("Enter the loan amount: "))
    if(loan_amount<=50000):
        print("You are eligible for loan.")
    else:
        print("Maximum loan amount is 50000")
else:
    print("You are not eligible for loan")