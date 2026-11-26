#This is a simple Python script that demonstrates the use of lists and some of their methods.
a=[1,2,3,4,5]
print(type(a))
a.append(6)
a.append("Hello")
a.append([1,8,9])
a.append(1)
print(a)
a.insert(2,115)
print(a)
a[0]="Hi"
print(a)
a.pop(7)
print(a)
b=["Hello", "World"]
b.pop()
b.pop()
print(b)