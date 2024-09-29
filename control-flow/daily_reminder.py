task_description = input("Enter your task: ")
priotity = input("Priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priotity:
    case "high":
        if time_bound == "yes":
            print(f" Remider: '{task_description}' is a high piority task that requires immediate attention today!")
        else:
            print(f" Note: '{task_description}' is a high piority task. Consider completing it when you have free time.")

    case "medium":
        if time_bound == "yes":
            print(f" Remider: '{task_description}' is a medium piority task that requires immediate attention today!")
        else:
            print(f" Note: '{task_description}' is a medium piority task. Consider completing it when you have free time.")

    case "low":
        if time_bound == "yes":
            print(f" Remider: '{task_description}' is a low piority task that requires immediate attention today!")
        else:
            print(f" Note: '{task_description}' is a low piority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered!")