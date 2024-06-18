"""
print yes or no if a number is even or odd resp.,
inputs: number
outputs: 
even
odd
"""

def EvenOdd(number):
    if (number % 2) == 0:
        print("The given number is even")
        return True
    else:
        print("The given number is odd")
        return False

user_input = input("Enter the input: ")

try:
    number = int(user_input)  
    result = EvenOdd(number) 
    print(result)  
except ValueError:
    print("Please enter only integer numbers!!")





# move to fun to return Treu or False and call then print result
# validate inputs