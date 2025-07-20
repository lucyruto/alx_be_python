# Prompt for task details
task = input("Enter your task for today: ")
priority = input("What is the priority level? (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Use match-case to handle priority
match priority:
    case "high":
        message = f"🔔 High Priority: {task}."
    case "medium":
        message = f"📌 Medium Priority: {task}."
    case "low":
        message = f"📝 Low Priority: {task}."
    case _:
        message = f"⚠️ Unknown priority. Task: {task}."

# Add time-sensitivity message if needed
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Print the final reminder
print("\nDaily Reminder:")
print(message)
