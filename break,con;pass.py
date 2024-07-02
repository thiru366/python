#Print numbers from 1 to 10, but stop when the number is 5
for i in range(1,11):
    if i==5:
        break
    else:
        print(i)

#Find the first negative number in a list.
a=[1,2,3,4,5,-9,-6,6]
for i in (a):
        if i<0:
                break           
print(i)
       

#3.Iterate over a list and stop if you encounter a zero.
a=[1,22,3,44,55,0,77,88]
for i in a:
    if i==0:
        break
    else:
        print(i)

#Print numbers from 1 to 10, skipping 5
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i)

#5.Print only even numbers from 1 to 10. 
for i in range(1,11):
    if i%2==0:
        print(i)
    else:
        pass


#6. Iterate over a list and skip negative numbers.
a=[1,2,44,55,-9,-5,6,7,-445]
for i in a:
    if i<0:
        continue
        pass
    else:
        print(i)
 
#7. Print characters of a string, skipping vowels.
str="welcome to python"
vowel='a','e','i','o','u'
for i in str:
    if i in vowel:
        continue
    else:
        print(i)


#8.Iterate over numbers from 1 to 20, but skip multiples of 3
for i in range(1,21):
    if i%3==0:
        continue
    else:
        print(i)

#Iterate over a list and use pass for future implementation.
for i in range(10):
    pass
    print(i)

#Iterate over numbers from 1 to 10, skip 5 and stop at 8
for i in range(1,10):
    if i==5:
        continue
    elif i==8:
        print(i)
        break
    else:
        print(i)

#11.Print only odd numbers from 1 to 10, but use pass for even number
for i in  range(1,11):
    if i%2==0:
        pass
    else:
        print(i)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
midpoint = len(num) // 2
for i in range(midpoint, len(num)):
    pass
    print(num[i])
