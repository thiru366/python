a=(1,)
print(type(a))


a = ("apple", "banana", "cherry")
print(a)



a = ("apple", "banana", "cherry", "apple", "cherry")
print(a)

a = ("apple", "banana", "cherry", "apple", "cherry")
print(len(a))



a = tuple(("apple", "banana", "cherry"))
print(a)



a = ("apple", "banana", "cherry", "apple", "cherry")
print(a[2])



a = ("apple", "banana", "cherry", "apple", "cherry")
print(a[2:6])


a = ("apple", "banana", "cherry", "apple", "cherry")
print(a[-1])



a = ("apple", "banana", "cherry", "apple", "cherry")
print(a[-1:-5:-1])



a = ("apple", "banana", "cherry", "apple", "cherry")
if "apple" in a:
    print("yes, in the tuple")

a = ("apple", "banana", "cherry", "apple", "cherry")
b=list(a)
b[2]="123"
a=tuple(b)
print(a)

a = ("apple", "banana", "cherry", "apple", "cherry")
b=list(a)
b.append("carrot")
a=tuple(b)
print(a)


a = ("apple", "banana", "cherry")
b = ("orange",)
a+= b

print(a)





x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x= tuple(y)

print(x)



a = ("apple", "banana", "cherry", "apple", "cherry")
del a
print(a)


a = ("apple", "banana", "cherry", "apple", "cherry")
(india,*japan,china)= a

print(india)
print(japan)
print(china)


a = ("apple", "banana", "cherry", "apple", "cherry")
for i in a:
    print(i)




a = ("apple", "banana", "cherry", "apple", "cherry")
for i in range(len(a)):
    print(a[i])




a= ("apple", "banana", "cherry", "apple", "cherry")
b= (1, 2, 3)
c =a+b
print(c)



a= ("apple", "banana", "cherry", "apple", "cherry")
b=a*3
print(b)

a= ("apple", "banana", "cherry", "apple", "cherry")
print(a.count("cherry"))


a= ("apple", "banana", "cherry", "apple", "cherry")
b=a.index("banana")
print(b)