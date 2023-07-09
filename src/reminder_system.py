```python
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

userTasks = []

class Task:
    def __init__(self, title, description, due_date, reminder_time):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.reminder_time = reminder_time

def createTask(title, description, due_date, reminder_time):
    new_task = Task(title, description, due_date, reminder_time)
    userTasks.append(new_task)
    setReminder(new_task)

def updateTask(task, title=None, description=None, due_date=None, reminder_time=None):
    if title:
        task.title = title
    if description:
        task.description = description
    if due_date:
        task.due_date = due_date
    if reminder_time:
        task.reminder_time = reminder_time
    setReminder(task)

def setReminder(task):
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: print(f"Reminder: {task.title} is due on {task.due_date}"), 'date', run_date=task.reminder_time)
    scheduler.start()

def removeTask(task):
    userTasks.remove(task)
    print(f"Task {task.title} removed.")
```