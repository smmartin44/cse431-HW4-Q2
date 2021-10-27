############################
# Hybrid Timsort Algorithm
# using Merge sort and
# Insertion Sort
############################

# Will start with the same merge and insertion sort algorithms
# from Q1 of the homework

import random
import timeit
import copy

# Python program for implementation of MergeSort
# Algorithm from: https://www.geeksforgeeks.org/merge-sort/
# FOR TIM SORT: will add a partition value k parameter
def mergeSort(arr, k):
    if len(arr) > 1:

        # if the len of the array is equal to/below the k threshold, use insertion sort
        if len(arr) <= k:
            arr = insertionSort(arr)

        else:
            # Finding the mid of the array
            mid = len(arr) // 2

            # Dividing the array elements
            L = arr[:mid]

            # into 2 halves
            R = arr[mid:]

            # Sorting the first half
            mergeSort(L, k)

            # Sorting the second half
            mergeSort(R, k)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    return arr


# Function to do insertion sort
# Algorithm from: https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def main():
    # I will use an input file with the different n values to test
    # Then random lists of length n will be initialized
    fp = open("n_inputs_Q2.txt", "r")
    master_lists = []
    for line in fp:
        # Create 3 lists for each length of input so we can average out the time per input
        # with different lists (won't be timing this part)
        for i in range(3):
            master_lists.append([random.randint(0, 500) for i in range(int(line.strip()))])

    # How to sort a list of lists by length of the sublists
    # https://stackoverflow.com/questions/30346356/how-to-sort-list-of-lists-according-to-length-of-sublists/30346379
    master_lists.sort(key=len)

    # Iterate over k input file for the different k thresholds to test
    fp = open("k_values.txt", "r")
    k_vals = [int(line.strip()) for line in fp]

    # Using the timeit module to measure elapsed time for each sorting operation
    # Used website below to remind myself of the timeit implementation
    # https://www.geeksforgeeks.org/how-to-measure-elapsed-time-in-python/
    for inputs in master_lists:
        print("length =", len(inputs))
        for k in k_vals:
            vals = copy.deepcopy(inputs)
            print(timeit.timeit(lambda: mergeSort(vals, k), number=1))
if __name__ == "__main__":
    main()
