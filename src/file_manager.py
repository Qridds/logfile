```python
import os
from datetime import datetime

userFiles = []

class FileSchema:
    def __init__(self, filename, filetype, date, tags):
        self.filename = filename
        self.filetype = filetype
        self.date = date
        self.tags = tags

def uploadFile(filepath, tags):
    filename, filetype = os.path.splitext(filepath)
    date = datetime.now()
    newFile = FileSchema(filename, filetype, date, tags)
    userFiles.append(newFile)
    return newFile

def updateFile(file, newTags=None, newDate=None):
    if newTags:
        file.tags = newTags
    if newDate:
        file.date = newDate
    return file

def searchFiles(query):
    results = []
    for file in userFiles:
        if query in file.filename or query in file.tags:
            results.append(file)
    return results

def storeLocal(file, path):
    os.rename(file.filename + file.filetype, path + file.filename + file.filetype)

def storeCloud(file, cloudService):
    # This function will depend on the specific cloud service API
    pass
```