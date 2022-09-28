#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on pupular vote

#The data we need to retrieve

#add out our dependencies
import csv
import os

# Assign a variable for the file to load and the path ((3.4.2))
file_to_load = '/Users/kweeniehutjrs/Desktop/Analysis Projects/Stock Analysis, Unit 3/election_analysis/Resources/election_results.csv'
mainPath = '/Users/kweeniehutjrs/Desktop/Analysis Projects/Stock Analysis, Unit 3/election_analysis/analysis'
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join(mainPath, "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

#1. Declare the epmty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and READ the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        #Print the cadidate name from each row
        candidate_name = row[2]

       
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
        
            #begin tracking that candidat's vote cound.
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#save the results to our text file.
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #determine the percentage of votes for each candidate by looping thru the counts
    #1 iterate thru the candidate list
    for candidate_name in candidate_votes:
        #2 retrieve vote count for a candidate
        votes = candidate_votes[candidate_name]
        #3 calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # #4 print the candidate name and percentage of votes
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")
    
     #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print the candidate list
    #Removed print(candidate_votes) to add candidate_results variable
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)   


    

####
# # Close the file.
# election_data.close()

# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# # Create a filename variable to a direct or indirect path to the file.p
# file_to_save = os.path.join(mainPath, "election_analysis.txt")

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     #you can continue to write using the write()
#     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

