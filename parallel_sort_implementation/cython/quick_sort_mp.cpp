#include <iostream>
#include <omp.h>
#include "partition.cpp"

using namespace std;

void quickSortMP(double arr[], int start, int end)
{
    if (start >= end)
        return;

    int p = partition(arr, start, end);

    #pragma omp parallel sections
    {
        #pragma omp section
        quickSortV2(arr, start, p - 1);

        #pragma omp section
        quickSortV2(arr, p + 1, end);
    }
}
