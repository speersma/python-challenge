# import the necessary modules
import os # for the universal file path stuff
import csv # for the csv reader and writer functions

# set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# create counters 
totalMonths = 0
totalProfit = 0
changes = []
greatestIncrease = [" ", 0]
greatestDecrease = [" ", 0]
prevProfLoss = 0


# open the csv
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read in the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    print(csvreader)

    # read each row of data
    for row in csvreader:
        # add one to the total months
        totalMonths += 1

        # add to the total profit
        totalProfit += int(row[1])

        # append change to list of changes
        # changes.append(int(row[1]))

        # calculate profit ()
        profit = int(row[1]) - prevProfLoss
        
        # append profit/change to changes list
        changes.append(profit)

        # set prevProfLoss = to row[1]
        prevProfLoss = int(row[1])

        # check if profit is more than greatestIncrease or..
        ##...less than greatestDecrease
        if profit > greatestIncrease[1]:
            greatestIncrease = [row[0], profit]
        if profit < greatestDecrease[1]:
            greatestDecrease = [row[0] , profit]
    
# calculate average profit (remember to minus the first change because the first month's profit isn't a change)
avgProfit = round(((sum(changes)-changes[0])/(len(changes)-1)),2)


# WRITING THE NEW CSV FILE
outputPath = os.path.join("pybankOutput.txt")


# open the file using "write" mode. Specify the variable to hold the contents
with open(outputPath, 'w') as txtfile:
    writer = csv.writer(txtfile)

    # write a header row
    writer.writerow(["Financial Analysis"])

    # write the next row
    writer.writerow(["----------------------"])
    writer.writerow([f"Total Months: {totalMonths}"])
    writer.writerow([f"Total: ${totalProfit}"])
    writer.writerow([f"Average Change: ${avgProfit}"])
    writer.writerow([f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})"])



# somehow print the analysis to the terminal   
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalProfit}")
print(f"Average Change: ${avgProfit}")
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")