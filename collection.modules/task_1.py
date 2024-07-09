import collections

#counter
d=["a","b","c","a","b","c"]
c=collections.Counter(d)
print(c)


#order.dict
d={}
d["a"]=1
d["b"]=2
d["c"]=3
for i,j in d.items():
    print(i,j)
d.pop("a")
print(d)


d["a"]=1
print(d)



d=collections.defaultdict(list)
for i in range(5):
    d[i].append(i)



print(d)




#chainmap


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}


c=collections.ChainMap(d1,d2,d3)
print(c)



#named tuple

student=collections.namedtuple("student",["name","age","DOB"])



s=student("thiru",18,"17.03.2007")
print(s[1])
print(s[0])
print(s[2])

# deque
a=collections.deque(["name","age","dob"])
a.pop()
print(a)

a.popleft()
print(a)




