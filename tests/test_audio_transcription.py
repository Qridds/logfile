```python
import unittest
from src.audio_transcription import transcribeAudio

class TestAudioTranscription(unittest.TestCase):

    def setUp(self):
        self.sample_audio_file = "sample_audio.wav"

    def test_transcribeAudio(self):
        result = transcribeAudio(self.sample_audio_file)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
```