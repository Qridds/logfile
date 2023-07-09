```python
import unittest
from src.video_processing import processVideo

class TestVideoProcessing(unittest.TestCase):

    def setUp(self):
        self.test_video = "test_video.mp4"
        self.processed_video = "processed_video.mp4"

    def test_processVideo(self):
        processVideo(self.test_video, self.processed_video)
        self.assertTrue(os.path.exists(self.processed_video))

    def tearDown(self):
        os.remove(self.processed_video)

if __name__ == '__main__':
    unittest.main()
```