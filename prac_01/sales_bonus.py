"""Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If Sales are $1000 or over the bonus is 15%"""

sales = float(input("Enter Sales:$ "))
###print(sales)- test statement for sales input
if sales < 1000:
    bonus = sales * 0.1
    print(bonus)
elif sales >= 1000:
        bonus = sales * 0.15
        print(bonus)
