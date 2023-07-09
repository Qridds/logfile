```python
import unittest
from src.storage_options import storeLocal, storeCloud

class TestStorageOptions(unittest.TestCase):

    def setUp(self):
        self.file = {
            'name': 'test_file',
            'type': 'txt',
            'content': 'This is a test file.'
        }

    def test_storeLocal(self):
        result = storeLocal(self.file)
        self.assertTrue(result)

    def test_storeCloud(self):
        result = storeCloud(self.file)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```