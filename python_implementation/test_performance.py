import matplotlib.pyplot as plt
from tqdm import tqdm

from python_implementation.plain_quick_sort import quick_sort
from python_implementation.quick_sort_multiprocessed import quick_sort_mp
from python_implementation.quick_sort_threaded import quick_sort_th
from python_implementation.utils import test_sort


def plot_perf(input_sizes: list, include_threaded: bool):
    gold_standard_times = []
    regular_quicksort_times = []

    multithreaded_quicksort_times = []
    multiprocess_quicksort_times = []

    for input_size in tqdm(input_sizes):
        gold_standard_time = test_sort(sorted, input_size)
        regular_quicksort_time = test_sort(quick_sort, input_size)
        if include_threaded:
            multithreaded_quicksort_time = test_sort(quick_sort_th, input_size)
        multiprocess_quicksort_time = test_sort(quick_sort_mp, input_size)

        gold_standard_times.append(gold_standard_time)
        regular_quicksort_times.append(regular_quicksort_time)
        if include_threaded:
            multithreaded_quicksort_times.append(multithreaded_quicksort_time)
        multiprocess_quicksort_times.append(multiprocess_quicksort_time)

    plt.plot(input_sizes, gold_standard_times, label="Gold Standard")
    plt.plot(input_sizes, regular_quicksort_times, label="Regular Quicksort")
    if include_threaded:
        plt.plot(
            input_sizes, multithreaded_quicksort_times, label="Multithreaded Quicksort"
        )
    plt.plot(input_sizes, multiprocess_quicksort_times, label="Multiprocess Quicksort")
    plt.xlabel("Input Size")
    plt.ylabel("Execution")
    plt.legend(loc="upper left")
    plt.show()


def test_single_perf(input_size):
    print(f"With input size {input_size}:")
    for sort_func in [sorted, quick_sort, quick_sort_th, quick_sort_mp]:
        print(f"{sort_func.__name__}: {round(test_sort(sort_func, input_size),3)}s")
