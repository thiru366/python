# emp1={"name":"thirumurugan",
#       "age":29,
#       "city":"puducherry",
#       "skill":"python"
#       }
# emp2={"name":"hari",
#       "age":28,
#       "city":"chennai",
#       "skill":"c++"}
# emp3={"name":"mukilan",
#       "age":30,
#       "city":"chennai",
#       "skill":"python"}
# empolyee={
# "emp1":emp1,
# "emp2":emp2,
# "emp3":emp3
# }

# print(empolyee)

# print(empolyee["emp1"]["skill"])


# for i,j in empolyee.items():
#     print(i) 
#     for y in j:
#         print(y + ":" , j[y])





# emp1={"name":"thirumurugan",
#       "age":29,
#       "city":"puducherry",
#       "skill":"python"
#       }
# emp2={"name":"hari",
#       "age":28,
#       "city":"chennai",
#       "skill":"c++"}
# emp3={"name":"mukilan",
#       "age":30,
#       "city":"chennai",
#       "skill":"python"}

# empolyee={
# "emp1":emp1,
# "emp2":emp2,
# "emp3":emp3
# }

# #clear method
# empolyee.clear()
# print(empolyee)
# #copy method
# x=empolyee.copy()
# print(x)

# name={"thiru","mukilan","hari"}
# skill="Python"
# detail=dict.fromkeys(name,skill)
# print(detail)

# # get method


# emp1={"name":"thirumurugan",
#       "age":29,
#       "city":"puducherry",
#       "skill":"python"
#       }
# x=emp1.get("age")
# print(x)


# emp1={"name":"thirumurugan",
#       "age":29,
#       "city":"puducherry",
#       "skill":"python"
#       }
# x=emp1.items()
# print(x)


# emp1={"name":"thirumurugan",
#       "age":29,
#       "city":"puducherry",
#       "skill":"python"
#       }
# # x=emp1.keys()
# # print(x)
# emp1.pop("age")
# print(emp1)

# # pop item
# emp3={"name":"mukilan",
#       "age":30,
#       "city":"chennai",
#       "skill":"python"}
# emp3.popitem()
# print(emp3)


# # setdefault

# emp3={"name":"mukilan",
#       "age":30,
#       "city":"chennai",
#       "skill":"python"}
# emp3.setdefault("company","IT")
# print(emp3)
# emp3.setdefault("age",39)




# emp2={"name":"hari",
#       "age":28,
#       "city":"chennai",
#       "skill":"c++"}
# emp2.update({"company":"IT"})
# print(emp2)



# emp2={"name":"hari",
#       "age":28,
#       "city":"chennai",
#       "skill":"c++"}

# x=emp2.values()
# print(x)