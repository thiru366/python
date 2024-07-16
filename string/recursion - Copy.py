# recursion
# print 1 to 10


def num(n):
    if n!=0:
        num(n-1)
        print(n)

num(10)




# print 10 to 1

def num(n):
    if n!=0:
        print(n)
        num(n-1)
    


num(10)




#factorial number

def number():
    global num


    a=[]

    while num>=1:
        
        a.append(num)
        num=num-1
    fact=1
    for i in a:
        fact=fact*i
    print("the  factorial of given number  is:",fact)

    
num=int(input("Enter a number:"))

if num==0 or num<0:
    print("invalid number please enter positive number")
elif num==1:
    print(num)
elif num>0:
    print(number())









def sum_list(index):
    
    if len(index) == 0:
        return 0
    else:
        return index[0] + sum_list(index[1:])
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list)) 
 




# #fibonacci 

# def fibonacci(n):
#     if(n <= 1):
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
# n = int(input("Enter number of terms:"))
# for i in range(n):
#     print(fibonacci(i))




# # reverse the string

# def  str(n):
#     if len(n)==0:
#         return n
#     else:
#         return n[-1] +  str(n[:-1])



