import os
import csv

# load the dataset file
fileLoad = os.path.join("resources", "election_data.csv")

# file to hold the output of analysis
analysisFile = os.path.join("analysis", "election_analysis.txt")

# intialize variables
totalVotes = 0          # variable for total votes
winningCount = 0        # variable for winning vote total
candidateNames = []     # list for candidate names
candidateVotes = {}     # dictionary to hold number of votes for each candidate
winningCandidate= ""    # variable for winning candidate name 

with open(fileLoad) as electData:   # read the csv file
    reader = csv.reader(electData)  # create reader object
    header = next(reader)           # read header row
    for row in reader:
        totalVotes += 1             # increment total vote count

        # check to see if the candiate is in the candidate name list
        if row[2] not in candidateNames:    
            candidateNames.append(row[2])   # if not, then add name to list
            candidateVotes[row[2]] = 1      # start the vote count at 1 by adding to the candidate vote dictionary
        else:
            candidateVotes[row[2]] += 1     # if yes, then increment the vote count by 1

voteResults = ""                                                # initialize results variable string
vrHeader = ["Canditate Name", "Pct. Votes", "Number of Votes"]  # create results header row

for candidateName in candidateVotes:
    votes = candidateVotes.get(candidateName)       # get total votes by candidate
    votePct = (float(votes) / float(totalVotes))    # get vote percent

    # compare votes to the winning count
    if votes > winningCount:
        winningCount = votes                # update new winning vote total
        winningCandidate = candidateName    # update new winning candidate

    votes = f"{votes:,}"                                            # inital format of votes to include thousand separator, after votePct to avoid string conversion error
    votePct = f"{votePct:.3%}"                                      # inital format of votePct to three decimal places and autoformat to percentage
    voteResults += f"{candidateName:<24}{votePct:>14}{votes:>20}\n" # formatting results to align text   

winningCandidate = f"The election winner is {winningCandidate.upper()}."    # formatted for uppper-case for emphasis

tvTitle = "Total Votes"         # initialize and set string for "Total Votes" to allow additional formatting when output occurs                         
totalVotes = f"{totalVotes:,}"  # inital format of total votes to include thousand separator

# additonal formatting to output to align text
output = (
    f"\n\n\n*********************ELECTION RESULTS*********************\n\n"
    f"{tvTitle:<24}{totalVotes:>14}\n\n"
    f"----------------------------------------------------------\n\n"
    f"{vrHeader[0]:<24}{vrHeader[1]:>14}{vrHeader[2]:>20}\n\n"
    f"{voteResults}\n"
    f"----------------------------------------------------------\n\n"
    f"{winningCandidate}\n\n"
    f"----------------------------------------------------------\n\n"
)
# print output to console
print(output)  

# export the output to the text file
with open(analysisFile, "w") as textFile:
    textFile.write(output)