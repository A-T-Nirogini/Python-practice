# Dictionary in Python
a={
    "name":"Nirogini",
    "Age":22,
    "Subjects":["Maths","Science"]
}
print (a)
a["age"]=21
a["colour"]="red"
print(a)
print(a.keys())
print(a.values())
a.update({"age":16})
print(a)

a.pop("colour")
print(a)
del a["Subjects"]
print(a)
del a
print(a) #error because the dictionary is deleted
