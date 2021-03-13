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

# Winning candidate variable and winning count tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    
    election_results = (
    f"\nElection Results\n"
    f"-------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"--------------------\n"
)
    print(election_results, end="")
    txt_file.write(election_results)
    
    ## new loop accessing the dictionary
    ## declare votes variable as the number of votes for a specific candidate
    ## declare vote_percentage variable as percentage of total votes for a specific candidate
    ## print statement of total votes/percentage for each candidate + formatting modifications
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
       
        print(candidate_results)
        txt_file.write(candidate_results)
    ## if statement withi the loop, increasing the value of variables until reaching the highest
    ## storing these values in new variables (winning_count, percentage, candidate)
    ## output winning data through winning_candidate_summary variable
    ## save (write) variable to txt file - previously defined variable txt_file
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n"
        )
    

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)




 











    
    





















