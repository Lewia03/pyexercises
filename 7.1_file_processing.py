"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -
# -
# -
# -

# 1. In:
# 2. Process, problem by problem:
# 3. Out:
# 4. How I decide which word is the last name:


# Your code below
input_filename = "names.txt"
output_filename = "cleaned_names.txt"

clean_names = []

# --- 1. LOAD AND CLEAN DATA ---
with open(input_filename, mode="r", encoding="utf-8") as file:
    for line in file:
        # Strip leading/trailing whitespaces and newlines
        cleaned_line = line.strip()
        
        # Problem 1: Skip blank lines
        if not cleaned_line:
            continue
        
        # Problem 3: Standardize internal spacing by splitting words and re-joining
        words = cleaned_line.split()
        
        # Skip invalid lines that don't have both first and last name
        if len(words) < 2:
            continue
            
        # Problem 2: Convert to Title Case (e.g., "john" -> "John")
        formatted_name = " ".join(word.capitalize() for word in words)
        
        # Problem 4: Avoid duplicates
        if formatted_name not in clean_names:
            clean_names.append(formatted_name)


# to sort by last name
# name.split()[-1] picks the last word (the last name) to sort by
clean_names.sort(key=lambda name: name.split()[-1].lower())


# The new output file 
with open(output_filename, mode="w", encoding="utf-8") as file:
    for name in clean_names:
        file.write(name + "\n")

print(f"Done! Cleaned and sorted {len(clean_names)} names into '{output_filename}'.")