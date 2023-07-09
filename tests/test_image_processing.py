```python
import unittest
from src.image_processing import processImage

class TestImageProcessing(unittest.TestCase):

    def setUp(self):
        self.test_image = "test_image.jpg"
        self.processed_image = "processed_image.jpg"

    def test_processImage(self):
        processImage(self.test_image, self.processed_image)
        self.assertTrue(os.path.exists(self.processed_image))

        # Check if the processed image is not the same as the original
        with open(self.test_image, 'rb') as file1:
            with open(self.processed_image, 'rb') as file2:
                self.assertNotEqual(file1.read(), file2.read())

if __name__ == '__main__':
    unittest.main()
```