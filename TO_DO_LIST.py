def create_tasks(task_name, index):
    tasks.insert(index,task_name)
    print("Task Added:", task_name)
    return tasks

def update_tasks(index, new_task):
    tasks[index]=new_task
    print("Updated:", new_task)
    return tasks

def delete_task(index):
    task_name=tasks[index]
    tasks.pop(index)
    print("Deleted:", task_name)

def track_tasks(tasks):
    print("-~-To-Do List-~-")
    i=1
    for task in tasks:
        print(i, end=". ")
        print(task)
        i+=1
    return tasks

tasks=[]

while True:
    print("TO-DO LIST")
    print("1. ADD A NEW TASK")
    print("2. UPDATE AN EXISTING TASK")
    print("3. DELETE AN EXISTING TASK")
    print("4. TRACK YOUR TO-DO LIST")
    print("5. Exit.")
    choice = int(input("Enter your choice:- "))
    if choice==1:
        task_name=input("Enter your task:-")
        inp=input("Do you want to add your task at a specific position? (y/n)")
        if inp=="y":
            index=int(input("Enter the position:-"))-1
        else:
            index=len(tasks)
        create_tasks(task_name,index)
        continue
    elif choice==2:
        index=int(input("Enter the task's number to be updated:-"))
        new_task=input("Enter the new task:-")
        update_tasks(index-1,new_task)
        continue
    elif choice==3:
        index=int(input("Enter the task's number to be deleted:-"))
        delete_task(index-1)
        continue
    elif choice==4:
        track_tasks(tasks)
        continue
    elif choice==5:
        break
    else:
        print("Invalid choice.")
        print("Try again!")
    
print("Exiting from your To-Do List. It was nice serving you!")