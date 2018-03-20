"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    Total_Income_Earned_Over_Time = []
    Period_of_time_worked = int(input("How many months? "))

    for month in range(1, Period_of_time_worked + 1):
        income = float(input("Enter income for month {} : ".format(str)))
        Total_Income_Earned_Over_Time.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, Period_of_time_worked + 1):
        income = Total_Income_Earned_Over_Time[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
