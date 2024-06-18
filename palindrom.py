"""
Objective: print palindrom or not
inputs: string
outpus: 
yes, it is palindrom 
no, its not
constraints: NA
"""
def reverseString(string):
    return string[::-1]

def isPalindrome(string):
    return reverseString(string)==user_input

def isPalindrome_native(string):
    reversedString = str([i for i in reversed(string)])
    # print(reversedString)
    return reversedString==user_input
  
try:
    user_input=input("enter a string:")
    string=str(user_input)
    result=isPalindrome(string)
    if result:
        print("yes,it is palindrome")
    else:    
        print("no,its not") 
except:
    print("Invalid!Please enter valid string")


    

