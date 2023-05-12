import os
import fnmatch


def get_size(path):
    """
    Вычисляет общий размер всех файлов в каталоге, указанном по заданному пути, включая файлы в подкаталогах

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

    :param filename:
    :type filename:
    :return:
    :rtype:
    """
    if (
            fnmatch.fnmatch(filename, '*.jpg') or
            fnmatch.fnmatch(filename, '*.png') or
            fnmatch.fnmatch(filename, '*.jpeg') or
            fnmatch.fnmatch(filename, '*.gif')
    ):
        return 'Images'
    elif (
            fnmatch.fnmatch(filename, '*.mp4') or
            fnmatch.fnmatch(filename, '*.mkv') or
            fnmatch.fnmatch(filename, '*.flv') or
            fnmatch.fnmatch(filename, '*.avi')
    ):
        return 'Videos'
    elif (
            fnmatch.fnmatch(filename, '*.mp3') or
            fnmatch.fnmatch(filename, '*.wav') or
            fnmatch.fnmatch(filename, '*.flac') or
            fnmatch.fnmatch(filename, '*.aac') or
            fnmatch.fnmatch(filename, '*.ogg')
    ):
        return 'Audio'
    elif (
            fnmatch.fnmatch(filename, '*.doc') or
            fnmatch.fnmatch(filename, '*.docx') or
            fnmatch.fnmatch(filename, '*.pdf') or
            fnmatch.fnmatch(filename, '*.txt') or
            fnmatch.fnmatch(filename, '*.ppt') or
            fnmatch.fnmatch(filename, '*.xlsx') or
            fnmatch.fnmatch(filename, '*.xls')
    ):
        return 'Documents'
    else:
        return 'Others'


def get_space_details(path):
    """
    Возвращает общий размер всех файлов в заданном каталоге

    :param path: Путь к каталогу для поиска.
    :type path: str
    :return: Общий размер всех файлов в каталоге.
    :rtype: int
    """
    file_types = {'Images': 0, 'Videos': 0, 'Audio': 0, 'Documents': 0,
                  'Others': 0}
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            file_type = check_file_type(f)
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                try:
                    file_types[file_type] += os.path.getsize(fp)
                except OSError:
                    pass
    return file_types
