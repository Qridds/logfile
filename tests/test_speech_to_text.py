```python
import unittest
from src.speech_to_text import SpeechToText

class TestSpeechToText(unittest.TestCase):

    def setUp(self):
        self.speech_to_text = SpeechToText()

    def test_transcribe(self):
        audio_file = 'path/to/audio/file'
        expected_transcription = 'This is a test audio file.'
        self.assertEqual(self.speech_to_text.transcribe(audio_file), expected_transcription)

    def test_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            self.speech_to_text.transcribe('invalid/path')

    def test_empty_file(self):
        empty_audio_file = 'path/to/empty/audio/file'
        self.assertEqual(self.speech_to_text.transcribe(empty_audio_file), '')

if __name__ == '__main__':
    unittest.main()
```