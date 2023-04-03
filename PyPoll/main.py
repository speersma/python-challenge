# import the necessary modules
import os
import csv

# set path for csv file to be read
csvpath = os.path.join("Resources", "election_data.csv")


# create totalVotes counter and winner var
totalVotes = 0
winner = ' '

# create specialized candidateDictionary with vote count and percentage
candidateDict = {}

# open the csv
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read in header row first
    csvHeader = next(csvreader)
    print(f'CSV Header: {csvHeader}')

    # read each row of data and do the stuff
    for row in csvreader:

        # add one to total votes
        totalVotes += 1

        # if candidate not in candidateDict, add them and start counting
        # if candidate IS IN candidateDict add to candidate's vote total
        if row[2] in candidateDict:
            candidateDict[row[2]][0] += 1
        else:
            candidateDict.setdefault(row[2], [0, 0])
            candidateDict[row[2]][0] += 1

    # printing candidateDict for testing
    print(candidateDict)

    # calculate percentage and add it to second value of candidate's key in candidateDict
    for key in candidateDict:
        candidateDict[key][1] = round(((candidateDict[key][0]/totalVotes)*100),3)

    # printing candidateDict for testing
    print(candidateDict)

    # decide winner
    winner = max(candidateDict, key=candidateDict.get)

# WRITING NEW CSV FILE
outputPath = os.path.join('analysis', 'pypollOutput.txt')

# open the file using write mode
with open(outputPath, 'w') as txtfile:
    writer = csv.writer(txtfile)

    # write header row
    writer.writerow(["Election Results"])

    # write the next rows
    writer.writerow(["-------------------------"])
    writer.writerow([f'Total Votes: {totalVotes}'])
    writer.writerow(["-------------------------"])
    for key, val1, in candidateDict.items():
        writer.writerow([f'{key}: {val1[1]}% ({val1[0]})'])
    writer.writerow(["-------------------------"])
    writer.writerow([f'Winner: {winner}'])
    writer.writerow(["-------------------------"])



# print out results to terminal
print("Election Results")
print("-------------------------")
print(f'Total Votes: {totalVotes}')
print("-------------------------")
for key, val1, in candidateDict.items():
    print(f'{key}: {val1[1]}% ({val1[0]})')
print(f'Winner: {winner}')