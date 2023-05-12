import unittest
import os
from file_utils import get_size, check_file_type, get_space_details
from draw_utils import prepare_data_for_chart, make_autopct


class TestUtils(unittest.TestCase):

    def test_get_size(self):
        size = get_size(os.path.dirname(os.path.abspath(__file__)))
        self.assertTrue(isinstance(size, int))

    def test_check_file_type(self):
        self.assertEqual(check_file_type("test.jpg"), 'Images')
        self.assertEqual(check_file_type("test.mp4"), 'Videos')
        self.assertEqual(check_file_type("test.mp3"), 'Audio')
        self.assertEqual(check_file_type("test.doc"), 'Documents')
        self.assertEqual(check_file_type("test.xyz"), 'Others')

    def test_get_space_details(self):
        details = get_space_details(os.path.dirname(os.path.abspath(__file__)))
        self.assertTrue(isinstance(details, dict))
        self.assertTrue('Images' in details and 'Videos' in details and
                        'Audio' in details and 'Documents' in details and
                        'Others' in details)

    def test_prepare_data_for_chart(self):
        file_types = {'Images': 1024, 'Videos': 2048, 'Audio': 3072,
                      'Documents': 4096, 'Others': 5120}
        total = sum(file_types.values())
        free = 1024
        sizes, labels = prepare_data_for_chart(file_types, total, free)
        self.assertEqual(len(sizes),
                         len(labels))
        self.assertEqual(labels[-1],
                         'Free space')

    def test_make_autopct(self):
        values = [1, 2, 3, 4, 5]
        autopct = make_autopct(values)
        self.assertEqual(autopct(20),
                         '20.00%  (3.00 GB)')


if __name__ == '__main__':
    unittest.main()
