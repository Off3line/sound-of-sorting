

def bubbleSort(arr):
        n = len(arr)
        swapped = False

        # Traverse through all array elements
        for i in range(n-1):
            for j in range(0, n-i-1):

                # Swap if the element found is greater
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j +1] = arr[j + 1], arr[j]

            if not swapped:
                # if we haven't needed to make a single swap, we can just exit the main loop.
                return


def insertionSort(A):
    if (n := len(A)) <= 1:
      return
    for i in range(1, n):
         
        key = A[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < A[j] :
                A[j+1] = A[j]
                j -= 1
        A[j+1] = key
 

def swap(A, i, j):

    if i != j:
        A[i], A[j] = A[j], A[i]


def quickSort(A, start, end):
   

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quickSort(A, start, pivotIdx - 1)
    yield from quickSort(A, pivotIdx + 1, end)
