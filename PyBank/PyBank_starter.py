# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total=0
total_net = 0
first_row=[]
# Add more variables to track other necessary financial data
dates=[]
profit_loss=[]
increase=[]
# Open and read the csv

with open(file_to_load) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')   
    print(csvreader)

    # Skip the header row
    csv_header = next(csvreader)
    print(csv_header)
    # Process each row of data
    # Extract first row to avoid appending to net_change_list
    for rows in csvreader:
        # print(rows[0])
        dates.append(rows[0])
        profit_loss.append(int(rows[1]))
    first_row=dates

    # Track the total and net change
    total_months=len(dates)
    total=sum(profit_loss)
    # print(f"Total Months: {total_months}")
    # print(f"Total: ${total}")
    
    
    # Calculate the greatest increase in profits (month and amount)
    
    for x in range(0,len(profit_loss)-1):
        Difference= (profit_loss[x+1])-(profit_loss[x])
        increase.append(Difference)
    Average_change=round(sum(increase)/(len(dates)-1),2)
    # print(f"Average Change: ${Average_change}")
    
    
    Greatest_increase=max(increase)
    greatest_increase_index=increase.index(Greatest_increase)
    Greatest_increase_month=dates[greatest_increase_index+1]
    # print(f"Greatest increase in Profits: {Greatest_increase_month} (${Greatest_increase})")

    



    # Calculate the greatest decrease in losses (month and amount)
    Greatest_decrease=min(increase)
    greatest_decrease_index=increase.index(Greatest_decrease)
    Greatest_decrease_month=dates[greatest_decrease_index+1]
    # print(f"Greatest decrease in Profits: {Greatest_decrease_month} (${Greatest_decrease})")


    
# Calculate the average net change across the months


# Generate the output summary
output=f"Total Months: {total_months}\nTotal: ${total}\nAverage Change: ${Average_change}\nGreatest increase in Profits: {Greatest_increase_month} (${Greatest_increase})\nGreatest decrease in Profits: {Greatest_decrease_month} (${Greatest_decrease})"
# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
