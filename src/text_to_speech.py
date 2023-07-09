```python
import pyttsx3

def textToSpeech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def updateTask(task):
    global userTasks
    for i, t in enumerate(userTasks):
        if t['id'] == task['id']:
            userTasks[i] = task
            textToSpeech(f"Task {task['name']} has been updated.")
            return
    raise Exception("Task not found.")

def createTask(task):
    global userTasks
    userTasks.append(task)
    textToSpeech(f"Task {task['name']} has been created.")
```
