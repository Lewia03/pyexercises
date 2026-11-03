"""
Exercise 7.0 — Collecting data and saving it

ANSWER THESE FIRST:
1. What goes in?
   User input from the terminal: student name, study subject, and study hours.

2. What happens to it?
   - The program asks the user for the details.
   - It validates that study hours is a positive number.
   - It checks if `study_log.csv` exists. If not, it creates it and writes the header line.
   - It appends the new entry as a new line in `study_log.csv`.

3. What comes out? (file name and columns)
   - File name: `study_log.csv`
   - Columns: `student_name,subject,hours_studied`

4. Why these columns, and what this file is for:
   - These columns record who studied what and for how long.
   - Once the file has 200 rows, I could calculate the average study time per subject or see which student studied the most.
"""

import os
import csv

# File name
filename = "study_log.csv"

# --- 1. GET INPUT AND VALIDATE ---
student_name = input("Enter student name: ").strip()
while not student_name:
    print("Name cannot be empty.")
    student_name = input("Enter student name: ").strip()

subject = input("Enter subject name: ").strip()
while not subject:
    print("Subject cannot be empty.")
    subject = input("Enter subject name: ").strip()

# check that hours is a valid positive number
hours_input = input("Enter hours studied: ").strip()
while True:
    try:
        hours_studied = float(hours_input)
        if hours_studied > 0:
            break
        else:
            print("Hours must be greater than 0.")
    except ValueError:
        print("Please enter a valid number for hours.")
    hours_input = input("Enter hours studied: ").strip()


# checking if the file exists or not
file_exists = os.path.exists(filename)


# add it to csv file
with open(filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # add header if it is new file
    if not file_exists:
        writer.writerow(["student_name", "subject", "hours_studied"])
    
    # the data that will be added to the row
    writer.writerow([student_name, subject, hours_studied])

print(f"Success! Entry saved to {filename}")