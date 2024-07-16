# my_list=[1,2,4,6,9,11,13,15,17,18,20,22,24,26,28,30,34,55]
# even=[]
# odd=[]
# for i in my_list:
#     if i%2==0:
        
#         even.append(i)
#     else:
     
#         odd.append(i)
# print("Even",even)
# print("odd",odd)


# my_list=[1,2,3,4,5,6,7,8,9,10]
# num=0
# for i in my_list:
#     num=num+i
# print(num)



# my_list=[1,2,3,4,5,0,6,7,8]
# num=1
# for i in my_list:
#     if i==0:
#         continue
#     else:
#         num=num*i
# print(num)

# number=[2,3,4,5,96,1,7,8,9]
# larger_number=max(number)
# print(larger_number)


a=[1,2,3,4,5,6-6,-7,-8,-9]
b=[]
for i in a:
    if i<0:
        b.append(i)
print(b)


number=[2,3,4,5,96,1,7,8,9]
larger_number=min(number)
print(larger_number)


a=[1,2,3,4,5,6,7,8,9,10]
reverse=a[::-1]
print(reverse)



number=[2,3,4,5,96,1,7,8,9]
large_num=number[0]
for num in number:
    if num > large_num:
        large_num=num
print("the large number is",large_num)




number=[2,3,4,5,96,1,7,8,9]
large_num=number[0]
for num in number:
    if num < large_num:
        large_num=num
print(large_num)


