# cython: language_level=3
# distutils: language=c++
import numpy as np
cimport numpy as np

cdef extern from "quick_sort.cpp":
    void quickSort(double *arr, int start, int end) nogil


def quicksort(list arr):
    cdef np.ndarray[np.float64_t, ndim=1] np_arr = np.array(arr, dtype=np.float64)
    cdef int n = np_arr.shape[0]
    cdef double* ptr = <double*>np.PyArray_DATA(np_arr)
    quickSort(ptr, 0, n - 1)
    return np_arr.tolist()

cdef extern from "partition.cpp":
    int partition(double *arr, int start, int end) nogil

def partition_cpp(list arr, int start, int end):
    cdef np.ndarray[np.float64_t, ndim=1] np_arr = np.array(arr, dtype=np.float64)
    cdef int n = np_arr.shape[0]
    cdef double* ptr = <double*>np.PyArray_DATA(np_arr)
    return partition(ptr, start, end)

cdef extern from "quick_sort.cpp":
    void smartQuickSort(double *arr, int start, int end) nogil


def smart_quicksort(list arr):
    cdef np.ndarray[np.float64_t, ndim=1] np_arr = np.array(arr, dtype=np.float64)
    cdef int n = np_arr.shape[0]
    cdef double* ptr = <double*>np.PyArray_DATA(np_arr)
    smartQuickSort(ptr, 0, n - 1)
    return np_arr.tolist()

# WIP: Parallel quicksort. Not working yet on Mac.
# from Cython.Includes.openmp import omp_set_num_threads
#
# cdef extern from "quick_sort_mp.cpp":
#     void quickSortMP(double *arr, int start, int end) nogil
#
# def quicksort_mp(list arr):
#     cdef np.ndarray[np.float64_t, ndim=1] np_arr = np.array(arr, dtype=np.float64)
#     cdef int n = np_arr.shape[0]
#     cdef double* ptr = <double*>np.PyArray_DATA(np_arr)
#
#     # Set the maximum number of threads
#     omp_set_num_threads(10)
#
#     quickSortMP(ptr, 0, n - 1)
#     return np_arr
