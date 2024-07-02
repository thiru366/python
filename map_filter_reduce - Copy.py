# #1.Square all numbers in a list


# def square(n):
#     return n**2
# num=[1,2,3,4,5,6,7,8,9]
# res=map(square,num)
# print(list(res))



 
# #  Convert all strings in a list to uppercase

# def string(n):
#     return n.upper()
# list_1=["thiru","hari","mugilan"]
# res=map(string,list_1)
# print(list(res))


# # 3.Add 10 to each number in a list

# def  add(n):
#     return n+10
# list_1=[1,2,3,4,5,6,7,8,9]
# res=map(add,list_1)
# print(list(res))



# # Double each number in a list

# def double(n):
#     return n**2
# list_1=[2,4,7,8,4,3]
# res=map(double,list_1)
# print(list(res))





# #Capitalize the first letter of each string in a list

# def cap(n):
#     return n.capitalize()
# list_1=["thiru","hari","mugilan"]
# res=map(cap,list_1)
# print(list(res))



# # 6.Filter out even numbers from a list

# def even(n):
#     return n%2==0
# list_1=[1,4,7,9,8,90,784,6,9,10,89]
# res=filter(even,list_1)
# print(list(res))



# # 7.Filter out words shorter than 4 characters
 
# def character(n):
#     return len(n)<4
# sentence=["thiru","hari","c++","java","mugilan"]
# res=filter(character,sentence)
# print(list(res))



# # 8.Filter out numbers greater than 10
# def greater(n):
#     return n>10


# list_1=[1,4,78,9,49,56,89,76,56]
# res=filter(greater,list_1)
# print(list(res))



# # 9.Filter out strings containing the letter 'a'
# def  filters(n):
#     return "a" in n
# list_1=["thiru","hari","c++","java","mugilan"]
# res=filter(filters,list_1)
# print(list(res))


# # Filter out numbers that are not divisible by 3

# def not_divisi(n):
#     return n%3!=0


# list_1=[1,4,78,9,49,56,3,6,21,89,76,56]
# res=filter(not_divisi,list_1)
# print(list(res))



# #11.Filter out negative numbers from a list

# def num(n):
#     return n<0
# list_1=[1,4,6,8,-3,-7,-5,-7,-4]
# res=filter(num,list_1)
# print(list(res))



# # Filter out numbers that are not divisible by 3

# def not_divisi(n):
#     return n%3!=0


# list_1=[1,4,78,9,49,56,3,6,21,89,76,56]
# res=filter(not_divisi,list_1)
# print(list(res))


# # Find the product of all numbers in a list


# import functools


# list_1=[1,4,7,8,9,6]
# res=functools.reduce(lambda x,y:x*y,list_1)
# print("the product of all numbers in a list:",res)



# # 14.Concatenate a list of strings

# import functools

# list_1=["c++","python","java","c"]
# res=functools.reduce(lambda x,y:x+y,list_1)
# print("Concatenate a list of strings:",res)




# # 15.Find the maximum number in a list
# import functools

# list_1=[3,56,79,190,57,578]
# res=functools.reduce(lambda x,y:x if x>y else y,list_1)
# print("Concatenate a list of strings:",res)


# # 16.Compute the sum of squares of numbers in a list
# import functools

# list_1=[1,2,3,4,5]
# res=functools.reduce(lambda x,y:x+y**2,list_1)

# print("Concatenate a list of strings:",res)



#17.Compute the factorial of a number using reduce

import functools

def fact(n):
    global x
    x= functools.reduce(lambda x,y:x*y,range(1,n+1),1)
num=5
res=fact(num)
print("factorial of a number ",x)