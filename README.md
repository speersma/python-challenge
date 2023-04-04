# python-challenge
This repository contains two basic analyses using python scripts. Both scripts read from a csv file using a context manager, analyze the contents of the csv, and output results by writing them to a txt file. Results are also printed to the terminal for easy viewing. The particular analyses performed are detailed below. 

## PyBank Financial Analysis
The `main.py` file in the PyBank folder reads in a csv containing budget data for a ficticious company. This data consisted of two columns: "Date" and "Profit/Losses". Each row of data represented a month of profit or loss for the company. Using this data, descriptive statistics were generated. 

Metrics produced include: 
- *Total Months*
- *Total Profit/Loss*
- *Average Change (month to month)* 
- *Greatest Increase in Profits (month and amount)*
- *Greatest Decrease in Profits (month and amount)*

This financial analysis (pybankOutput.txt) revealed that while the company may have a net positive profit over the entire 86 month period, the average monthly change in profit is negative ($-8311.11). 

## PyPoll Voting Analysis
The `main.py` script in the PyPoll folder analyzes voting data for a particular district. The data has columns for "Voter ID", "County", and "Candidate". "Voter ID" provides a unique ID number for every voter. "County" identifies the county in which the vote was cast. "Candidate" reflects which candidate the vote was cast for. The analysis produced was meant to identify the winner of the election and impart a basic understanding of the distribution of votes. To that end, statistics produced included:
- *Total Votes*
- *Percentage of Votes Won Across Candidates*
- *Count of Votes Won Across Candidates*

Additionally the file containing the output of this analysis (pypollOutput.txt) decides the winner of the election based on popular vote. 