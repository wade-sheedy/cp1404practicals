"""
Prac 3 Task 2
"""

MENU = """ C- Convert Celsius to Farenheit
F - Convert Farenheit To Celsius
Q - Quit """

def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            out_put = convert_to_fahrenheit(float(input("Celsius: ")))
            print("Result: {:.2f} F".format(out_put))
        elif choice == "F":
            out_put = convert_to_celsius(float(input('Fahrenheit: ')))
            print("Result: {:.2f} C".format(out_put))
        else:
            print("invalid selection")
        print(MENU)
        choice =input(">>> ").upper()

    print ("Thank You")

def convert_to_fahrenheit(celsisus):
    fahrenheit = celsisus * 9.0 / 5 + 32
    return fahrenheit

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)* 5 / 9
    return celsius


main()
