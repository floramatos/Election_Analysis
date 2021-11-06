import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Create variable to count total votes
total_votes = 0

#Create list to find the candidates
candidate_options = []

# Create dictionary to find votes for each candidate
candidate_votes = {}

#Create variable to declare winning candidate
winning_candidate = ""

#Create variable to count the election winner
winning_count = 0

#Create varible to calculate the winner percentage
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #Add to total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            #Add candidate_name to candidate_options list
            candidate_options.append(candidate_name)

            #Track candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to a candidate's count.
        candidate_votes[candidate_name] += 1

#Print the candidate votes
print(candidate_votes)

#Print the candidate list
print(candidate_options)

#Print the total votes
print(total_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes 
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson")
