import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tasks.append({"task": task, "timestamp": timestamp, "completed": False})

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task and not t["completed"]:
                t["completed"] = True
                print(f"Task '{task}' marked as completed.")
                return
        print(f"Task '{task}' not found or already completed.")

    def show_tasks(self):
        for t in self.tasks:
            status = "Completed" if t["completed"] else "Pending"
            print(f"{t['task']} - {status} (Added on {t['timestamp']})")

# Example Usage
todo = TodoList()
todo.add_task("Learn Python")
todo.add_task("Build a web app")
todo.show_tasks()
todo.complete_task("Learn Python")
todo.show_tasks()
