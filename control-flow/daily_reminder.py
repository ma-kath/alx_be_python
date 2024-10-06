task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f" Remider: '{task}' is a high piority task that requires immediate attention today!")
        else:
            print(f" Note: '{task}' is a high piority task. Consider completing it when you have free time.")

    case "medium":
        if time_bound == "yes":
            print(f" Remider: '{task}' is a medium piority task that requires immediate attention today!")
        else:
            print(f" Note: '{task}' is a medium piority task. Consider completing it when you have free time.")

    case "low":
        if time_bound == "yes":
            print(f" Remider: '{task}' is a low piority task that requires immediate attention today!")
        else:
            print(f" Note: '{task}' is a low piority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered!")
