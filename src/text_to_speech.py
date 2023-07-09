```python
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def updateTask(task_id, new_text):
    global userTasks
    for task in userTasks:
        if task['id'] == task_id:
            task['text'] = new_text
            text_to_speech(new_text)
            return True
    return False
```