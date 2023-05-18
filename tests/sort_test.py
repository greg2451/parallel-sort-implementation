import unittest
import random
from typing import List

from parallel_sort_implementation.python import quick_sort, quick_sort_mp, quick_sort_th
from parallel_sort_implementation.cython import quicksort_cpp


def get_random_array(size: int, seed: int = 42) -> List[float]:
    random.seed(seed)
    return [random.random() for _ in range(size)]


class TestSort(unittest.TestCase):
    def test_standard_quicksort(self):
        example = get_random_array(1000)
        self.assertEqual(quick_sort(example, 0, len(example) - 1), sorted(example))

    def test_multiprocessed_quicksort(self):
        example = get_random_array(1000)
        self.assertEqual(quick_sort_mp(example), sorted(example))

    def test_multithreaded_quicksort(self):
        example = get_random_array(1000)
        self.assertEqual(quick_sort_th(example, 0, len(example) - 1), sorted(example))

    def test_cpp_quicksort(self):
        example = get_random_array(1000)
        self.assertEqual(quicksort_cpp(example), sorted(example))
