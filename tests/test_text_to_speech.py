```python
import unittest
from src.text_to_speech import TextToSpeech

class TestTextToSpeech(unittest.TestCase):

    def setUp(self):
        self.tts = TextToSpeech()

    def test_convert_text_to_speech(self):
        text = "Hello, world!"
        output_file = "hello_world.mp3"
        self.tts.convert_text_to_speech(text, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.tts.convert_text_to_speech(123, "test.mp3")

if __name__ == '__main__':
    unittest.main()
```