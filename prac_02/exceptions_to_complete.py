"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
number = 0
while not finished:
    try:
        number = int(input ("please enter a number: "))
        result = number + result
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
    #number = int(input("please enter a number: ")) commented out because was having an issue where if you entered in a second invalid integar the porgram would crash 
print("Valid result is:", result)
