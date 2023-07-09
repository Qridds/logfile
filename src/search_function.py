```python
import re
from typing import List, Dict

from file_manager import userFiles, FileSchema

def searchFiles(query: str, search_by: str = 'words') -> List[Dict]:
    """
    Function to search files based on words, dates or custom tags.
    """
    results = []

    if search_by == 'words':
        for file in userFiles:
            if re.search(query, file['name'], re.I):
                results.append(file)
    elif search_by == 'dates':
        for file in userFiles:
            if file['date'] == query:
                results.append(file)
    elif search_by == 'tags':
        for file in userFiles:
            if query in file['tags']:
                results.append(file)

    return results
```