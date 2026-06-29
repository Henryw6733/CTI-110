# Whitney Henry
# 06/29/2026
# P4HW1
# This program will ask user for number of scores, then ask user to enter that many scores,the program will use a loop. Also, after displaying score average (after dropping lowest score), the program is to display a letter grade for the calculated average.

# Pseudocode:
# Ask user how many scores they want to enter
# Create an empty list to store valid scores
# Use a loop to collect each score
# If score is less than 0 or greater than 100, display error and ask again
# If score is valid, add it to the score list
# Find the lowest score
# Remove the lowest score from the list
# Calculate the average of the remaining scores
# Determine the letter grade
# Display the lowest score, modified list, average, and grade

num_scores = int(input("How many scores do you want to enter? "))

score_list = []

for score_num in range(1, num_scores + 1):

    score = float(input(f"Enter score #{score_num}: "))

    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_num} again: "))

    score_list.append(score)

lowest_score = min(score_list)

score_list.remove(lowest_score)

average = sum(score_list) / len(score_list)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print()
print("--------------Results--------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")