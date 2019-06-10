#Import libraries
import csv
import os

#define file paths

budget_csv = os.path.join('.','budget_data.csv')

#define variables

month_data = []
rev_data = []

greatest_change = 0
least_change  = 0
change = 0
total_change = 0


#open csv and read to budget_data list, calculate monthly change write to list change_data

with open(budget_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	header = next(csvreader)
	
	for row in csvreader:
		month_data.append(row[0])
		rev_data.append(float(row[1]))
		change = row[1]
	if greatest_change < change:
		greatest_change = change
	elif least_change > change:
		least_change = change
	total_change =+ change
	i =+ i
	
		

#Output
totalmonths = len(month_data)
print(totalmonths)
#print(sum(rev_data)
print(total_change)
print(greatest_change)
print(least_change)





