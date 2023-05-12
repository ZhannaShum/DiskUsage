import shutil
from file_utils import get_size, get_space_details
from draw_utils import draw_pie_chart, prepare_data_for_chart


if __name__ == "__main__":
    root_path = '/'
    total_space = shutil.disk_usage(root_path).total
    used_space = get_size(root_path)
    file_types_space = get_space_details(root_path)
    free_space = total_space - used_space
    if free_space < 0:
        print(
            'Error: free space is negative. '
            'Please check the calculation of total and used space.')
    else:
        sizes, labels = prepare_data_for_chart(file_types_space, total_space, free_space)
        draw_pie_chart(sizes, labels)
