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

# Open the election results and read the file 
with open(file_to_load) as election_data:
# read file obkect with reader function
    file_reader = csv.reader(election_data)

# print header row 
    headers = next(file_reader)
    print(headers)



    
    




















