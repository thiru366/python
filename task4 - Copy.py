#nested if
a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
c=int(input("Enter a third number:"))
if a >b:
    if a>c:
        print("first number is a larger")
    else:
        print("second numberis larger")
else:
    if c>a and c>b:
              print("third number is the larger")

#divisible by  5 and 11
a=int(input("Enter a  number:"))
if a%5==0:
    if a%11==0:
        print("divisible by 5 and 11")
    else:
        print("divisible by 5")
else:
    print("divisible by 11")

#3.Check if a number lies in the range 10-50.      
a=int(input("Enter a number:"))
if a>=10:
    if a<=50:
        print("between 10 to 50 ")
    else:
        print("the number is not between 10 to 50")
else:
    print("the number is not between 10 to 50")



#leap year
a=int(input("Enter a year:"))
if ( a%4==0 and a%100!=0 or a%400==0):
    if (a%4==0 and a%100!=0):
         print("this year is leap year")
else:
    print("this year is not leap year")

# even number and positive
a=20
if a%2==0 :
    if a>0:
        print ("Given numberr is even number and positive")
    else:
        print("Given number is even")
else:
    print("Given number is zero or negavtive")



