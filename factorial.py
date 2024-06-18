"""
objtive: print factorial of a number
inputs: number
outputs: 
factorial of a number
example: for 3 as input; 
print result for 3*2*1*0! as 6
"""

def find_factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * find_factorial(number - 1)
    
try:
    user_input=input("enter a number:")
    number=int(user_input)
    if number < 0:
        print("enter valid number starts with 0!")
    else:
        factorial=find_factorial(number)
        print(factorial)
except ValueError:    
    print("Invalid input!!")
    
