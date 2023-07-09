```python
import re

userFiles = []  # This will be populated with FileSchema objects

class FileSchema:
    def __init__(self, type, date, tags, content):
        self.type = type
        self.date = date
        self.tags = tags
        self.content = content

def searchFiles(query):
    results = []
    for file in userFiles:
        if re.search(query, file.content, re.I):
            results.append(file)
        elif query in file.tags:
            results.append(file)
        elif query in str(file.date):
            results.append(file)
    return results
```