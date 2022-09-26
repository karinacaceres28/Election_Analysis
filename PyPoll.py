#The data we need to retreieve

#add out our dependencies
import csv
import os

# Assign a variable for the file to load and the path ((3.4.2))
file_to_load = '/Users/kweeniehutjrs/Desktop/Analysis Projects/Stock Analysis, Unit 3/election_analysis/Resources/election_results.csv'
mainPath = '/Users/kweeniehutjrs/Desktop/Analysis Projects/Stock Analysis, Unit 3/election_analysis/Resources/analysis'

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join(mainPath, "election_analysis.txt")

# Open the election results and READ the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

####
# Close the file.
election_data.close()

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.p
file_to_save = os.path.join(mainPath, "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #you can continue to write using the write()
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#1. The total number of votess cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on pupular vote