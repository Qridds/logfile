import unittest
from src.audio_transcription import transcribeAudio

class TestAudioTranscription(unittest.TestCase):

    def setUp(self):
        self.sample_audio_file = "sample_audio.wav"
        self.transcribed_text = "This is a sample audio file for testing."

    def test_transcribeAudio(self):
        result = transcribeAudio(self.sample_audio_file)
        self.assertEqual(result, self.transcribed_text)

if __name__ == '__main__':
    unittest.main()