// C++ Implementation of the Quick Sort Algorithm.
#include <iostream>
#include "partition.cpp"


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
