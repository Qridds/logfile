```python
import datetime
from src.file_manager import userFiles, FileSchema

def sort_files_by_date():
    return sorted(userFiles, key=lambda x: x.date, reverse=True)

def display_files_in_timeline():
    sorted_files = sort_files_by_date()
    for file in sorted_files:
        print(f"Date: {file.date.strftime('%Y-%m-%d')}, File: {file.name}")

def filter_files_by_date(date):
    return [file for file in userFiles if file.date.date() == date]

def display_files_on_date(date):
    files_on_date = filter_files_by_date(date)
    for file in files_on_date:
        print(f"Date: {file.date.strftime('%Y-%m-%d')}, File: {file.name}")

def timeline_view():
    print("Timeline View:")
    display_files_in_timeline()

def timeline_view_on_date(date):
    print(f"Timeline View on {date.strftime('%Y-%m-%d')}:")
    display_files_on_date(date)
```