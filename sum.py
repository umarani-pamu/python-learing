"""
print sum of all numbers given
inputs: numbers
outputs:
number as sum
"""

def sum_of_numbers(inputs):
    sum = 0
    for i in inputs:
        sum += i
    return sum

input_message= input("Enter numbers separated by spaces: ")

"""Firstly, the input message will be splited 
eg: input_message=1 2 3 4 5
    by using split() function the input_message will be converted as ["1","2","3","4","5"]

secondly, map(int, ['1', '2', '3', '4', '5']) will convert each element to an integer,
 resulting to map object 1, 2, 3, 4, 5

thirdly,list(map(int, ['1', '2', '3', '4', '5'])) will convert the map object to the list [1, 2, 3, 4, 5]
"""
try:
    input_list = list(map(int, input_message.split()))
    result = sum_of_numbers(input_list)
    print("The sum of all given numbers: ", result)
except ValueError:
    print("Please enter only numbers!!")