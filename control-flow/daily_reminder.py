# 4. Personal Daily Reminder
# mandatory
# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

# Task Description:

# Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

# Instructions:

# Prompt for a Single Task:

# Ask the user to input a task description and save it into a task variable
task = input("Enter your task: ")
# Prompt for the task’s priority (high, medium, low) and save it into a priority variable
priority = input("Priority (high/medium/low): ")
# In a time_bound variable, Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ")
# Process the Task Based on Priority and Time Sensitivity:

# Use a Match Case statement to react differently based on the task’s priority.
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high-priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high-priority task that requires your attention.")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a medium-priority task that needs to be completed soon.")
        else:
            print(f"Reminder: '{task}' is a medium-priority task. Put it on your to-do list.")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a low-priority task, but you should make some time for it.")
        else:
            print(f"Reminder: '{task}' is a low-priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid choice. Please select a valid priority (high/medium/low).")

# Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
# Provide a Customized Reminder:

# Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
# A message should be ‘that requires immediate attention today!’
# Example Interaction and Output:

# Enter your task: Finish project report
# Priority (high/medium/low): high
# Is it time-bound? (yes/no): yes

# Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
# Or, for a non-time-bound task:

# Enter your task: Read a book
# Priority (high/medium/low): low
# Is it time-bound? (yes/no): no

# Note: 'Read a book' is a low priority task. Consider completing it when you have free time.