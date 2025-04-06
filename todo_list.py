tasks =[]
def My_Tasks():
     print("/n To-Do list menu:")
     print("1.add task")
     print("2.view tasks")
     print("3.Remove the Task")
     print("4.mark task as Done")
     print("exit")
def add_Task():
     task=input("Add your Task:")    
     tasks.append({"task":task,"Done":False})
     print("Task added.")
def view_Tasks():
     if not tasks:
          print("Tasks are not added.")
          return
     for i,task in enumerate(tasks,start=1):
          status ="✅"if task["Done"]else"❌"
          print(f"{i}.{task['task']}[{status}]")

def complete_Task():
    view_Tasks()
    index = int(input("Enter task number to mark as Done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["Done"] = True
        print("Task marked as Done!")
    else:
        print("Invalid task number.")

def Remove_Task():
    view_Tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed Task: {removed['task']}")
    else:
        print("Invalid task number.")

while True:
    My_Tasks()
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        add_Task()
    elif choice == "2":
        view_Tasks()
    elif choice == "3":
        complete_Task()
    elif choice == "4":
        Remove_Task()
    elif choice == "5":
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")


