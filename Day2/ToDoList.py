# 1) add tasks to a list
# 2) mark task as complete
# 3) view tasks
# 4) close the program

tasks = [
{"task":"Quran", "completed":True}, 
{"task":"Salah", "completed":True}, 
{"task":"Study", "completed":False},
{"task":"Exercise", "completed":False}, 
{"task":"Sleep", "completed":False}, 
{"task":"Play Games", "completed":False}
]



def main():
    message = '''1) add tasks to a list
2) mark task as complete
3) view tasks
4) close the program'''


    while True:
        print(message)
        choice = input("Enter your choice: ")
        if choice == '1':
            # add task to tasks list
            add_task()
        elif choice == '2':
            # marks task as complete
            mark_task_complete()
        elif choice == '3':
            #view tasks
            view_tasks(tasks)
        elif choice == '4':
            # close the program
            print("you closed the program :<")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4")


def add_task():
    # get task from user
    task = input("Enter task: ")
    # define task status
    task_info = {"task" : task , "completed" : False}
    # add task to the list of tasks
    tasks.append(task_info)
    print("Task added to the list successfuly")
    # ... same as pass


def mark_task_complete():
    # get list of incomplete tasks
    incomplete_tasks = [task for task in tasks if task["completed"] == False]

    #in case no incompleted tasks
    if not incomplete_tasks:
        print("No tasks to mark as complete")
        return
    
    # show the list to the user
    for i, task in enumerate(incomplete_tasks):
        print(f"{i+1}- {task['task']}")
        print('-'*30)

    # get the task you want to mark from the user
    try:
        task_number = int(input("choose the task number you completed: "))
        if task_number < 1 or task_number > len(incomplete_tasks):
            print("Invalind task number")
            return

        # mark the task as completed
        #aliasing
        incomplete_tasks[task_number-1]["completed" ] = True

        # print the message to the user
        print("Task marked as completed")
    except ValueError:
        print("Invalid input, please enter a number")
    
 
def view_tasks(tasks_list):
    # if there are no tasks to view print a message and return
    if not tasks_list:
        print("No tasks to view")
        return
    
    # view list like this:
    # 1. Read Quran ✔️
    # 2. Salah ✔️
    # 3. play games ❌
    for i, task in enumerate(tasks_list):
        status = "✔️" if task['completed'] else "❌"
        print(f"{i+1}. {task['task']} {status}")


if __name__ == "__main__":
    main()