```python
import datetime
from plyer import notification

userTasks = []

class TaskSchema:
    def __init__(self, name, date, reminder_settings):
        self.name = name
        self.date = date
        self.reminder_settings = reminder_settings

def createTask(name, date, reminder_settings):
    new_task = TaskSchema(name, date, reminder_settings)
    userTasks.append(new_task)

def updateTask(task, name=None, date=None, reminder_settings=None):
    if name:
        task.name = name
    if date:
        task.date = date
    if reminder_settings:
        task.reminder_settings = reminder_settings

def setReminder(task):
    if datetime.datetime.now() >= task.date - datetime.timedelta(minutes=task.reminder_settings):
        notification.notify(
            title = 'Reminder',
            message = f'Task {task.name} is due soon!',
            timeout = 10,
        )

def checkReminders():
    for task in userTasks:
        setReminder(task)
```
This code creates a reminder system for the digital organizer. It uses the plyer library to send notifications to the user. The `TaskSchema` class defines the structure of a task, including its name, due date, and reminder settings. The `createTask` function creates a new task and adds it to the `userTasks` list. The `updateTask` function allows the user to update the details of a task. The `setReminder` function checks if a task is due soon based on its reminder settings and sends a notification if it is. The `checkReminders` function checks all tasks for upcoming due dates.