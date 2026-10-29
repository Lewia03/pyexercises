"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence entered by the user (string).
# 2. Process: The program prompts the user for input and applies four distinct Python string transformation methods to it.
# 3. Out: Four modified versions of the input sentence printed to the console.
# 4. My four transformations, and when each is useful:
#    - strip(): Removes leading/trailing whitespace; useful for cleaning up user inputs before storing or processing.
#    - upper(): Converts all characters to uppercase; useful for creating bold headlines or doing case-insensitive string comparisons.
#    - title(): Capitalizes the first letter of each word; useful for formatting book titles, article headings, or user names.
#    - swapcase(): Inverts the casing of all letters; useful for creating playful visual effects or toggling text modes.


# Your code below

# Ask the user for a sentence
sentence = input("Please enter a sentence: ")

# Apply four distinct transformations
t1 = sentence.strip()
t2 = sentence.upper()
t3 = sentence.title()
t4 = sentence.swapcase()

# Display the transformations
print("String Transformations")
print("1. Strip:   ", t1)
print("2. Upper:   ", t2)
print("3. Title:   ", t3)
print("4. Swapcase:", t4)
