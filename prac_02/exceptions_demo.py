"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? i got a value error when i input the number in the format of a string '5'
2. When will a ZeroDivisionError occur? When a input of 0 was placed in for the denominator a ZeroDivisionError
3. Could you change the code to avoid the possibility of a ZeroDivisionError? using the logic of limits so that if x = 0 we can make x infinatly smaller
        #  so it gets close to 0 but it never reaches 0
        # 10^-15 is very close to zero but it is not yet zero
"""
import math
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        denominator = 'Infinity'
        print("The fraction has reached a limit and the denominator has reached a limit and has achieved {} ".format(denominator))
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
#except ZeroDivisionError:
    #denominator = 1 * math.pow(10, 15)
    #fraction = numerator / denominator
    #print(fraction)
    #print("Cannot divide by zero! converting to a number close to zero but not zero")
print("Finished.")
