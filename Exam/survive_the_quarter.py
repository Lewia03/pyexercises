# Name: Lewis GAUTHIER
# Group: A
# Feature I chose: d - Difficulty (easy 15000 EUR or hard 6000 EUR)
# Why: It seemed to be the easiest to code.
#
# 1. What goes in? 
# The file scenarios_A.csv. The separator is a comma. The first line is the
# column names. Each other line is one scenario, with 14 columns: ID, the
# situation, 3 options (A, B, C), 3 budget numbers, 3 reputation numbers and
# 3 feedback texts. The numbers are plain whole numbers like -500 or 10.
# To find option B, I use the columns OptionB, BudgetB, ReputationB, FeedbackB.
# The player also types a name, E or H, and A, B or C.
#
# 2. What happens? 
# - Show the day number, the budget and the reputation.
# - Show the situation and the options A, B, C.
# - Ask the player for A, B or C (ask again if the answer is wrong).
# - Change the budget and the reputation (reputation stops at 100).
# - Show the feedback and the changes.
# - Save the move in the history list.
# - If budget or reputation is 0 or less, stop the game: fired.
#
# 3. What comes out?
# The player sees: quarter survived or fired, budget, reputation, score,
# title, best move and worst move, then "Saved in results.csv".
# One line of results.csv looks like this:
# Lewis,11000,100,Viral Legend,2026-11-03
#
# 4. What could go wrong?
# - The CSV file could be missing: the program says it cannot see where it is stops.
# - The player types a wrong answer like x: the program asks again until it
#is A, B or C .
# - Budget or reputation hits 0: the game stops at once and the player is fired.
# - Reputation goes above 100: the program sets it back to 100 and never goes above

import csv
import random
from datetime import date


# A scenario is considered as a tuple
# An option is also a tuple
def load_scenarios(filename):
    scenarios = []
    file = open(filename, newline="", encoding="utf-8")
    reader = csv.DictReader(file)
    for row in reader:
        option_a = (row["OptionA"], int(row["BudgetA"]), int(row["ReputationA"]), row["FeedbackA"])
        option_b = (row["OptionB"], int(row["BudgetB"]), int(row["ReputationB"]), row["FeedbackB"])
        option_c = (row["OptionC"], int(row["BudgetC"]), int(row["ReputationC"]), row["FeedbackC"])
        scenarios.append((row["Scenario"], option_a, option_b, option_c))
    file.close()
    return scenarios


# Ask until the player types A, B or C. Returns 0, 1 or 2.
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().lower()
    while answer not in ["a", "b", "c"]:
        answer = input("Please type A, B or C: ").strip().lower()
    return "abc".index(answer)


# Apply an option which leads it to return the new buget and reputation.
def apply_choice(budget, reputation, option):
    text, budget_change, rep_change, feedback = option
    budget = budget + budget_change
    reputation = reputation + rep_change
    if reputation > 100:
        reputation = 100
    return budget, reputation


# gives us the title when compared to a score.
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"


# Add one line at the end of results.csv
def save_result(name, budget, reputation, title):
    file = open("results.csv", "a", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow([name, budget, reputation, title, date.today()])
    file.close()


# ---------- the game starts here ----------
# Ask the name
name = input("What is your name? ")
# Load the file it will stop with a message if it is missing
try:
    scenarios = load_scenarios("scenarios_A.csv")
except FileNotFoundError:
    print("scenarios_A.csv not found. Put it in the same folder as this file.")
    quit()

# Feature d: difficulty
level = input("Easy (15000 EUR) or hard (6000 EUR)? Type E or H: ").strip().lower()
while level not in ["e", "h"]:
    level = input("Please type E or H: ").strip().lower()
if level == "e":
    budget = 15000
else:
    budget = 6000
# The values at the beginning
reputation = 50
history = []        # one tuple per day: (reputation_change, day, option_text)
fired = False

random.shuffle(scenarios)
# Play 10 days: show the day, ask A, B or C and then budget or reputation chnages
for day in range(1, 11):
    situation, option_a, option_b, option_c = scenarios[day - 1]
    options = [option_a, option_b, option_c]

    print()
    print(f"--- Day {day} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
    print(situation)
    print("  A:", option_a[0])
    print("  B:", option_b[0])
    print("  C:", option_c[0])

    number = ask_choice()
    chosen = options[number]

    budget, reputation = apply_choice(budget, reputation, chosen)
    history.append((chosen[2], day, chosen[0]))

    print(chosen[3])
    print(f"Budget {chosen[1]:+d} EUR, Reputation {chosen[2]:+d}")

    if budget <= 0 or reputation <= 0:
        fired = True
        break

# Show the result: fired or survived
print()
print("==============================")
if fired:
    title = "Fired"
    print("You are fired!")
    if budget <= 0:
        print("Your budget hit zero.")
    else:
        print("Your reputation hit zero.")
    print(f"Budget: {budget} EUR, reputation: {reputation}/100")
else:
    score = reputation + budget // 200
    title = get_title(score)
    print("Quarter survived!")
    print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
    print(f"Final score: {score}")

print(f"{name}, your title: {title}")

# Tuples are compared from the first element, so max/min use the reputation change
best = max(history)
worst = min(history)
print(f'Best move: day {best[1]}, "{best[2]}" ({best[0]:+d})')
print(f'Worst move: day {worst[1]}, "{worst[2]}" ({worst[0]:+d})')

# Save the game in results.csv
save_result(name, budget, reputation, title)
print("Saved in results.csv")