```python
import unittest
from src import user_interface

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.ui = user_interface.UserInterface()

    def test_fileListView(self):
        self.assertIsNotNone(self.ui.fileListView)

    def test_taskListView(self):
        self.assertIsNotNone(self.ui.taskListView)

    def test_searchBar(self):
        self.assertIsNotNone(self.ui.searchBar)

    def test_fileUploadButton(self):
        self.assertIsNotNone(self.ui.fileUploadButton)

    def test_taskCreateButton(self):
        self.assertIsNotNone(self.ui.taskCreateButton)

    def test_uploadFile(self):
        test_file = "test.txt"
        self.ui.uploadFile(test_file)
        self.assertIn(test_file, self.ui.userFiles)

    def test_createTask(self):
        test_task = "Test Task"
        self.ui.createTask(test_task)
        self.assertIn(test_task, self.ui.userTasks)

    def test_updateFile(self):
        test_file = "test.txt"
        self.ui.uploadFile(test_file)
        updated_file = "updated_test.txt"
        self.ui.updateFile(test_file, updated_file)
        self.assertIn(updated_file, self.ui.userFiles)
        self.assertNotIn(test_file, self.ui.userFiles)

    def test_updateTask(self):
        test_task = "Test Task"
        self.ui.createTask(test_task)
        updated_task = "Updated Test Task"
        self.ui.updateTask(test_task, updated_task)
        self.assertIn(updated_task, self.ui.userTasks)
        self.assertNotIn(test_task, self.ui.userTasks)

    def test_searchFiles(self):
        test_file = "test.txt"
        self.ui.uploadFile(test_file)
        search_result = self.ui.searchFiles("test")
        self.assertIn(test_file, search_result)

if __name__ == '__main__':
    unittest.main()
```