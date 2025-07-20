task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder:'{task}' is a highly priority task that requires immediate attention today!")
        else:
            print("Please finish it as the first task")
    case "medium":
        if time_bound == "no":
            print(f"NB: '{task}' is medium priority and can be done in 2 days")
        else:
            print("Finish it after the high priority task")
    case "low":
        if time_bound == "no":
            print(f"Note:'{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("You can finish this after the medium priority work")
    case _:
        print(" All your tasks are done")
