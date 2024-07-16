a=(1,2,3,4,5)
b=[]
for i in a:
    b.append(i)
# print(b)

b.append(6)
b.append(7)
b.append(8)
b.append(9)
b.append(10)
a=tuple(b)
print(a)



subject=("java","java script","python")
new_subject=[]
for i in subject:
    new_subject.append(i)
# print(new_subject)
new_subject.append("c++")
new_subject.append("c")
new_subject.append("note")

subject=tuple(new_subject)
print(subject)