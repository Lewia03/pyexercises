"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# Number_1: First integer entered by the user.
#Number_2: Second integer entered by the user.
#
# 2. Process:
#Prompt the user to type two numbers and convert both string inputs into integers.
#Print the two numbers to confirm input.
#Compute the addition, subtraction (Number_2 - Number_1), multiplication, and division of the two numbers.
#
# 3. Out:
#The value of Number_1 and Number_2.
#The calculated sum, difference, product, and quotient.
#
# 4. What happens when the second number is zero, and why:
#The program crashes with an Error: division by zero.
# Why: The script executes line by line. It successfully calculates the sum, difference, and product 
# because addition, subtraction, and multiplication by zero are valid math operations. 
#Fix is to put an if 


# Your code below
Number_1 = int(input("enter number 1: "))
Number_2 = int(input("Enter number 2: "))
print("The number 1 is: ", Number_1)
print("The number 2 is: ", Number_2)

# addition of numbers
sum = Number_1 + Number_2 
print("The sum of two numbers is:", sum)

# difference of 2 number
dif = Number_2 - Number_1 
print("The difference of two numbers is:", dif)

#product of two numbers
product = Number_1 * Number_2
print("The product of two numbers is:", product)

#division of two numbers
if Number_2 != 0:
    division = Number_1 / Number_2
    print("The division of two numbers is:", division)
else:
    print("The second number is 0")


