"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: number of attempts
# 2. Process:create 2 while loops one for the attempt number and the other for if you
#want to continue and input yes or no
# 3. Out: attempt number: 
# do you want to continue
# 4. My stop condition, my attempt limit, my summary:Stop condition: First loop stops 
# when i reaches 5 (i < 5); second loop stops when answer equals "yes" or "no".
#Attempt limit: Fixed at 5 total attempts in the counting loop.
#Summary: The program counts through 5 attempt iterations and then blocks 
#execution in a validation loop until the user explicitly inputs "yes" or "no".


# Your code below
i = 0
while i < 5:
    print ("attempt number: ", i + 1)
    i = i + 1

while True:
    answer = input("Do you want to continue? (yes/no): ")
    if answer.strip().lower() == "yes":
        print("you chose to continue")
        break
    elif answer.strip().lower() == "no":
        print("you chose not to continue")
        break
    else:
        print("invalid input enter yes or no")