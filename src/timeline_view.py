```python
import datetime
from src.file_manager import userFiles

def sort_files_by_date():
    sorted_files = sorted(userFiles, key=lambda x: x['date'], reverse=True)
    return sorted_files

def display_files_in_timeline(sorted_files):
    for file in sorted_files:
        print(f"Date: {file['date'].strftime('%Y-%m-%d')}, File: {file['name']}")

def timeline_view():
    sorted_files = sort_files_by_date()
    display_files_in_timeline(sorted_files)

if __name__ == "__main__":
    timeline_view()
```