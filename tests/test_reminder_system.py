```python
import unittest
from src.reminder_system import setReminder, userTasks

class TestReminderSystem(unittest.TestCase):

    def setUp(self):
        self.task1 = {
            'id': 1,
            'name': 'Test Task 1',
            'date': '2022-01-01',
            'reminders': [],
            'associated_files': []
        }
        self.task2 = {
            'id': 2,
            'name': 'Test Task 2',
            'date': '2022-02-01',
            'reminders': [],
            'associated_files': []
        }
        userTasks.append(self.task1)
        userTasks.append(self.task2)

    def tearDown(self):
        userTasks.clear()

    def test_setReminder(self):
        setReminder(1, '2022-01-01 10:00:00')
        self.assertEqual(userTasks[0]['reminders'][0], '2022-01-01 10:00:00')

        setReminder(2, '2022-02-01 15:00:00')
        self.assertEqual(userTasks[1]['reminders'][0], '2022-02-01 15:00:00')

if __name__ == '__main__':
    unittest.main()
```