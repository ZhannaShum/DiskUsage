import matplotlib.pyplot as plt


def prepare_data_for_chart(file_types, total, free):
    """
    Подготавливает данные для диаграммы,
    вычисляя размеры типов файлов и свободное пространство в гигабайтах и создавая метки.

    :param file_types: Количество каждого типа файла.
    :type file_types: dict
    :param total: Общий размер хранилища в байтах.
    :type total: int
    :param free: Объем свободного пространства в байтах.
    :type free: int
    :return:  Кортеж, содержащий два списка - sizes и labels, где sizes содержит размеры типов файлов и
свободное пространство в гигабайтах, а labels содержит метки для каждого размера
    :rtype: tuple
    """
    sizes = [file_types[key] / (1024 ** 3) for key in file_types]
    sizes.append(free / (1024 ** 3))
    legend_labels = [f"{key} ({(size / total) * 100:.2f}%)" for key, size in
                     file_types.items()]
    legend_labels.append(f"Free space ({(free / total) * 100:.2f}%)")
    return sizes, legend_labels


def make_autopct(values):
    """
    Возвращает замыкание, которое форматирует процент и значение каждого
    кругового среза на диаграмме

    :param values: Размеры каждой части круговой диаграммы.
    :type values: list
    :return: Замыкание, которое принимает процент от каждого фрагмента в качестве
    входных данных и возвращает строку, содержащую процент и значение в гигабайтах.
    :rtype: callable
    """
    def my_autopct(pct):
        """
        Форматирует процент и значение каждого кругового среза в диаграмме

        :param pct: Процентная доля среза.
        :type pct: float
        :return: Процент и значение в гигабайтах.
        :rtype: str
        """
        total = sum(values)
        val = pct * total / 100.0
        return '{v:.2f} GB'.format(v=val)

    return my_autopct


def draw_pie_chart(sizes, legend_labels):
    """
    Рисует круговую диаграмму, используя предоставленные размеры и метки

    :param sizes: Список размеров для каждого среза диаграммы.
    :type sizes: list[float]
    :param legend_labels: Список меток для каждого среза диаграммы.
    :type legend_labels: list[str]
    :return: None
    :rtype: None
    """
    fig1, ax1 = plt.subplots()
    wedges, _, _ = ax1.pie(sizes, autopct=make_autopct(sizes))
    ax1.axis('equal')
    plt.subplots_adjust(right=0.6)
    plt.legend(wedges, legend_labels, title="Categories", loc="center left",
               bbox_to_anchor=(1, 0, 0.5, 1))
    plt.show()
