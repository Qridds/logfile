```python
import unittest
from src.ocr_module import OCRModule

class TestOCRModule(unittest.TestCase):

    def setUp(self):
        self.ocr_module = OCRModule()
        self.test_file = 'test_file.pdf'

    def test_scan_document(self):
        result = self.ocr_module.scan_document(self.test_file)
        self.assertIsInstance(result, str)

    def test_summarize_document(self):
        result = self.ocr_module.summarize_document(self.test_file)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
```