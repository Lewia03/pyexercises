"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A number N from the user.
# 2. Process: Loop from 1 to N and check if each number is divisible by 2.
# 3. Out: Prints whether each number is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
#    - On 0: Tell the user it must be at least 1.
#    - On negative: Tell the user to use a positive number.
#    - On 5000: Stop it if it's over 100 so it doesn't flood the screen.


# Your code below

num = int(input("Enter a number: "))

if num < 1:
    print("Please enter a number 1 or higher.")
elif num > 100:
    print("Number is too big, pick 100 or less.")
else:
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
