"""
print leap year or not
inputs: number
outputs:
leap year
not a leap year
"""

def is_leap_year_or(year):
    if not  year % 4 == 0:  #if the year is divisible by 4 and not divisible by 100 then they are leap years
        return False
    if not year % 100 == 0:
        return True

    if year % 400 == 0: #century years are leap years only if they are divisible by 400
        return True
    else:
        return False

def is_leap_year(year):
    if not  year % 4 == 0:  #if the year is divisible by 4 and not divisible by 100 then they are leap years
        return False
    if not year % 100 == 0:
        return True

    return year % 400 == 0 #century years are leap years only if they are divisible by 400


try:
    user_input = input("Enter a year: ")
    year = int(user_input) 

    if not year > 0:
        print("Please enter a valid year!")
    else:
        if is_leap_year(year):
            print(f"leap year")
        else:
            print(f"not a leap year")
except ValueError:
    print("Please enter only a number!") 