import random
import time
from python_implementation.plain_quick_sort import quick_sort
from python_implementation.quick_sort_multi_processed import quick_sort_mp
from python_implementation.quick_sort_threaded import quick_sort_th
from python_implementation.test_performance import test_single_perf


if __name__ == "__main__":

    example = [random.randint(0, 1000) for i in range(10)]
    start = time.time()
    quick_sort_mp(example, 0, len(example)-1)
    end = time.time()
    print(end-start)
    print(example == sorted(example))

    input_sizes = [i for i in range(10000, 1000000, 1000)]

    # test_single_perf(input_size=1000)
    # plot_perf(input_sizes=input_sizes)
