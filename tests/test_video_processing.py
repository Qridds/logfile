```python
import unittest
from src.video_processing import processVideo

class TestVideoProcessing(unittest.TestCase):

    def setUp(self):
        self.test_video = {
            "name": "test_video.mp4",
            "type": "video",
            "date": "2022-01-01",
            "tags": ["test", "video"]
        }

    def test_process_video(self):
        result = processVideo(self.test_video)
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "test_video.mp4")
        self.assertEqual(result["type"], "video")
        self.assertIn("processed", result["tags"])

if __name__ == '__main__':
    unittest.main()
```