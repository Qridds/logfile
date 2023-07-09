```python
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

userFiles = []
userTasks = []
userPreferences = {}

def load_files():
    global userFiles
    if os.path.exists('userFiles.json'):
        with open('userFiles.json', 'r') as f:
            userFiles = json.load(f)

def save_files():
    with open('userFiles.json', 'w') as f:
        json.dump(userFiles, f)

def ai_analysis(file_id, query):
    load_files()
    file_texts = [file['text'] for file in userFiles if 'text' in file]
    file_ids = [file['id'] for file in userFiles if 'text' in file]

    if not file_texts:
        return []

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(file_texts)

    query_tfidf = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_tfidf, tfidf).flatten()

    related_file_indices = cosine_similarities.argsort()[:-6:-1]
    related_files = [file_ids[i] for i in related_file_indices]

    return related_files

def update_file(file_id, new_text):
    global userFiles
    for file in userFiles:
        if file['id'] == file_id:
            file['text'] = new_text
            save_files()
            return True
    return False
```