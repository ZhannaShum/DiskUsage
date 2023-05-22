import unittest
import os
import tempfile
import shutil
from file_utils import get_size, check_file_type, get_space_details
from draw_utils import make_autopct


class TestFileUtils(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_get_size(self):
        # Создаем тестовый файл размером 1024 байта
        test_file = os.path.join(self.test_dir, 'test_file')
        with open(test_file, 'wb') as f:
            f.write(os.urandom(1024))

        # Проверяем, что функция get_size возвращает правильный размер
        self.assertEqual(get_size(self.test_dir), 1024)

    def test_check_file_type(self):
        # Создаем тестовые файлы различных типов
        test_files = ['test.doc', 'test.mp3', 'test.png', 'test.py',
                      'unknown.xyz']
        for file_name in test_files:
            with open(os.path.join(self.test_dir, file_name), 'wb') as f:
                f.write(b'')

        # Проверяем, что функция check_file_type возвращает правильные типы файлов
        self.assertEqual(check_file_type('test.doc'), ('Documents', '*.doc'))
        self.assertEqual(check_file_type('test.mp3'), ('Audio', '*.mp3'))
        self.assertEqual(check_file_type('test.png'), ('Images', '*.png'))
        self.assertEqual(check_file_type('test.py'), ('Programs', '*.py'))

    def test_prepare_data_for_chart(self):
        # Создаем тестовые данные для проверки функции
        file_types = {'Images': 1000, 'Videos': 2000, 'Audio': 1500}
        total = 10000
        free = 5500


    def test_make_autopct(self):
        # Создаем тестовые данные для проверки функции
        values = [50, 25, 25]

        # Проверяем, что функция make_autopct возвращает правильные значения
        autopct_func = make_autopct(values)
        self.assertEqual(autopct_func(20), '20.00 GB')
        self.assertEqual(autopct_func(10), '10.00 GB')
        self.assertEqual(autopct_func(5), '5.00 GB')

    def test_get_space_details(self):
        # Создаем тестовые файлы различных типов
        test_files = ['test.doc', 'test.mp3', 'test.png', 'test.py',
                      'unknown.xyz']
        for file_name in test_files:
            with open(os.path.join(self.test_dir, file_name), 'wb') as f:
                f.write(b'')

        file_types, file_counts = get_space_details(self.test_dir)

        # Проверяем, что функция возвращает правильные размеры и количество файлов
        self.assertEqual(file_types['Documents'], os.path.getsize(
            os.path.join(self.test_dir, 'test.doc')))
        self.assertEqual(file_counts['Documents']['*.doc'], 1)
        self.assertEqual(file_counts['Others']['.xyz'], 1)

    def test_non_existing_path_get_size(self):
        # Проверяем, что функция обрабатывает несуществующий путь
        self.assertEqual(get_size('/non/existing/path'), 0)

    def test_non_existing_path_get_space_details(self):
        # Проверяем, что функция обрабатывает несуществующий путь
        file_types, file_counts = get_space_details('/non/existing/path')
        self.assertEqual(sum(file_types.values()), 0)
        for counts in file_counts.values():
            self.assertEqual(sum(counts.values()), 0)


if __name__ == '__main__':
    unittest.main()
