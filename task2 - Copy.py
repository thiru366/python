#positive number
# x=int(input("Enter a number:"))
# if x>0:
#     print(x,"Given number is positive")
# elif x==0:
#     print(x,"Given number is zero")
# else:
#     print(x,"Given num be is negative") 


# # even number
# a=int(input("Enter a number:"))
# if a%2==0:
#     print ("Given numberr is even number")
# else:
#     print("Given number is odd number")



#divided by 5

# b=int(input("Enter a number:"))
# if b%5==0:
#     print("divided by 5")
# else:
#     print("not divided by 5")



# n1=int(input("Enter a first number:"))
# n2=int(input("Enter a second number "))
# if n1>n2:
#     print("the first number is larger")
# elif n1<n2:
#     print("The second number is larger")
# else:
#     print("the numer are equal")


# #string contain specific substring
# a=str(input("Enter the sentence:"))
# print ('welcome' in a)

# #1 to 10
# a=int(input("Enter a number:"))
# if a<=10:
#     print("number is between 1 to 10")
# else:
#     print("Number is not between 1 to 10")




# # vowel letter

# str=str(input("Enter the character"))
# string='a','e','i','o,u'
# print(str in string)


# a=int(input("Enter your age:"))
# if a>=18:
#     print("your are eligible for vote")
# else:
#     print("your are not eligible for vote")
     
#leap year
# a=int(input("Enter a year:"))
# if (a%4==0 and a%100!=0) or (a%400==0):
#     print("this year is leap year")
# else:
#     print("this year is not leap year")


# # #teenager
# a=int(input("Enter your age:"))
# if a<=19 and a>=13:
#     print("your are teenager ")
# else:
#     print("your are not teenager")


# #vowel
# s=str(input("enter a letter:"))
# if s=='a' or s=='e' or s=='i' or s=='o' or s=='u' :
#     print(" given letterr is vowel")
# else:
#     print("Given letter is not vowel") 

#mutiple of 3 and 7
a=int(input("Enter a number:"))
if a%3==0 :
    if a%7==0 and a%3==0:
        print("Both are divisible by 3 and 7")
    else :
        print("divisible by 3 only")

else:
    print("divisible by 7 only")
