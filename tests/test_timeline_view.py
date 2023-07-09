import unittest
from src.timeline_view import TimelineView

class TestTimelineView(unittest.TestCase):

    def setUp(self):
        self.timeline_view = TimelineView()

    def test_add_file(self):
        file = {'name': 'test_file', 'date': '2022-01-01', 'type': 'txt'}
        self.timeline_view.add_file(file)
        self.assertIn(file, self.timeline_view.userFiles)

    def test_remove_file(self):
        file = {'name': 'test_file', 'date': '2022-01-01', 'type': 'txt'}
        self.timeline_view.add_file(file)
        self.timeline_view.remove_file(file)
        self.assertNotIn(file, self.timeline_view.userFiles)

    def test_sort_files_by_date(self):
        file1 = {'name': 'test_file1', 'date': '2022-01-01', 'type': 'txt'}
        file2 = {'name': 'test_file2', 'date': '2022-01-02', 'type': 'txt'}
        self.timeline_view.add_file(file1)
        self.timeline_view.add_file(file2)
        sorted_files = self.timeline_view.sort_files_by_date()
        self.assertEqual(sorted_files, [file1, file2])

    def test_search_files_by_date(self):
        file1 = {'name': 'test_file1', 'date': '2022-01-01', 'type': 'txt'}
        file2 = {'name': 'test_file2', 'date': '2022-01-02', 'type': 'txt'}
        self.timeline_view.add_file(file1)
        self.timeline_view.add_file(file2)
        search_result = self.timeline_view.search_files_by_date('2022-01-01')
        self.assertEqual(search_result, [file1])

if __name__ == '__main__':
    unittest.main()