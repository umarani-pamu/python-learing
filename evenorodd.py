"""
print yes or no if a number is even or odd resp.,
inputs: number
outputs: 
even
odd
"""

"""
def isEven(number):
    if (number % 2) == 0:
        print("The given number is even")
        return True
    else:
        print("The given number is odd")
        return False
"""

def isEven(number):
    return (number % 2) == 0    

user_input = input("Enter the input: ")

try:
    number = int(user_input)  
    result = isEven(number) 

    # do application logic
    if result:
        print("even")
    else:
        print("odd")
except ValueError:
    print("please enter a valid input!!")

