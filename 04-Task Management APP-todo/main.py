def task():
    tasks = []
    print(f"----Welcome to the Task Management App-------")

    total_tasks = int(input("Enter the number of tasks you want to add ="))

    for i in range(1 , total_tasks+1):
        task_name = input(f"Enter tasks {i} =")
        tasks.append(task_name)
    
    while True:
        operations = int(input(f"Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))

        if operations == 1:
            add = input("Enter the task you want to add =")
            tasks.append(add)
            print(f"The task {add} has been successfuly added")


        elif operations == 2:
            updated_val = input("Enter the task you want to update = ")

            if updated_val in tasks:
                up = input("Enter the new tasks ")
                ind = tasks.index(updated_val)
                tasks[ind]= up
                print(f"updated tasks{up}")

        elif operations == 3:
            del_val = input("Enter the tasks you want to delete =")

            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind] 
                print(f"The task {del_val} has been successfuly deleted")

        elif operations == 4:
            print(f"Total tasks = {tasks}")

        elif operations == 5:
            print("Thank you for using our Task-Management-App")
            break

task()

