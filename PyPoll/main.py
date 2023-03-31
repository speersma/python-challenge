# import the necessary modules
import os
import csv

# set path for csv file to be read
csvpath = os.path.join("Resources", "election_data.csv")


# create counters
totalVotes = 0
voteDict = {"Charles Casper Stockham": 0, "Diana DeGette": 0, "Raymon Anthony Doane": 0}
votePercDict = {'Charles': 0, "Diana": 0, "Raymon": 0}
winner = ' '

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

        # add to candidate's vote total
        if row[2] == "Charles Casper Stockham":
            voteDict["Charles Casper Stockham"] += 1
        elif row[2] == "Diana DeGette":
            voteDict["Diana DeGette"] += 1
        else:
            voteDict["Raymon Anthony Doane"] += 1

    # calculate percentage of votes obtained by each candidate
    votePercDict["Charles"] = round((voteDict["Charles Casper Stockham"]/totalVotes)*100, 3)
    votePercDict['Diana'] = round((voteDict['Diana DeGette']/totalVotes)*100, 3)
    votePercDict['Raymon'] = round((voteDict['Raymon Anthony Doane']/totalVotes)*100, 3)

    # decide winner
    winner = max(voteDict, key=voteDict.get)

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
    writer.writerow([f'Charles Casper Stockham: {votePercDict["Charles"]}% ({voteDict["Charles Casper Stockham"]})'])
    writer.writerow([f'Diana DeGette: {votePercDict["Diana"]}% ({voteDict["Diana DeGette"]})'])
    writer.writerow([f'Raymon Anthony Doane: {votePercDict["Raymon"]}% ({voteDict["Raymon Anthony Doane"]})'])
    writer.writerow(["-------------------------"])
    writer.writerow([f'Winner: {winner}'])
    writer.writerow(["-------------------------"])



# print out results to terminal
print("Election Results")
print("-------------------------")
print(f'Total Votes: {totalVotes}')
print("-------------------------")
print(f'Charles Casper Stockham: {votePercDict["Charles"]}% ({voteDict["Charles Casper Stockham"]})')
print(f'Diana DeGette: {votePercDict["Diana"]}% ({voteDict["Diana DeGette"]})')
print(f'Raymon Anthony Doane: {votePercDict["Raymon"]}% ({voteDict["Raymon Anthony Doane"]})')
print(f'Winner: {winner}')