"""
print sum upto nth natural numbers
inputs: integer or number as n
outputs:
number as sum

"""  

def sum_naturals(number):
    return number * (number + 1) // 2

try:
    user_input = input("Enter an integer: ")  
    number = int(user_input) 
    result_sum = sum_naturals(number)  
    print(result_sum)  
except ValueError:  
    print("Invalid input!!")
