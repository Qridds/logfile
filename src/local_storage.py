```python
import os
import shutil
from file_manager import userFiles, FileSchema

def storeLocal(file: FileSchema, destination: str):
    """
    Function to store a file locally.
    :param file: File to be stored.
    :param destination: Local destination to store the file.
    """
    try:
        # Check if destination directory exists, if not, create it
        if not os.path.exists(destination):
            os.makedirs(destination)

        # Copy the file to the destination
        shutil.copy2(file.path, destination)

        # Update the file's path in the userFiles list
        for userFile in userFiles:
            if userFile.id == file.id:
                userFile.path = os.path.join(destination, os.path.basename(file.path))
                break

        print(f"File {file.name} stored locally at {destination}")

    except Exception as e:
        print(f"An error occurred while storing the file locally: {str(e)}")
```