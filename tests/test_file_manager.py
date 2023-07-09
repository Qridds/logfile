import unittest
from src.file_manager import uploadFile, updateFile, searchFiles, storeFile

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.userFiles = []
        self.FileSchema = {
            'name': '',
            'type': '',
            'date': '',
            'tags': []
        }

    def test_uploadFile(self):
        uploadFile(self.userFiles, self.FileSchema, 'test_file', 'txt', '2022-01-01', ['test'])
        self.assertEqual(len(self.userFiles), 1)
        self.assertEqual(self.userFiles[0]['name'], 'test_file')

    def test_updateFile(self):
        uploadFile(self.userFiles, self.FileSchema, 'test_file', 'txt', '2022-01-01', ['test'])
        updateFile(self.userFiles, 'test_file', 'updated_file', 'txt', '2022-01-02', ['updated'])
        self.assertEqual(self.userFiles[0]['name'], 'updated_file')

    def test_searchFiles(self):
        uploadFile(self.userFiles, self.FileSchema, 'test_file', 'txt', '2022-01-01', ['test'])
        uploadFile(self.userFiles, self.FileSchema, 'another_file', 'txt', '2022-01-02', ['another'])
        result = searchFiles(self.userFiles, 'test')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'test_file')

    def test_storeFile(self):
        uploadFile(self.userFiles, self.FileSchema, 'test_file', 'txt', '2022-01-01', ['test'])
        storeFile(self.userFiles, 'test_file', 'local')
        self.assertEqual(self.userFiles[0]['storage'], 'local')

if __name__ == '__main__':
    unittest.main()