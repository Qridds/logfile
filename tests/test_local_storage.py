```python
import unittest
from src.local_storage import storeLocal

class TestLocalStorage(unittest.TestCase):

    def setUp(self):
        self.file = {
            'type': 'document',
            'date': '2021-12-01',
            'tags': ['work', 'important'],
            'content': 'This is a test document.'
        }

    def test_storeLocal(self):
        result = storeLocal(self.file)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```