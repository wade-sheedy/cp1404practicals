def main():
    """Also added in comments into each step to practice with my comments"""
    incomes = []
    months = int(input("How many months? "))#amount of months we want to calculate total income for

    for month in range(1, months + 1): # for loop to gain income for each month for the number of months
        income=float(input("enter income for month " + str (month) + ": "))# gains a income value for each month
        incomes.append(income)# appends the incomes list for the monthly incomes

    print("/n Income Report' /n ------------")
    total = 0 #total incomes starts at zero
    for month in range(1, months + 1):# starts at zero incomes and adds on the incomes for each month for the total number of months
        income = incomes[month-1]#reduces month by 1
        total += income # increases my total income by the value of the income
        print(" Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))# Prints each months income to the screen and then the total income

main()
