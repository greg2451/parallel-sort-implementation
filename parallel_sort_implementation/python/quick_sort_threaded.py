import threading

from parallel_sort_implementation.python.utils import partition


def quick_sort_th(to_sort: list, left_index, right_index):
    if left_index < right_index:
        pivot_index = partition(to_sort, left_index, right_index)

        # Create threads for left and right sub-arrays
        left_thread = threading.Thread(
            target=quick_sort_th, args=(to_sort, left_index, pivot_index - 1)
        )
        right_thread = threading.Thread(
            target=quick_sort_th, args=(to_sort, pivot_index + 1, right_index)
        )

        # Start threads
        left_thread.start()
        right_thread.start()

        # Wait for threads to complete
        left_thread.join()
        right_thread.join()

    return to_sort
