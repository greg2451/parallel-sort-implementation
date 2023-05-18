import matplotlib.pyplot as plt
from tqdm import tqdm

from parallel_sort_implementation.python import (
    quick_sort,
    quick_sort_mp,
    quick_sort_th,
)
from parallel_sort_implementation.python.utils import test_sort
from parallel_sort_implementation.cython import quicksort_cpp


def plot_perf(input_sizes: list, include_threaded: bool):
    gold_standard_times = []
    regular_quicksort_times = []

    multithreaded_quicksort_times = []
    multiprocess_quicksort_times = []
    cpp_quicksort_times = []

    for input_size in tqdm(input_sizes):
        gold_standard_time = test_sort(sorted, input_size)
        regular_quicksort_time = test_sort(quick_sort, input_size)
        if include_threaded:
            multithreaded_quicksort_time = test_sort(quick_sort_th, input_size)
        multiprocess_quicksort_time = test_sort(quick_sort_mp, input_size)
        cpp_quicksort_time = test_sort(quicksort_cpp, input_size)

        gold_standard_times.append(gold_standard_time)
        regular_quicksort_times.append(regular_quicksort_time)
        if include_threaded:
            multithreaded_quicksort_times.append(multithreaded_quicksort_time)
        multiprocess_quicksort_times.append(multiprocess_quicksort_time)
        cpp_quicksort_times.append(cpp_quicksort_time)

    plt.plot(input_sizes, gold_standard_times, label="Gold Standard")
    plt.plot(input_sizes, regular_quicksort_times, label="Regular Quicksort")
    if include_threaded:
        plt.plot(
            input_sizes, multithreaded_quicksort_times, label="Multithreaded Quicksort"
        )
    plt.plot(input_sizes, multiprocess_quicksort_times, label="Multiprocess Quicksort")
    plt.plot(input_sizes, cpp_quicksort_times, label="C++ Quicksort")
    plt.xlabel("Input Size")
    plt.ylabel("Execution")
    plt.legend(loc="upper left")
    plt.show()


def test_single_perf(input_size):
    print(f"With input size {input_size}:")
    for sort_func in [
        sorted,
        quick_sort,
        quick_sort_th,
        quick_sort_mp,
        quicksort_cpp,
    ]:
        print(f"{sort_func.__name__}: {round(test_sort(sort_func, input_size),3)}s")