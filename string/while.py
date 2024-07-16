# # #1.Print numbers 1 to 10
# # i=1
# # while i<11:
# #     print(i)
# #     i=i+1

# # #2.Print the square of each number from 1 to 10
# # i=1
# # while i<11:
# #     print(i*i)
# #     i=i+1

# # #3.Print each character in a s/
# # sum=0
# # i=1
# # while i<=10:
# #     sum=sum+i
# #     i=i+1
# # print("the sum of 1 to 5 is",sum)

# # #6.Print numbers from 10 to 1 (reverse order)
# # i=10
# # while i>=1:
# #     print(i)
# #     i=i-1

# # #5.Print each element in a list
# # a=[1,2,3,4,5,6]
# # i=0
# # while i<len(a):
# #     print(a[i])
# #     i=i+1
    
# #print only even number
# i=10
# while i<21:
#     print(i ,"is the even number")
#     i=i+2

# #multiple of 5
# i=20
# while i<=50:
#     print(i)
#     i=i+5

# #9.Print the factorial of a number (e.g., 5!)
# a = 5
# b = 1
# n = a
# while n > 1:
#     b =b*n
#     n =n-1
# print(b,"is the factorial of ",a)


# 10.Print numbers from a list that are greater than 10
# a=[24,55,68,7,8,9]
# index=0
# while index<len(a):
#     if a[index]>10:
#         print(a[index])
#     index=index+1

  
# #11.Print all prime numbers between 10 and 20
# num = 10
# while num <= 20:
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
#    num += 1


# #12.Find the largest number in list
# numbers = [10, 5, 20, 15, 8, 25]
# largest = numbers[0]
# index = 0

# while index < len(numbers):
#    if numbers[index] > largest:
#        largest = numbers[index]
#    index += 1

# print("The largest number is:", largest)


#13.vowels in a string
name="thirumurugan"
vowels="i" or "e" or "i" or  "o" or "u"
index=0
while index<len(name):
    if name[index]=="a":
        print(name[index],"its the vowel")
    elif name[index]=="e":
         print(name[index],"its the vowel") 
    elif name[index]=="i":
         print(name[index],"its the vowel")
    elif name[index]=="u":
         print(name[index],"its the vowel")
    elif name[index]=="o":
          print(name[index],"its the vowel")
         
          index=index+1


#even numbers from 10 to 20:
	
num = 10

while num <= 20:
   if num % 2 == 0:
       print(num)
   num += 1


#product from 1 to 5:
	
product = 1
num = 1

while num<= 5:
   product *= num
   num+= 1

print("Product from 1 to 5 is:", product)