```python
import speech_recognition as sr

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text

def save_transcription(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)

def speech_to_text(audio_file, transcription_file):
    transcription = transcribe_audio(audio_file)
    save_transcription(transcription_file, transcription)
```