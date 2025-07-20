task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is is time-bound? (yes/no): ")

match priority:
    case "high":
        if time == "yes":
            print(f"Reminder:'{task}' is a highly priority task that requires immediate attention today!")
        else:
            print("Please finish it as the first task")
    case "medium":
        if time == "no":
            print(f"NB: '{task}' is medium priority and can be done in 2 days")
        else:
            print("Finish it after the high priority task")
    case "low":
        if time == "no":
            print(f"Note:'{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("You can finish this after the medium priority work")
    case _:
        print(f" All your tasks are done")
