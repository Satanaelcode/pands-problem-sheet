# Es program
# The text file is a plain text file and not a binary file
# This program rads in a text file and outputs
# the number of 'e' it contains
# Filename taken from an argument on the command line
# The program should count both uppercase and lower case,
# or as part of a word or string.


# Using sys.argv module to access command line arguments in a list
import sys
# Get the filename from the command line arguments
Anne_of_Green_Gable = sys.argv[0]

# Open the file for reading
with open(Anne_of_Green_Gable, 'r') as f:
    # Initialize a counter for the number of e's found
    e_count = 0
    # Loop over each line in the file
    for line in f:
        # Count the number of e's in the line and add it to the counter
        e_count += line.count('e') + line.count('E')

# Output the final count of e's found
print(e_count)






