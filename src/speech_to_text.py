```python
import speech_recognition as sr

def speechToText(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

def updateFile(file, text):
    file['content'] = text
    return file
```