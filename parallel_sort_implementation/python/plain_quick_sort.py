from parallel_sort_implementation.python.utils import partition, smart_partition


def quick_sort(to_sort: list, left_index, right_index):
    if left_index < right_index:
        pivot_index = partition(to_sort, left_index, right_index)

        # Left side
        quick_sort(to_sort, left_index, pivot_index - 1)

        # Right side
        quick_sort(to_sort, pivot_index + 1, right_index)
    return to_sort


def smart_quick_sort(to_sort: list, left_index, right_index):
    if left_index < right_index:
        pivot_index = smart_partition(to_sort, left_index, right_index)

        # Left side
        smart_quick_sort(to_sort, left_index, pivot_index - 1)

        # Right side
        smart_quick_sort(to_sort, pivot_index + 1, right_index)
    return to_sort
