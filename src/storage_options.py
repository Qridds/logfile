```python
import os
import shutil
from src.local_storage import LocalStorage
from src.cloud_storage import CloudStorage

class StorageOptions:
    def __init__(self):
        self.local_storage = LocalStorage()
        self.cloud_storage = CloudStorage()

    def store_file(self, file, location):
        if location == 'local':
            self.local_storage.store(file)
        elif location == 'cloud':
            self.cloud_storage.store(file)
        else:
            raise ValueError("Invalid storage location. Choose 'local' or 'cloud'.")

    def retrieve_file(self, file_id, location):
        if location == 'local':
            return self.local_storage.retrieve(file_id)
        elif location == 'cloud':
            return self.cloud_storage.retrieve(file_id)
        else:
            raise ValueError("Invalid storage location. Choose 'local' or 'cloud'.")

    def delete_file(self, file_id, location):
        if location == 'local':
            self.local_storage.delete(file_id)
        elif location == 'cloud':
            self.cloud_storage.delete(file_id)
        else:
            raise ValueError("Invalid storage location. Choose 'local' or 'cloud'.")
```