import os
import csv

csvpath = os.path.join("..", "..", "..", 'election_data.csv')

#Give each variable a list 
total_votes = 0
candidates = []
candidate_votes = []

#Open csv file
with open(csvpath) as election:
    csvreader=csv.reader(election, delimiter=',')

    #Skip Header for row count
    csv_header = next(csvreader)
    
    #Read csv file by row
    for row in csv.reader(election):
      
        #Count number of rows in sheet
        total_votes += 1

        #Start counting candi..dates in row 2
        candidate_name = (row[2])

        #Add a count to each candidate name whenever a match is found
        if candidate_name in candidates:
            candidate_index = candidates.index(candidate_name)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else:
            candidates.append(candidate_name)
            candidate_votes.append(1)

#Percentage of each candidate and name
percent = []
max_votes = candidate_votes[0]
total_index = 0

for i in range(len(candidates)):
    vote_percent = round(candidate_votes[i]/total_votes*100,2)
    percent.append(vote_percent)

    if candidate_votes[i] > max_votes:
        max_votes = candidate_votes[i]
        total_index = i

#WINNER!!
winner = candidates[total_index]

#Print to Terminal 
print("Election Results")
print("-------------------------------")
print(f"Total Vote: {total_votes}")
print("-------------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]} : {percent[i]}% ({candidate_votes[i]})")
print("-------------------------------")
print(f"Winner: {winner}")

#Output to Analysis
csvpath = os.path.join('Analysis', 'election_data_code_summary.txt')
with open(csvpath, "w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------------")
    file.write("\n")
    file.write(f"Total Vote: {total_votes}")
    file.write("\n")
    file.write("-------------------------------")
    file.write("\n")
    for i in range(len(candidates)):
        file.write(f"{candidates[i]} : {percent[i]}% ({candidate_votes[i]})")
        file.write("\n")
    file.write("-------------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")