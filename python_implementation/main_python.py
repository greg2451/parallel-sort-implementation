from python_implementation.test_performance import plot_perf, test_single_perf


if __name__ == "__main__":
    test_single_perf(input_size=10000)

    input_sizes = [i for i in range(100, 10000, 1000)]
    print(input_sizes)
    plot_perf(input_sizes=input_sizes, include_threaded=True)
