def name():
    name="hari"
    print(name)
name()



def number(a,b):
    c=a+b
    print(c)
number(1,2)


def number(a,b):
    c=a+b
    return c
print(number(1,10))



#global

a=10
def number():
    a=4
    print(a,"local")
number()
print(a,"global")

#check even number

def even(a):
    if a%2==0:
        print(a,"even number")
    else:
        print(a,"not  a even number")
even(16)



#check odd number

def odd(a):
    if a%2==1:
        print(a,"odd number")
    else:
        print(a,"not  a odd number")
odd(15)




#sum of two number

def sum():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    return a+b
print((sum()))


#factorial number


def factorial(a):
    b=1
    for i in range(1,a+1):

       b=b*i
       if i==a:
         print(b,"is the factorial of ",a)
        
factorial(5)

#check prime or not

a=int(input("Enter  a number:"))
def prime():
    if (a==2 or a==3):
        print(a,"prime number")
    elif (a%2==0 or a%3==0):
        print(a,"not a prime nnumber")
    else:
        print(a,"prime number")

prime()



#maximum in a list

def maximum(maximum_1):
    x=max(maximum_1)
    return x
a=[1,4,6,8,93,999,8847]
maxi=maximum(a)
print(f"the maximum in a list: {maxi}")


# reverse a sting
def rev():
    a=str(input("Enter a string:"))
    b=a[::-1]
    print(b)
rev()




# palindrome

def palin():
    a=str(input("Enter a string:"))
    x=a[0:]
    y=a[::-1]
    if x==y:
        print(a,"Its is palindrome")
    else:
        print(a,"Its is not palindrome")
palin()



# fibonacci

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
for i in range(n):
    print(fibonacci(i))


def vowels(string):
    vowels = "aeiouAEIOU"  
    count = 0 

    for char in string:
        if char in vowels:
            count += 1  

    return count
input_string = input("Enter a words:")
vowel_count = vowels(input_string)
print(f"The number of vowels in the string is: {vowel_count}")

# list length
def length(list_1):
    print(list_1)
    count=len(list_1)
    return count
    
    
a=[1,2,3,4,5,7,88,785,89839,8893489]
b=length(a)
print(f"the list length is {b}")


#list sort
def sort(sort1):
     sort1.sort()
     return sort1
    

a=[1,3,4,5,6,7,8,545,545,4,54654,6546,54,654,654,654,6,545,654]
count_1=sort(a)
print(f"Given list is sort {count_1}")



