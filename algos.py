

def bubbleSort(arr):
    n = len(arr)
    if n == 1:
        return
    
    swapped = True
    for i in range(n-1):
        if not swapped:
            break
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr


def insertionSort(A):

    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            j -= 1
            yield A


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
