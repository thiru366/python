# 1.Write a Python program that asks the user to input a number and prints the reciprocal of that number. Handle the exception if the user inputs zero
try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    reciprocal=f"{b}/{a}"
    
    print(reciprocal)
    

except Exception as e :
    print(e)
 



try:
    number=float(input("enter a number"))
    reciprocal=1/number
    print(f"The reciprocal of {number} is {reciprocal}")
except ZeroDivisionError:
    print("Exception: You cannot divide by zero")

try:
    number=float(input("enter a number"))
    reciprocal=1/number
    print(f"The reciprocal of {number} is {reciprocal}")
except ZeroDivisionError:
     print("Exception: You cannot divide by zero" )
except ValueError:
     print("Error:Invalid input. Please enter a numeric value")


try:
    number = int(input("Enter a number: "))
    square = number ** 2
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print(f"The square of {number} is {square}")
    print("Success: The operation completed without any errors.")





try:
    number = int(input("Enter a number: "))
    square = number ** 2
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print(f"The square of {number} is {square}")
    print("Success: The operation completed without any errors.")
finally:
    print("Ocuur")











        

















