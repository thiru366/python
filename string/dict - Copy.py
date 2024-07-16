#dict

emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }
print(emp)
print(type(emp))
print(emp["age"])




#dict contructor
a=dict(name="hari",age=36,country="india")
print(a)
print(len(emp))
emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True,
    "age":35
     }
print(emp["age"])




emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }
print(emp["department"])
print(emp.get("active"))
print(emp.keys())




emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }
emp["salary"]=600000
print(emp)
emp["country"]="india"
print(emp)
print(emp.values())

emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }


if  "age" in emp:
    print("yes")
else:
    print("no")


emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }
emp["age"]=36
print(emp)
emp.update({"age":65})
print(emp)





emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }
emp.pop("active")
print(emp)

emp.popitem()
print(emp)


emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }
del emp["name"]
print(emp)


del emp
print(emp)


emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }
emp.clear()
print(emp)

emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }
for i in emp:
    print(i)
for i in emp:
    print(emp[i])


for i in emp.values():
    print(i)

for i in emp.keys():
    print(i)



for i,j in emp.items():
    print(i,j)





emp={
    "name":"hari",
    "age":34,
    "salary":50000,
    "department":"IT",
    "active":True
     }
x=emp.copy()
print(x)


x=dict(emp)
print(x) 

