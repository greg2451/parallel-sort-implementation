from python_implementation.plain_quick_sort import quick_sort
from quick_sort_multiprocessed import quick_sort_mp
from python_implementation.quick_sort_threaded import quick_sort_th
from python_implementation.test_performance import plot_perf, test_single_perf


if __name__ == "__main__":
    # test_single_perf(input_size=10000)

    input_sizes = [i for i in range(100, 10000, 1000)]
    print(input_sizes)
    plot_perf(input_sizes=input_sizes, include_threaded=True)
