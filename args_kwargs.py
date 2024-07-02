#1: Sum of all arguments

def num(*a):
    sum=0
    for i in a:
       sum=sum+i
    print("The sum of all",sum)
        
num(1,2,3,4,5,6)


# 2: Multiply all arguments

def num(*a):
    mul=1
    for i in a:
        mul=mul*i
    print("the mutiple of number",mul) 
num(10,19,14)



# 3: Con ll arguments

def name(*names):
    print("python couse"+ ' ' + names[2])
    
    
name("thiru","mugilan","hari")
    



def course(**name):
    print(name["python"])
course(python="thiru",java="hari",c="mugilan")

