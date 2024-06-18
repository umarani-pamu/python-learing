"""
print leap year or not
inputs: number
outputs:
leap year
not a leap year
"""
def is_leap_year(year):
    if year % 4 == 0:  #if the year is divisible by 4 and not divisible by 100 then they are leap years
        if year % 100 == 0:
            if year % 400 == 0: #century years are leap years only if they are divisible by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False



try:
    user_input = input("Enter a year: ")
    year = int(user_input) 
    if year > 0:
        if is_leap_year(year):
            print(f"leap year")
        else:
            print(f"not a leap year")
    else:
        print("Please enter a valid year!")
except ValueError:
    print("Please enter only a number!") 