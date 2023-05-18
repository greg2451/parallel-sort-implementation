# cython: language_level=3
# distutils: language=c++
import numpy as np
cimport numpy as np

cdef extern from "quick_sort.cpp":
    void quickSort(double *arr, int start, int end) nogil

def quicksort_simple(list arr):
    cdef np.ndarray[np.float64_t, ndim=1] np_arr = np.array(arr, dtype=np.float64)
    cdef int n = np_arr.shape[0]
    cdef double* ptr = <double*>np.PyArray_DATA(np_arr)
    quickSort(ptr, 0, n - 1)
    return np_arr.tolist()

