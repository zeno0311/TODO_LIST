class ToDoList:
    def __init__(self):
        self.tasks = []

    # method to add task
    def add_task(self, task):
        self.tasks.append({"description": task, "completed": False})

    # method to remove task
    def remove_task(self, task):
        for t in self.tasks:
            if t["description"] == task:
                self.tasks.remove(t)
                break

    #method to mark the task as completed
    def mark_completed(self, task):
        for t in self.tasks:
            if t["description"] == task:
                t["completed"] = True
                break
    
    #method to display list
    def display_list(self):
        for t in self.tasks:
            status = "Completed" if t["completed"] else "Not Completed"
            print(f"{t['description']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display List")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task description: ")
            todo_list.remove_task(task)
        elif choice == "3":
            task = input("Enter task description: ")
            todo_list.mark_completed(task)
        elif choice == "4":
            todo_list.display_list()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
