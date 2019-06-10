#Import libraries
import csv
import os

#define file paths

budget_csv = os.path.join('.','budget_data.csv')

#define variables

month = "none"
rev = 0
prev_rev = 0
greatest_change = 0
greates_change_month = "greatest_change_month"
least_change  = 0
lease_change_month = "least_change_month"
rev_change = 0
total_rev = 0
total_months = 1
avg_change = 0


#open csv and read to budget_data list, calculate monthly change write to list change_data

with open(budget_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	header = next(csvreader)
	
	for row in csvreader:
	#	month = month(row[0])
		rev = (float(row[1]))
		rev_change = rev - prev_rev
		if greatest_change < rev_change:
			greatest_change = rev_change
			greatest_change_month = month
		elif least_change > rev_change:
			least_change = rev_change
			least_change_month = month
		else:	total_rev=+ rev_change
		total_months =+ 1
	
avg_change = total_rev / total_months
	
		

#Output
print(total_months)
print(total_rev)
print(avg_change)
print(greatest_change)
print(greatest_change_month)
print(least_change)
print(least_change_month)





