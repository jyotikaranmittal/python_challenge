# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0 
    # Track the total number of votes cast
total_votes=len(file_to_output)
    

# Define lists and dictionaries to track candidate names and vote counts
votes=[]
candidates=[]


# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it 
with open(file_to_load) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')   
    print(csvreader)

    # Skip the header row
    header = next(csvreader)
    print(header)

    # # Loop through each row of the dataset and process it
    for rows in csvreader:
        votes.append(rows[0])
        candidates.append(str(rows[2]))

    total_votes=len(votes)
    # print(f"Total Votes: {total_votes}")
    # print("----------------------------")

    # To get of unique candidates:
    unique_candidates=set(candidates)

    count_anthony=0
    count_charles=0
    count_diana=0
for candidate in candidates:
    if candidate=="Raymon Anthony Doane":
        count_anthony=count_anthony+1
    elif candidate=="Charles Casper Stockham":
        count_charles=count_charles+1
    else:
        count_diana=count_diana+1

anthony_percent=round((count_anthony/len(votes))*100,3)
charles_percent=round(((count_charles/len(votes))*100),3)
diana_percent=round(((count_diana/len(votes))*100),3)
# print(f"Charles Casper Stockham: {charles_percent}% ({count_charles})")
# print(f"Diana DeGette: {diana_percent}% ({count_diana})")
# print(f"Raymon Anthony Doane: {anthony_percent}% ({count_anthony})")
# print("----------------------------")


winner=""
if (anthony_percent)>(charles_percent) and (anthony_percent)>(diana_percent):
        winner="Raymon Anthony Doane"
elif (charles_percent)> (anthony_percent) and  (charles_percent)>(diana_percent):     
    winner="Charles Casper Stockham"        
else:
    winner="Diana DeGette"       
# print(f"Winner: {winner}")


        # Print and save each candidate's vote count and percentage
output=f"Total Votes: {total_votes}\nCharles Casper Stockham: {charles_percent}% ({count_charles})\nDiana DeGette: {diana_percent}% ({count_diana})\nRaymon Anthony Doane: {anthony_percent}% ({count_anthony})\nWinner: {winner}"

    # Generate and print the winning candidate summary
print(output)
    # Save the winning candidate summary to the text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
