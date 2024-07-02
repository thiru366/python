# #1.Print numbers 1 to 10
# for i in range(1,11):
#     print(i)


# #2.Print the square of each number from 1 to 10
# for i in range(1,11):
#     print(i*i)


# #3.Print each character in a string
# a=input("Enter a sring:")
# for i in  a:
#     print(i)


# #4.Sum of numbers from 1 to 10
# sum=0
# for i in range(1,10+1):
#     sum=sum+i
# print(sum)

# #5.Print each element in a list
# a = [1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     print(i)


# #6.Print numbers from 10 to 1 (reverse order)
# for i in range(10,0,-1):
#     print(i)

# #7.Print only even numbers from 10 to 20
# for i in range(10,21):
#     if i%2==0:
#         print(i,"is even number")
#     else:
#         print(i,"is odd number")


# #8.Print the multiples of 5 between 20 to 50 .
# for i in range(20,51):
#     if i%5==0:
#         print(i,"divisible by 5")
#     else:
#         print(i,"not divisible by 5")

# #9.Print the factorial of a number (e.g., 5!)
# a= int(input("Enter a number:"))
# b=1
# for i in range(1,a+ 1):
#     b*= i
# print("factorial of",b)

# #10.Print numbers from a list that are greater than 10
# a=[34,1,5,8,9,2,25,67,89,67,89]
# for i in a:
#     if i>10:
#         print(i,"The number greater than 10")
 

# #11.Print all prime numbers between 10 and 20
# for i in range(1,15):
#     if   (i==2  or i==3 ):
#         print(i,"prime number")
#     elif(i%2==0 or i%3==0):
#         print(i," not prime number")
#     else:
#         print(i,"prime number")


# #12.Find the largest number in list
# number=[2,3,4,5,6,7,8,9]
# larger_number=number[0]
# for num in number:
#     if num > larger_number:
#         larger_number=num
# print(num,"larger number")


# #count the number of vowels in a str:
# str="thIrU"
# for name in str.lower():
#     if name=='a' or name=='e' or name=='i' or name=='o' or name=='u':
#         print(name,"the vowel leter")
#     else:
#          print(name,"not a vowel letter")



# #print even number  from 10 to 20:
# for i in range(10,21):
#     if i%2==0:
#         print(i,"is the even number")
#     else:
#         print(i,"is not even number")

    
# #print  the product 0f 1to5
# product=1
# for i in range(1,6):
#     product=product*i
# print(product,"product of 1 to 5")