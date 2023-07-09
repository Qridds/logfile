```python
import unittest
from src.file_manager import uploadFile, updateFile, userFiles, FileSchema

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.file = {
            'type': 'document',
            'date': '2021-12-01',
            'tags': ['work', 'report'],
            'name': 'work_report.docx'
        }

    def test_uploadFile(self):
        uploadFile(self.file)
        self.assertIn(self.file, userFiles)

    def test_updateFile(self):
        new_file = {
            'type': 'document',
            'date': '2021-12-02',
            'tags': ['work', 'report', 'updated'],
            'name': 'work_report.docx'
        }
        updateFile(self.file['name'], new_file)
        self.assertIn(new_file, userFiles)
        self.assertNotIn(self.file, userFiles)

    def test_FileSchema(self):
        file_schema = FileSchema()
        result = file_schema.load(self.file)
        self.assertEqual(result, self.file)

if __name__ == '__main__':
    unittest.main()
```