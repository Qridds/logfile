import unittest
from src.image_processing import processImage

class TestImageProcessing(unittest.TestCase):

    def setUp(self):
        self.test_image = {
            'name': 'test_image.jpg',
            'type': 'image',
            'date': '2021-12-01',
            'tags': ['test', 'image'],
            'path': '/path/to/test_image.jpg'
        }

    def test_process_image(self):
        result = processImage(self.test_image)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'test_image.jpg')
        self.assertEqual(result['type'], 'image')
        self.assertIn('processed', result['tags'])

    def test_process_image_no_image(self):
        with self.assertRaises(TypeError):
            processImage(None)

    def test_process_image_invalid_type(self):
        with self.assertRaises(ValueError):
            processImage({'name': 'test.txt', 'type': 'text'})

if __name__ == '__main__':
    unittest.main()