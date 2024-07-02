# #create list
# a=[1,2,3,4,5,6,7,8,9]
# mylist=["thiru","mugilan",2,3,5,6,True,False]
# print(a)
# print(mylist)

# #another method list constructor
# my_list=list(("hello","apple","mango"))
# print(my_list)

# #access the list
# a=["thiru","hari","murugan","elankavi",1,2,3]
# print(a[1])
# print(a[-2])
# print(a[1:])
# print(a[:5])
# print(a[-4:-1])


# a=["thiru","hari","murugan","elankavi",1,2,3]
# if 2 in a:
#     print("yes, in the list")


# a=[1,"thiru","murugan",2,3,4,5,6,7,8,9,10]
# a [1]=24
# print(a)


# a=["thiru","hari","murugan","elankavi",1,2,3]
# a[0:4]=["india","japan"]
# print(a)

# a=["apple","mango","orange",1,2,3,4,50]
# a[1:3]=["juice",10]
# print(a)

# a=["thiru","hari","murugan","elankavi",1,2,3]
# a.insert(2,"fire")
# print(a)


# #append method


# a=["thiru","hari","murugan","elankavi",1,2,3]
# a.append("student")
# print(a)

# #extend method


# even=[2,4,6,8,10]
# odd=[1,3,5,7,9]
# even.extend(odd)
# print(even)


# #remove mehtod
# a=["thiru","hari","murugan","elankavi",1,2,3]
# a.remove("hari")
# print(a)

# #pop method
# a=["thiru","hari","murugan","elankavi",1,2,3]
# a.pop(1)
# print(a)


# # del method used to delete the list


# my_list=["thiru","hari","murugan","elankavi",1,2,3]
# del my_list
# print(my_list)


# my_list=["thiru","hari","murugan","elankavi",1,2,3]
# del my_list[1]
# print(my_list)


# #clear method


# mylist=["thiru","hari","murugan","elankavi",1,2,3]
# mylist.clear()
# print(mylist)

# #for loop

# mylist=["thiru","hari","murugan","elankavi",1,2,3]
# for i in mylist:
#     print(i)

# my_list=["thiru","hari","murugan","elankavi",1,2,3]
# for i in range(len(my_list)):
#     print(my_list[i])

# my_list = ["china", "japan", "india"]
# [print(x) for x in my_list]


# #list compersion
# my_list=["thiru","hari","murugan","elankavi"]
# new_list=[]
# for i in my_list:
#     if "a" in i:
#         new_list.append(i)


# print(new_list)


# #sort list
# my_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# my_list.sort()
# print(my_list)


# a=[1,2,3,4,5,6,7,8,9]
# a.sort()
# print(a)




# my_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# my_list.sort(reverse=True)
# print(my_list)




# a=[1,2,3,4,5,6,7,8,9]
# a.sort(reverse=True)
# print(a)


# a = ["banana", "Orange", "Kiwi", "cherry"]
# a.sort(key = str.lower)
# print(a)
 


# my_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# my_list.reverse()
# print(my_list)


# #copy
# my_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# newlist=my_list.copy()
# print(newlist)

# my_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# newlist=list(my_list)
# print(my_list)


#join

# a=[1,2,3,4,5,6,7,8,9]
# b=["a","b","c"]
# c=a+b
# print(c)

# a = ["a", "b" , "c"]
# b= [1, 2, 3]
# for x in b:
#   a.append(x)
# print(a)



# a = ["a", "b" , "c"]
# b= [1, 2, 3]
# a.extend(b)
# print(a)