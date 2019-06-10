#Import libraries
import csv
import os

#define file paths

budget_csv = os.path.join('.','budget_data.csv')

#define variables

month_data = []
rev_data = []
change_data = []

#open csv and read to budget_data list, calculate monthly change write to list change_data

with open(budget_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	header = next(csvreader)
	
	for row in csvreader:
		month_data.append(row[0])
		rev_data.append(int(row[0]))

#calculate change of profits month to month

#month_change = 0
#for row  in rev_data:
#	month_change = rev_data[0] - month_change
#	change_data.append(int(row[0]))
	
		

#Output
#totalmonths = len(month_data)
#totalprofit = sum(rev_data)
#print(totalmonths)
print(rev_data)	
#print(sum(rev_data))






