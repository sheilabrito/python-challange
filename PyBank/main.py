import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
Financial_Report = os.path.join("Analysis", "Financial_Report.txt")

months = 1
profits = 0
changes = []
date = []
highest = ["",0]
lowest = ["",999999999999999]

with open(budget_data) as finance:
    reader = csv.reader(finance, delimiter=',')
    titles = next(reader)
    numbers = next(reader)
    profits += int(numbers[1])
    xone = int(numbers[1])
    for row in reader:
        months += 1
        profits += int(row[1])
        change = int(row[1]) - xone
        xone = int(row[1])
        changes += [change]
        date += [row[0]]
        if change > highest[1]:
            highest[0] = row[0]
            highest[1] = change
        if change < lowest[1]:
            lowest[0] = row[0]
            lowest[1] = change


average = sum(changes) / (int(months) - 1)

report = (
f"Financial Analysis\n"
f"---------------------------\n"
f"Total Months = {months}\n"
f'Total: $ {profits} \n'
f"Average Change = {average:.2f}\n"
f'Greatest Increase = {highest[0]} - $ {highest[1]}\n'
f'Greatest Decrease = {lowest[0]} - $ {lowest[1]}\n'
)

print(report)

with open(Financial_Report, 'w') as txt_file:
    txt_file.write(report)