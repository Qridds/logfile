```python
import unittest
from src.search_function import searchFiles

class TestSearchFunction(unittest.TestCase):

    def setUp(self):
        self.userFiles = [
            {"name": "file1", "type": "doc", "date": "2021-01-01", "tags": ["work", "report"]},
            {"name": "file2", "type": "jpg", "date": "2021-02-01", "tags": ["holiday", "beach"]},
            {"name": "file3", "type": "mp3", "date": "2021-03-01", "tags": ["music", "rock"]},
        ]

    def test_search_by_word(self):
        result = searchFiles(self.userFiles, "file1")
        self.assertEqual(result, [self.userFiles[0]])

    def test_search_by_date(self):
        result = searchFiles(self.userFiles, "2021-02-01")
        self.assertEqual(result, [self.userFiles[1]])

    def test_search_by_tag(self):
        result = searchFiles(self.userFiles, "music")
        self.assertEqual(result, [self.userFiles[2]])

    def test_search_no_result(self):
        result = searchFiles(self.userFiles, "nonexistent")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
```