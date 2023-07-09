```python
import unittest
from src.cloud_storage import storeCloud

class TestCloudStorage(unittest.TestCase):

    def setUp(self):
        self.file = {
            'name': 'test_file.txt',
            'type': 'text',
            'date': '2021-12-01',
            'tags': ['test', 'cloud_storage'],
            'content': 'This is a test file for cloud storage.'
        }

    def test_storeCloud(self):
        result = storeCloud(self.file)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```