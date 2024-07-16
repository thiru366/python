a='python'
b="java"
c='''thankyou'''
print(a,b,c)


# slicing
a="thirumurugan"
print(a[0:5])
print(a[-7:])


##center
a="python"
print(a.center(100))

#format
age=17
a = f"My name is thirumurugan ,I am {age} "
print(a)

#escape
text = "Hello\nWorld"
print(text)

a="we are the \"student\"of ocean academy"
print(a)

#capitalize()	Converts the first character to upper case
a=input("Enter a name:")
print(a.capitalize())

#casefold()	Converts string into lower case
a="welcome TO PYTHON"
print(a.casefold())

#count()	Returns the number of times a specified value occurs in a string
a="I love apples, apple are my favorite fruit"
x=a.count("apple")
print(x)


#endswith()	Returns true if the string ends with the specified value
a=input("Enter your gmail account:")
print(a.endswith("gmail.com"))

#expandtabs()	Sets the tab size of the string
a= "t\th\ti\tr\tu"
print(a.expandtabs(5))
 

#find()	Searches the string for a specified value and returns the position of where it was found
a="Hello,welcome to python"
print(a.find("welcome"))


#index()	Searches the string for a specified value and returns the position of where it was found
a="welcome to python,it is a programme language"
print(a.index("is"))

#lower()	Converts a string into lower case
a="THIRUmurugan"
print(a.lower())

#upper()	Converts a string into upper case
a="thiruMURUGAN"
print(a.upper())

#title()	Converts the first character of each word to upper case
a="welcome to python to study programme language"
print(a.title())


#swapcase()	Swaps cases, lower case becomes upper case and vice versa
a="welcome to python to study programme language"
print(a.swapcase())


name = ["John", "Peter", "Vicky"]
x = ",".join(name)
print(x)

a="python"
x=a.zfill(10)
print(x)