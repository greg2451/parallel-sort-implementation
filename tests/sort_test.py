# This file is a test file for all quicksorts implementation

import unittest
import random
from typing import List

import numpy as np

from python_implementation.plain_quick_sort import quick_sort
from python_implementation.quick_sort_multiprocessed import quick_sort_mp
from python_implementation.quick_sort_threaded import quick_sort_th
from parallel_sort_implementation import quicksort_cpp


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

    def test_cpp_quicksort_v2(self):
        example = get_random_array(1000)
        self.assertEqual(quicksort_cpp(example), sorted(example))
