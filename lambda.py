# lambda

# Add Two Numbers


def first_num(a):
    return lambda b : a+b
sec_num=first_num(13)
print(sec_num(2))


# 2.Find the Maximum of Two Numbers

def first_num(a):
    return lambda b : max(a,b)
sec_num=first_num(13)
print(sec_num(28))


# 3.Square a Number

x=lambda a: a*a
print(x(a=4)) 


# 4.Reverse a String

x=lambda name:name[::-1]
print(x(name="mugilan"))



# 5.Check if a Number is Even
x=lambda a:f"{a} is even" if a%2==0 else f"{a}is odd number"
print(x(a=6))