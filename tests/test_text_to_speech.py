import unittest
from src.text_to_speech import textToSpeech

class TestTextToSpeech(unittest.TestCase):

    def setUp(self):
        self.sample_text = "This is a sample text for testing."

    def test_text_to_speech(self):
        audio_output = textToSpeech(self.sample_text)
        self.assertIsNotNone(audio_output)

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            textToSpeech("")

if __name__ == '__main__':
    unittest.main()