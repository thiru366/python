# def fibonacci(n):
#     if(n <= 1):
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
# n = int(input("Enter number of terms:"))
# for i in range(n):
#     print(fibonacci(i))





# def is_armstrong_number(number):
#     num_str = str(number)
#     num_length = len(num_str)
#     sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
#     return sum_of_powers == number
# test_number = 153
# if is_armstrong_number(test_number):
#     print(f"{test_number} is an Armstrong number.")
# else:
#     print(f"{test_number} is not an Armstrong number.")




# def is_harshad_number(number):
    
#     num_str = str(number)
    
    
#     sum_of_digits = sum(int(digit) for digit in num_str)
    
#     return number % sum_of_digits == 0

# test_number = 18
# if is_harshad_number(test_number):
#     print(f"{test_number} is a Harshad number.")
# else:
#     print(f"{test_number} is not a Harshad number.")




def is_automorphic_number(n):
    return str(n*n).endswith(str(n))

# Example usage
number = 76
if is_automorphic_number(number):
    print(f"{number} is an Automorphic number")
else:
    print(f"{number} is not an Automorphic number")