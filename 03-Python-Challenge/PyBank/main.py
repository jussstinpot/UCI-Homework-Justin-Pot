import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

print("Financial Analysis")
print("-------------------")

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    months = len(list(csvreader))

    print(f"Total Months: " + str(months))