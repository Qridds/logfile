```python
import unittest
from src.storage_options import storeFile

class TestStorageOptions(unittest.TestCase):

    def setUp(self):
        self.file = {
            'name': 'test_file',
            'type': 'txt',
            'date': '2021-12-01',
            'tags': ['test', 'sample'],
            'content': 'This is a test file.'
        }

    def test_local_storage(self):
        result = storeFile(self.file, 'local')
        self.assertTrue(result)

    def test_cloud_storage(self):
        result = storeFile(self.file, 'cloud')
        self.assertTrue(result)

    def test_invalid_storage_option(self):
        with self.assertRaises(ValueError):
            storeFile(self.file, 'invalid_option')

if __name__ == '__main__':
    unittest.main()
```