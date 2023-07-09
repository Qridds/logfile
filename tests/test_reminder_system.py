import unittest
from src.reminder_system import setReminder, updateTask

class TestReminderSystem(unittest.TestCase):

    def setUp(self):
        self.userTasks = []
        self.task1 = {"name": "Task 1", "date": "2022-01-01", "reminder": "2022-01-01 10:00:00"}
        self.task2 = {"name": "Task 2", "date": "2022-02-01", "reminder": "2022-02-01 10:00:00"}

    def test_setReminder(self):
        setReminder(self.task1, self.userTasks)
        self.assertEqual(len(self.userTasks), 1)
        self.assertEqual(self.userTasks[0]['name'], "Task 1")

    def test_updateTask(self):
        setReminder(self.task1, self.userTasks)
        self.task1["reminder"] = "2022-01-01 11:00:00"
        updateTask(self.task1, self.userTasks)
        self.assertEqual(self.userTasks[0]['reminder'], "2022-01-01 11:00:00")

    def test_multipleReminders(self):
        setReminder(self.task1, self.userTasks)
        setReminder(self.task2, self.userTasks)
        self.assertEqual(len(self.userTasks), 2)

    def test_noReminder(self):
        self.task1["reminder"] = None
        setReminder(self.task1, self.userTasks)
        self.assertEqual(self.userTasks[0]['reminder'], None)

if __name__ == '__main__':
    unittest.main()