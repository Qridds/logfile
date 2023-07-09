```python
import os
from datetime import datetime

# Shared variables
userFiles = []
userTasks = []
userPreferences = {}

# File schema
class FileSchema:
    def __init__(self, name, type, date, tags):
        self.name = name
        self.type = type
        self.date = date
        self.tags = tags

# Function to upload a new file
def uploadFile(filePath):
    try:
        # Extract metadata
        name = os.path.basename(filePath)
        type = os.path.splitext(name)[1]
        date = datetime.fromtimestamp(os.path.getmtime(filePath))
        tags = []

        # Create a new file object
        file = FileSchema(name, type, date, tags)

        # Add the file to the list of user files
        userFiles.append(file)

        # Send a message that a new file has been uploaded
        print("fileUploaded")

    except Exception as e:
        print(f"An error occurred while uploading the file: {e}")

# Function to update an existing file
def updateFile(file, newFilePath):
    try:
        # Update the file's metadata
        file.name = os.path.basename(newFilePath)
        file.type = os.path.splitext(file.name)[1]
        file.date = datetime.fromtimestamp(os.path.getmtime(newFilePath))

        # Send a message that the file has been updated
        print("fileUpdated")

    except Exception as e:
        print(f"An error occurred while updating the file: {e}")

# Function to store a file
def storeFile(file, location):
    try:
        # Check if the location is local or cloud
        if location == "local":
            # Store the file locally
            pass
        elif location == "cloud":
            # Store the file in the cloud
            pass

        # Send a message that the file has been stored
        print("fileStored")

    except Exception as e:
        print(f"An error occurred while storing the file: {e}")
```