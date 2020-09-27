import os
import csv

csvpath = os.path.join('Resources', '.gitignore', 'budget_data.csv')

with open(csvpath) as budget:
    csvreader=csv.reader(budget, delimiter=',')

    #Skip Header for row count
    csv_header = next(csvreader)

    #Total number of months 
    months = len(list(csvreader))







    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months: ", str(months))
    print(f"Total: ", "$")
    print(f"Average Change: ", "$")
    print(f"Greatest Increase in Profits: ")
    print(f"Greatest Decrese in Profits: ")

    



