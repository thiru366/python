
# # reverse the number 
# number=126

# orginal_number=number
# rev_number=0
# while number>0:
#     digit = number % 10 
#     rev_number=rev_number*10+digit
#     number=number//10
# print(rev_number)





# #  reverse the number
# a=(input("Enter a number:"))
# b=[]
# for i in a:
#     b.append(i)
# # print(b)
# reverse_list=b[::-1]
# # print(reverse_list)

# for i in reverse_list:
#     print(i,end=" ")
# print()





# key=["a","b","c"]
# value=[1,2,3]
# output={}

# for i in range(len(key)):
#    output[key[i]]=value[i]
# print(output)


# check the given string is palindrome
string=str(input("enter a words:"))
x=string[0:5]
y=string[::-1]
for i in string.lower():
    if x!=y:
       print(i,"it is  not a palindrome")
       break 
    if x==y:
        print(i,"it is palinndrome")
        
      





# # the sum of given number
# i=1
# b=[]
# while i>0:
#     a=int(input("Enter a number:"))
#     i=i+1
#     if a>=0:
#         a=a+0
#         b.append(a)
    
#     else:
#         break
# a=0
# for i in b:
#     # print(i)
#     a=i+a
# print("The sum of given number=",a)

    



# # the product of given number
# i=1
# b=[]
# while i>0:
#     a=int(input("Enter a number:"))
#     i=i+1
#     if a>0:
#         b.append(a)
#     else:
#         break
# a=1
# for i in b:
#     print(i)
#     a=i*a
# print("The product of given number:",a)
    




# a="thirumurugan"
# b=[]
# print(a)
# for i in a:
#     print(i)
#     b.append(i)
# print(b)
# i=1
# while i>0:
#     for i in chr(96+i):
#         print(i)
#         if i=="z":
#             print(i)



a = "thirumurugan"
char_count = {}

for char in a:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
