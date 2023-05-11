#import data
import os
import csv

# Grabbing Location of Data
election_csv = os.path.join('Resources', 'election_data.csv')

# open and read csv
with open(election_csv) as csv_file :
    csv_reader = csv.reader(csv_file,delimiter=",")

    # skip header
    csv_header=next(csv_file)
    print(f"Header: {csv_header}")

    #defining counter
    votes_list = []
    candidate_results = {}
    total_votes = 0
    candidate_charles = 0
    candidate_diana = 0
    candidate_raymon = 0
    
    # Read each row of data
    for row in csv_reader :
        total_votes += 1
        ballot_id=(row[0])
        votes_list.append(ballot_id)
        names=(row[2])
        candidate_results=(names)
        number_votes=len(votes_list)
        
    #counting for Charles
        if names == 'Charles Casper Stockham':
            candidate_charles +=1
        charles_percent = (candidate_charles/number_votes) * 100

        if names == 'Diana DeGette':
            candidate_diana +=1
        diana_percent = (candidate_diana/number_votes) * 100

        if names == 'Raymon Anthony Doane':
            candidate_raymon +=1
        raymon_percent = (candidate_raymon/number_votes) * 100

if charles_percent > diana_percent and charles_percent > raymon_percent:
    winner = 'Charles Casper Stockham'
elif diana_percent > charles_percent and diana_percent > raymon_percent:
    winner = 'Diana DeGette'
else:
    winner = 'Raymon Anthony Doane'




#print(canidate_results)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {number_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({candidate_charles})")
print(f"Diana DeGette: {diana_percent:.3f}% ({candidate_diana})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({candidate_raymon})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#create a new file       
#create a new file       
with open('Analysis/Election_Results.txt', 'w') as file:

    #inputing information into text file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {number_votes}\n")
    file.write("-------------------------\n")
    file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({candidate_charles})\n")
    file.write(f"Diana DeGette: {diana_percent:.3f}% ({candidate_diana})\n")
    file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({candidate_raymon})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")