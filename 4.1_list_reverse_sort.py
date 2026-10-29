"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A starting list of items (favorite movies or numbers).
# 2. Process: Make temporary sorted/reversed versions of the list without changing the original.
# 3. Out: The list shown in 4 different orders, plus the original list at the end to prove it wasn't changed.
# 4. My four orders, and which ones modify the original:
#    - sorted(list): Alphabetical (does NOT modify original)
#    - sorted(list, reverse=True): Reverse alphabetical (does NOT modify original)
#    - list(reversed(list)): Reversed original order (does NOT modify original)
#    - sorted(list, key=len): By word length (does NOT modify original)
#    * Note: None of these 4 modify the original list because methods like list.sort() or list.reverse() were avoided.


# Your code below

# Original list from Exercise 4.0
movies = ["Inception", "Avatar", "Titanic", "Jaws", "Interstellar"]

# Display in 4 different orders using copy/return methods
print("1. Alphabetical:", sorted(movies))
print("2. Reverse Alphabetical:", sorted(movies, reverse=True))
print("3. Reversed original:", list(reversed(movies)))
print("4. By word length:", sorted(movies, key=len))

# Prove the original list has not been changed
print("Proof - Original list is unchanged:")
print(movies)
