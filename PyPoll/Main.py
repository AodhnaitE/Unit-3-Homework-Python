
import os
import csv

PyPollcsv = os.path.join("Resources","election_data.csv")

# Define the variable
totalVotes = 0

# Creates a dictionary to store the votes
votesPerCandidate = {}


# open up election_data
with open(PyPollcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)


    # Read each row of data after the header
    for row in csvreader:

        # Counts the number of votes       
        totalVotes += 1
        
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1   
        
        
print('\n')
print("Election Results          ")
print("--------------------------------------------")
print("Total Votes: " + str(totalVotes))
print("--------------------------------------------")

for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print("--------------------------------------------") 

winner = max(votesPerCandidate, key=votesPerCandidate.get)

print(f"Winner: {winner}")
print('\n')

# now write this to an output file

f = open("electionResults.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-----------------------------------------")
f.write('\n')
f.write("Total Votes: " + str(totalVotes))
f.write('\n')
f.write("-----------------------------------------")
f.write('\n')

for candidate, votes in votesPerCandidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-----------------------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
f.write('-----------------------------------------')
