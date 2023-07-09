import unittest
from src.ocr_ai_analysis import ocrScan

class TestOCRAnalysis(unittest.TestCase):

    def setUp(self):
        self.sample_files = [
            {"name": "doc1", "type": "pdf", "content": "This is a sample document."},
            {"name": "doc2", "type": "jpg", "content": "This is a sample image."},
            {"name": "doc3", "type": "png", "content": "This is another sample image."}
        ]

    def test_ocrScan(self):
        for file in self.sample_files:
            result = ocrScan(file)
            self.assertIsNotNone(result)
            self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()