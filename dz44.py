class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Виконано" if self.completed else "Не виконано"
        return f"Завдання: {self.title}\nОпис: {self.description}\nДедлайн: {self.deadline}\nСтан: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        new_task = Task(title, description, deadline)
        self.tasks.append(new_task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()

    def show_tasks(self):
        if not self.tasks:
            print("Немає завдань.")
        for task in self.tasks:
            print(task)
            print("-" * 40)

# Приклад використання
task_manager = TaskManager()
task_manager.add_task("Завдання 1", "Опис завдання 1", "2025-04-30")
task_manager.add_task("Завдання 2", "Опис завдання 2", "2025-05-05")

task_manager.show_tasks()

task_manager.mark_task_completed("Завдання 1")
task_manager.show_tasks()

task_manager.remove_task("Завдання 2")
task_manager.show_tasks()
