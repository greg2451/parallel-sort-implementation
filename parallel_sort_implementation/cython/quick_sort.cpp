// C++ Implementation of the Quick Sort Algorithm.
#include <iostream>
#include "partition.hpp"


void quickSort(double arr[], int start, int end)
{
	if (start >= end)
		return;

	int p = partition(arr, start, end);

	// Sorting the left part
	quickSort(arr, start, p - 1);

	// Sorting the right part
	quickSort(arr, p + 1, end);
}

void smartQuickSort(double arr[], int start, int end)
{
    if (start >= end)
        return;

    int p = smartPartition(arr, start, end);

    // Sorting the left part
    smartQuickSort(arr, start, p - 1);

    // Sorting the right part
    smartQuickSort(arr, p + 1, end);
}
