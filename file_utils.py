import os
import fnmatch

extensions = {
    'Images':
        ['*.jpg', '*.png', '*.jpeg', '*.gif', '*.tiff', '*.bmp', '*.ico'],
    'Videos':
        ['*.mp4', '*.mkv', '*.flv', '*.avi', '*.mov', '*.wmv', '*.mpeg',
         '*.m4v'],
    'Audio':
        ['*.mp3', '*.wav', '*.flac', '*.aac', '*.ogg', '*.m4a', '*.aiff'],
    'Documents':
        ['*.doc', '*.docx', '*.pdf', '*.txt', '*.ppt', '*.pptx', '*.xlsx',
         '*.xls', '*.odt'],
    'Archives': ['*.zip', '*.rar', '*.7z', '*.gzip', '*.tar', '*.iso', '*.jar',
                 '*.apk'],
    'Webpages':
        ['*.html', '*.htm', '*.mht', '*.xml', '*.css', '*.json', '*.js'],
    'Torrents': ['*.torrent'],
    'Ebooks':
        ['*.fb2', '*.epub', '*.mobi', '*.azw', '*.azw3', '*.lit'],
    'Programs':
        ['*.exe', '*.bat', '*.sh', '*.py', '*.js', '*.php', '*.pl',
         '*.rb', '*.java', '*.class', '*.dll'],
    'Databases':
        ['*.sql', '*.db', '*.dbf', '*.mdb', '*.accdb', '*.sqlite',
         '*.sqlite3'],
    'Fonts': ['*.ttf', '*.otf', '*.fon', '*.fnt']
}


def get_size(path):
    """
    Вычисляет общий размер всех файлов в каталоге, указанном по заданному пути,
    включая файлы в подкаталогах

    :param path: Путь к каталогу для поиска.
    :type path: str
    :return: Общий размер всех файлов в каталоге.
    :rtype: int
    """
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                try:
                    total += os.path.getsize(fp)
                except OSError:
                    pass
    return total


def check_file_type(filename):
    """
    Возвращает тип файла на основе его расширения

    :param filename: Название файла для проверки типа.
    :type filename: str
    :return: Кортеж, содержащий категорию и расширение файла.
             Если расширение не распознано, возвращается ("Others", "*.*").
    :rtype: tuple(str, str)
    """
    for category, exts in extensions.items():
        for ext in exts:
            if fnmatch.fnmatch(filename, ext):
                return category, ext
    return 'Others', os.path.splitext(filename)[1] or '*.*'


def get_space_details(path):
    """
    Возвращает общий размер всех файлов в заданном каталоге

    :param path: Путь к каталогу для поиска.
    :type path: str
    :return: Общий размер всех файлов в каталоге.
    :rtype: int
    """
    file_types = {key: 0 for key in extensions}
    file_types['Others'] = 0

    file_counts = {key: {ext: 0 for ext in exts} for key, exts in
                   extensions.items()}
    file_counts['Others'] = {}

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            file_type, ext = check_file_type(f)
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                try:
                    file_types[file_type] += os.path.getsize(fp)
                    if ext not in file_counts[file_type]:
                        file_counts[file_type][ext] = 0
                    file_counts[file_type][ext] += 1
                except OSError:
                    pass
    return file_types, file_counts
