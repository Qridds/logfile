import unittest
from src.speech_to_text import speechToText

class TestSpeechToText(unittest.TestCase):

    def setUp(self):
        self.sample_audio = "sample_audio.wav"
        self.expected_text = "This is a sample audio file for testing."

    def test_speech_to_text(self):
        result_text = speechToText(self.sample_audio)
        self.assertEqual(result_text, self.expected_text)

if __name__ == '__main__':
    unittest.main()