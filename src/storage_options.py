```python
import os
import shutil
from cloud_storage import CloudStorage

class StorageOptions:
    def __init__(self):
        self.local_path = "/local/storage/path"
        self.cloud_storage = CloudStorage()

    def store_file(self, file, storage_type):
        if storage_type == "local":
            self.store_local(file)
        elif storage_type == "cloud":
            self.store_cloud(file)
        else:
            print("Invalid storage type. Please choose 'local' or 'cloud'.")

    def store_local(self, file):
        destination = os.path.join(self.local_path, file['name'])
        shutil.copyfile(file['path'], destination)
        print(f"File {file['name']} stored locally.")

    def store_cloud(self, file):
        self.cloud_storage.upload_file(file)
        print(f"File {file['name']} stored in cloud.")

    def retrieve_file(self, file_name, storage_type):
        if storage_type == "local":
            return self.retrieve_local(file_name)
        elif storage_type == "cloud":
            return self.retrieve_cloud(file_name)
        else:
            print("Invalid storage type. Please choose 'local' or 'cloud'.")

    def retrieve_local(self, file_name):
        file_path = os.path.join(self.local_path, file_name)
        if os.path.exists(file_path):
            return file_path
        else:
            print(f"File {file_name} not found in local storage.")

    def retrieve_cloud(self, file_name):
        return self.cloud_storage.download_file(file_name)
```
