from parallel_sort_implementation.python.test_performance import (
    plot_perf,
    test_single_perf,
)


if __name__ == "__main__":
    test_single_perf(input_size=10000)

    input_sizes = [i**2 for i in range(1, 2000, 100)]
    print(input_sizes)
    plot_perf(input_sizes=input_sizes, include_multithreaded_and_multiprocessed=True)
