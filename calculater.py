# This program performs basic arithmetic operations based on user input.
a=int(input())
b=int(input())
c=input()

if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)
else:
    print("Invalid symbol")