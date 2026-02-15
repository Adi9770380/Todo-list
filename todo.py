tasks=[]
try:
    file=open("tasks.txt","r")
    for line in file:
        tasks.append(line.strip())
        file.close()
except:
    pass
while True:
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        task=input("Enter the task:")
        tasks.append(task)
        file=open("tasks.txt","w")
        for t in tasks:
            file.write(t+"\n")
        file.close()
        print("Task added successfully")
    elif choice==2:
        for i in range(len(tasks)):
            print(i+1,tasks[i])
    elif choice==3:
        for i in range(len(tasks)):
            print(i+1,tasks[i])
        num=int(input("Enter number to remove:"))
        tasks.pop(num-1)
        file=open("tasks.txt","w")
        for t in tasks:
            file .write(t+"\n")
        file.close()
        print("Task removed")
    elif choice==4:
        print("Exit")
        break
    else:
        print("Invalid choice")
            
            
        
        