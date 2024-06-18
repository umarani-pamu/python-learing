"""
print n natural numbers
inputs: integer or number as n
outputs:
all natural numbers till give input n

"""
      
"""
def natural_numbers(number):
    numbers = []  
    for i in range(1, number + 1):  
        numbers.append(i)  
       
    return numbers
    """

def natural_numbers(number):
    return list(range(1, number + 1))

try:
    user_input = input("Enter the number till how many natural numbers you require : ")
    number = int(user_input)
    if number<=0:
        print("please enter valid natural number starts with 1.")

    else:    
       result = natural_numbers(number) 
       print("The natural numbers are:", result)  
except ValueError:
    print("Invalid input !! Please enter only a number.") 


      
