#pattern 1
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()
         
#pattern 34
for i in range(6):
    for j in range(i):
        print("*", end='')
    print()

#pattern 2
for i in range(1,5+1):
    for j in range(1,5+1):
        j=i
        print(j,end=" ")
    print()
#pattern 35
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

#pattern 4
for i in range(5,0,-1):
    for j in range(5,0,-1):
        j=i
        print(j,end=" ")
    print()





for i in range(5,0,-1):
    for j in range(i):
        j=i
        print(j,end=" ")
    print()

for i in range(1,5):
    for j in range(5):
        print(i,end=" ")
        i=i+1
    print(i)

startnumber=1
for row in range(5):
    for col in range(5):
        print(f"{startnumber:2}",end=" ")
        startnumber+=1
    print()

for i in range(5):
    for j in range(65,71):
       print(chr(65+i),end=" ")
    print()

for i in range(5):
    for j in range(69,65,-1):
       print(chr(69-i),end=" ")
    print()
        
        