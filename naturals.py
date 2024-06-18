"""
print n natural numbers
inputs: integer or number as n
outputs:
all natural numbers till give input n

"""
      
def natural_numbers(number):
   numbers = []  
   if number>0:
        for i in range(1, number + 1):  
            numbers.append(i)  
   if number<0:
        for i in range(-1, number - 1,-1):  
            numbers.append(i)  
   if number==0:
       return [0]        
   return numbers
    
user_input = input("Enter the number till how many natural numbers you require (positive or negative): ")

try:
    number = int(user_input) 
    result = natural_numbers(number) 
    print("The natural numbers are:", result)  
except ValueError:
    print("Invalid input !! Please enter only a number.") 


