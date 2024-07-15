# Write an if-else statement that determines if a string (like "apples") is less than 5 characters long. 
# Use the function len() to determine the length of the string. 
# Print an output message that tells you the length of the string if the string is less than 5 characters long. 
# If the string is longer than 5 characters, print out something that says "string is too long" or something like that.


# [JONATHAN] Delete my notes here when you update it.

input_string = 'apples'
len(input_string)

if len(input_string) < 5:   # [JONATHAN] Add len() around the input_string. Remove the word 'characters'. Add a colon (:) at the end of this line.
    print('String is too short')  # [JONATHAN] This should be indented 
else:
    print('String is too long')






# The first line says: if the length of the input_string is less than 5
# The expression 'len(input_string) < 5' will evaluate to False because "apples" is not less than 5 characters in length.

if (expression that evaluates to True or False):
	# Do things if expression evaluates to True
else:
	# Do things if expression evaluates to False


################################################################################
# While Loop Template

# A while loop executes the code inside the body of the while loop for as long as the expression evaluates to True
while (expression evaluates to True):
	# Do things


################################################################################
# While Loop Examples

# This example loops forever because the expression never encounters a situation where it evaluates to False
while True:
	print("Hello World!")


# This example provides an iteration counter
i = 0;
while i < 100:
	print(i)
	i = i + 1  # i += 1


# Loop through list of subjects
i = 0
subjects = ["geology", "algebra", "history", "civics"]
length_subjects = len(subjects)

while i < length_subjects:
	print(subjects[i])






# While Loop
i = 0
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
while i < 5:
    print(planets[i])
    i += 1






# Import Library
import datetime
import time

# Define Variable
i = 0

# While Loop
while i < 10:
    print(f'Loop Number: {i}') # This is known as an f-string
    print(datetime.datetime.now()) # Show datetime in 'YYYY-MM-DD HH:MM:SS.000000' format
    time.sleep(2.0) # Delay for 2 seconds
    i += 1 # Increment (add one)




