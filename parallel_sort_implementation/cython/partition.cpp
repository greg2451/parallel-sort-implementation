#include <iostream>
#include "partition.hpp"

using namespace std;

int partition(double arr[], int start, int end)
{
    double pivot = arr[start];

    int count = 0;
    for (int i = start + 1; i <= end; i++) {
        if (arr[i] <= pivot)
            count++;
    }

    int pivotIndex = start + count;
    swap(arr[pivotIndex], arr[start]);

    int i = start, j = end;
    while (i < pivotIndex && j > pivotIndex) {
        while (arr[i] <= pivot) {
            i++;
        }

        while (arr[j] > pivot) {
            j--;
        }

        if (i < pivotIndex && j > pivotIndex) {
            swap(arr[i++], arr[j--]);
        }
    }

    return pivotIndex;
}

int smartPartition(double arr[], int start, int end)
{
    int mid = (start + end) / 2;
    if (arr[mid] < arr[start]) {
        swap(arr[start], arr[mid]);
    }
    if (arr[end] < arr[start]) {
        swap(arr[start], arr[end]);
    }
    if (arr[mid] < arr[end]) {
        swap(arr[mid], arr[end]);
    }

    double pivot = arr[end];

    int count = 0;
    for (int i = start + 1; i <= end; i++) {
        if (arr[i] <= pivot)
            count++;
    }

    int pivotIndex = start + count;
    swap(arr[pivotIndex], arr[end]);

    int i = start, j = end;
    while (i < j) {
        while (arr[i] <= pivot) {
            i++;
        }

        while (arr[j] > pivot) {
            j--;
        }

        if (i < j) {
            swap(arr[i++], arr[j--]);
        }
    }

    return j;
}
