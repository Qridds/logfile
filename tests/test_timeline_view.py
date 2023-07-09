```python
import unittest
from src.timeline_view import TimelineView
from src.file_manager import FileManager

class TestTimelineView(unittest.TestCase):

    def setUp(self):
        self.file_manager = FileManager()
        self.timeline_view = TimelineView(self.file_manager)

    def test_initial_state(self):
        self.assertEqual(self.timeline_view.get_files(), [])

    def test_add_file(self):
        file = {
            'name': 'test_file',
            'type': 'txt',
            'date': '2021-01-01',
            'tags': ['test']
        }
        self.file_manager.uploadFile(file)
        self.assertEqual(self.timeline_view.get_files(), [file])

    def test_remove_file(self):
        file = {
            'name': 'test_file',
            'type': 'txt',
            'date': '2021-01-01',
            'tags': ['test']
        }
        self.file_manager.uploadFile(file)
        self.file_manager.removeFile(file['name'])
        self.assertEqual(self.timeline_view.get_files(), [])

    def test_sort_files_by_date(self):
        file1 = {
            'name': 'test_file1',
            'type': 'txt',
            'date': '2021-01-01',
            'tags': ['test']
        }
        file2 = {
            'name': 'test_file2',
            'type': 'txt',
            'date': '2021-02-01',
            'tags': ['test']
        }
        self.file_manager.uploadFile(file1)
        self.file_manager.uploadFile(file2)
        self.assertEqual(self.timeline_view.get_files(), [file1, file2])

if __name__ == '__main__':
    unittest.main()
```