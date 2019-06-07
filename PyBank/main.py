#Import libraries
import csv
import os


#Define input and output files

#budget_input = os.path.join('.', 'budget_data.csv')
#budget_output = "budget_output.csv"

#Read csv data
with open('budget_data.csv', newline='') as csvfile:
    budgetData = csv.reader(csvfile, delimiter=",")
    print(budgetData)




#skip header row; count numnber of rows; assign to TotalMonths
# Count number of months
#next(BudgetData)
#for i in BudgetData
    

#Calculate Net Profits/Losses
#Calculate Avg of changes for Profits/Losses
#Find greatest increase in profits; Return Date and Amount
#Find greatest decrease in losses; Return Date and Amount
