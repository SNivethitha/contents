print("SIMPLE TO-DO LIST")
class todo:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter task description: ")
        self.tasks.append({"task": task, "done": False})
        print("Task added!")

    def view_tasks(self):
        print("Tasks Scheduled :")
        for index, task in enumerate(self.tasks):
            status = "Done" if task["done"] else "Pending"
            print(f"{index + 1}. {task['task']} - {status}")

    def mark_task_done(self):
        self.view_tasks()
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    def remove_task(self):
        self.view_tasks()
        index = int(input("Enter the task number to remove task: ")) - 1
        if not self.tasks:
            print("No task to delete")
        elif 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            print("Task removed successfully")
        else:
            print("Invalid task number.")

    def save(self):
        inputfile = "data.txt"
        with open(inputfile, 'a') as filedata:
            filedata.write(str(self.tasks) + "\n")
        with open("data.txt") as filedata:
            print(filedata.read())

def main():
    To_Do = todo()
    while True:
        print("Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove task ")
        print("5. Save and Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            To_Do.add_task()
        elif choice == "2":
            To_Do.view_tasks()
        elif choice == "3":
            To_Do.mark_task_done()
        elif choice == "4":
            To_Do.remove_task()
        elif choice == "5":
            To_Do.save()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
