task = input ("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print("Note: '{task}' is a low priority task. Consider completing it when you have free time")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed soon.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time")
    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be done later.")
        