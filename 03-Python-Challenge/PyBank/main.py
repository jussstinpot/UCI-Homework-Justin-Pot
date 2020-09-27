import os
import csv

csvpath = os.path.join("..", "..", "..", 'budget_data.csv')

#Set each variable to 0
total_months = []
total_net = []
average_change= []

with open(csvpath) as budget:

    csvreader=csv.reader(budget, delimiter=',')

    #Skip Header for row count
    csv_header = next(csvreader)
    
    for row in csv.reader(budget):
      
      # append the total months and total profit to their corresponding lists
      total_months.append(row[0])
      total_net.append(int(row[1]))
    
    for i in range(len(total_net)-1):
        average_change.append(total_net[i+1]-total_net[i])

greatest_increase = max(average_change)
greatest_decrease = min(average_change)

increase_month = average_change.index(max(average_change)) + 1
decrease_month = average_change.index(min(average_change)) + 1

print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total:$ {sum(total_net)}")
print(f"Average Change:${round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrese in Profits: {total_months[decrease_month]} (${(str(greatest_decrease))})")



