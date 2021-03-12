# the data we need to retrieve:
    # 1. total number of votes cast 
    # 2. complete list of candidates who received votes 
    # 3. percentage of votes each candidate won
    # 4. total number of votes each candidate won 
    # 5. winner of the election based on popular vote


# Add dependencies 
import csv
import os 

# Assign variable to load a file from a path (indirect)
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize vote counter and set to 0
total_votes = 0

# Initialize Candidates list 
candidate_options = []

# Initizalize Dictionary 
candidate_votes = {}

# Open the election results and read the file 
with open(file_to_load) as election_data:
# read file object with reader function
    file_reader = csv.reader(election_data)

# read header row - skipping first row in the count (ie header row)
    headers = next(file_reader)
# loop through rows in file_reader
## increase total_votes by one with every row and get total vote count
## initialize variable candidate_name to hold candidate values and reference respective column 
## use conditionals to add new candidate name if it hasn't been added already
## begin tracking a candidates vote count referencing the empty dictionary 
## add a vote to the candidate's vote count outside of if statement, but within forloop
## print info
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

print(total_votes)
print(candidate_options)
print(candidate_votes)



 











    
    





















