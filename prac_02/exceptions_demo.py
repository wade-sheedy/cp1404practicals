"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? i got a value error when i input the number in the format of a string '5'
2. When will a ZeroDivisionError occur? When a input of 0 was placed in for the denominator a ZeroDivisionError
3. instead of useing a except if i do an if statement before the program  gets to the division and some input validation occurs i can mae
"""
while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            denominator = 'Infinity'
            print("Cannot Divide by zero enter a valid denominator!!!")
        else:
            fraction = numerator / denominator
            print(fraction)
            print("Finished.")
            break
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    #except ZeroDivisionError:
        #denominator = 1 * math.pow(10, 15)
        #fraction = numerator / denominator
        #print(fraction)
        #print("Cannot divide by zero! converting to a number close to zero but not zero")

