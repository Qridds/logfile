```python
import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = main.DigitalOrganizer()

    def test_uploadFile(self):
        result = self.app.uploadFile('test.txt')
        self.assertEqual(result, 'File uploaded successfully')

    def test_createTask(self):
        result = self.app.createTask('Test Task')
        self.assertEqual(result, 'Task created successfully')

    def test_updateFile(self):
        self.app.uploadFile('test.txt')
        result = self.app.updateFile('test.txt')
        self.assertEqual(result, 'File updated successfully')

    def test_updateTask(self):
        self.app.createTask('Test Task')
        result = self.app.updateTask('Test Task')
        self.assertEqual(result, 'Task updated successfully')

    def test_searchFiles(self):
        self.app.uploadFile('test.txt')
        result = self.app.searchFiles('test')
        self.assertEqual(result, ['test.txt'])

    def test_setReminder(self):
        self.app.createTask('Test Task')
        result = self.app.setReminder('Test Task', '2022-12-31')
        self.assertEqual(result, 'Reminder set successfully')

    def test_processImage(self):
        result = self.app.processImage('test.jpg')
        self.assertEqual(result, 'Image processed successfully')

    def test_processVideo(self):
        result = self.app.processVideo('test.mp4')
        self.assertEqual(result, 'Video processed successfully')

    def test_transcribeAudio(self):
        result = self.app.transcribeAudio('test.mp3')
        self.assertEqual(result, 'Audio transcribed successfully')

    def test_storeLocal(self):
        self.app.uploadFile('test.txt')
        result = self.app.storeLocal('test.txt')
        self.assertEqual(result, 'File stored locally successfully')

    def test_storeCloud(self):
        self.app.uploadFile('test.txt')
        result = self.app.storeCloud('test.txt')
        self.assertEqual(result, 'File stored in cloud successfully')

if __name__ == '__main__':
    unittest.main()
```