"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of numbers goes in.
# 2. Process: The function loops through the list and adds every number together to get a total.
# 3. Out: the sum of numbers 
# 4. My function name, and why return rather than print: my function name is compute_sum 
# return instead of print so it isnt overwritten


# Your code below
print("HEllo, World!")

number_1 = 10
number_2 = 20

sum = number_1 + number_2
print("The sum of", number_1, "and", number_2, "is", sum)

number_3 = 100
number_4 = 220

sum = number_3 + number_4
print("The sum of", number_3, "and", number_4, "is", sum)

def compute_sum(a, b):
    return a + b

result1 = compute_sum(10, 20)
result2 = compute_sum(100, 220)
result3 = compute_sum(5, 15)
print("The sums are:", result1, "and", result2, "and", result3)