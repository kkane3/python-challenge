#Import libraries
import csv
import os

#define input file paths

budget_csv = os.path.join('.','budget_data.csv')

#define variables

rev = 0
prev_rev = 0
greatest_change = 0
greates_change_month = "greatest_change_month"
least_change  = 0
lease_change_month = "least_change_month"
rev_change = 0
total_rev = 0
total_rev_change = 0
total_months = 0
avg_change = 0

#open csv and read

with open(budget_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

#skip header row

	header = next(csvreader)

#for each row take second col and iteratea through rows to calcualte change in revenue monthly.  Store values to calculaute greatest increase, greatest decrease and find averages. 	
	
	for row in csvreader:
		rev = (float(row[1]))
		rev_change = rev - prev_rev  #selected month - previous month
		if greatest_change < rev_change:
			greatest_change = rev_change
			greatest_change_month = row[0]
		elif least_change > rev_change:
			least_change = rev_change
			least_change_month = row[0]
		prev_rev = rev
		total_rev= total_rev + rev
		total_rev_change = total_rev_change + rev_change
		total_months = total_months + 1
	
	avg_change = total_rev_change / total_months
	
#Output

print(f"Financial Analysis")
print(f"---------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_rev}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {greatest_change_month} {greatest_change}")
print(f"Greatest Decrease in Profits: {least_change_month} {least_change}")

out = open("output_revenue.txt", "w+")

out.write(f"Financial Analysis\n") 
out.write(f"---------------------------------\n")
out.write(f"Total Months: {total_months}\n")
out.write(f"Total: {total_rev}\n")
out.write(f"Average Change: {avg_change}\n")
out.write(f"Greatest Increase in Profits: {greatest_change_month} {greatest_change}\n")
out.write(f"Greatest Decrease in Profits: {least_change_month} {least_change}\n")


out.close()



