import os
import csv

csvpath = os.path.join("..", "..", "..", 'budget_data.csv')

#Give each variable a list 
total_months = []
total_net = []
average_change= []

#Open csv file
with open(csvpath) as budget:

    csvreader=csv.reader(budget, delimiter=',')

    #Skip Header for row count
    csv_header = next(csvreader)
    
    #Read csv file by row
    for row in csv.reader(budget):
      
      #append total months to correct list
      total_months.append(row[0])
      #append total profit/loss to correct list
      total_net.append(int(row[1]))
      
    #Calculate average change between the entire period
    for i in range(len(total_net)-1):
        #Subtract the total changes between two months and assigning it to proper list
        average_change.append(total_net[i+1]-total_net[i])

#Greatest increase in profit
greatest_increase = max(average_change)
#Greatest decrease in profit
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


#Create summary page
csvpath = os.path.join('Analysis', 'budget_data_code_summary.txt')
with open(csvpath, "w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_net)}")
    file.write("\n")
    file.write(f"Average Chnage: {round(sum(average_change)/len(average_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[increase_month]}(${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrese in Profits: {total_months[decrease_month]}(${(str(greatest_decrease))})")
    
