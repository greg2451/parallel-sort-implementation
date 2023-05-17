import random
import time


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

    if right_index == greater_element_index:
        print("Pivot {pivot} was already in the right spot")
    # Pivot in its definite spot
    to_sort = swap_by_index(to_sort, right_index, greater_element_index)

    # Definite index of pivot
    return greater_element_index


def test_sort(sort_func, input_size, show_error=False):
    to_sort = [random.randint(0, input_size) for i in range(input_size)]

    if sort_func == sorted:
        start_time = time.time()
        res = sort_func(to_sort)
        end_time = time.time()
        return end_time - start_time

    start_time = time.time()
    sort_func(to_sort, 0, len(to_sort) - 1)
    end_time = time.time()
    if show_error:
        print(f"Valid sort: {res == sorted(res)}.")
    return end_time - start_time
