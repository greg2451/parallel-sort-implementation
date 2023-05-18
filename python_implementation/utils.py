import random
import time

from parallel_sort_implementation import quicksort_cpp

from python_implementation.quick_sort_multiprocessed import quick_sort_mp


def swap_by_index(array, index_a, index_b):
    array[index_a], array[index_b] = array[index_b], array[index_a]
    return array


def partition(to_sort, left_index, right_index):
    # Pivot choice
    pivot = to_sort[right_index]

    greater_element_index = left_index
    for index in range(left_index, right_index):
        if to_sort[index] <= pivot:
            to_sort = swap_by_index(to_sort, index, greater_element_index)
            greater_element_index += 1

    # if right_index == greater_element_index:
    #     print(f"Pivot {pivot} was already in the right spot")

    # Pivot in its definite spot
    to_sort = swap_by_index(to_sort, right_index, greater_element_index)

    # Definite index of pivot
    return greater_element_index


def test_sort(sort_func, input_size, show_error=False):
    to_sort = [random.randint(0, input_size) for i in range(input_size)]

    start_time = time.time()
    if sort_func in [sorted, quick_sort_mp, quicksort_cpp]:
        res = sort_func(to_sort)
    else:
        res = sort_func(to_sort, 0, len(to_sort) - 1)
    end_time = time.time()
    if show_error and res != sorted(res):
        print(f"Error in {sort_func.__name__}")
    return end_time - start_time
