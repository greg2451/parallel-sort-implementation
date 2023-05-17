
import multiprocessing as mp

from python_implementation.utils import partition


def quick_sort_mp(to_sort, left_index, right_index):
    if left_index < right_index:
        pivot_index = partition(to_sort, left_index, right_index)

        # Left side
        left_process = mp.Process(target=quick_sort_mp, args=(
            to_sort, left_index, pivot_index-1))
        left_process.start()

        # Right side
        right_process = mp.Process(target=quick_sort_mp, args=(
            to_sort, pivot_index+1, right_index))
        right_process.start()

        # Wait for the processes to finish
        left_process.join()
        right_process.join()

    # Add a base case to return the sorted array
    else:
        print(to_sort)
        print(
            f"left index {left_index} greater than right index {right_index}")
        return [to_sort[left_index]]

    return quick_sort_mp(to_sort, left_index, pivot_index-1) + \
        quick_sort_mp(to_sort, pivot_index+1, right_index)
